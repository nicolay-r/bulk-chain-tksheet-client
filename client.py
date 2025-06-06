import asyncio
import tkinter as tk

from bulk_chain.api import iter_content
from bulk_chain.core.utils import dynamic_init
from tksheet import Sheet

from utils import iter_test_jsonl_samples

COLUMNS = [
    "r_aspect",
    "r_opinion",
    "r_polarity",
    "r_label"
]


def callback(chunk, col, row, sheet):

    # Update cell data.
    c =COLUMNS.index(col)
    new_cell_data = sheet.get_cell_data(r=row, c=c) + chunk
    sheet.set_cell_data(r=row, c=c, value=new_cell_data, redraw=True)

    # Setup color.
    bg = "lightblue"
    if col == "r_label":
        content = new_cell_data.lower()
        if "positive" in content and "negative" not in content:
            bg = "lightgreen"
        elif "positive" not in content and "negative" in content:
            bg = "lightcoral"
        else:
            bg = "lightyellow"

    sheet.highlight_cells(row, c, bg=bg, fg="black")  # Apply cell coloring

    sheet.update()


def limit_total(iter, n):
    for ind, i in enumerate(iter):
        if ind > n:
            break
        yield i


def on_fill_button_click(sheet):
    """Event handler for the button to populate the sheet."""

    data_it = iter_content(input_dicts_it=limit_total(iter_test_jsonl_samples("data/sample.jsonl"), n=sheet.total_rows()),
                           llm=llm,
                           return_batch=False,
                           batch_size=5,
                           infer_mode="batch_stream_async",
                           return_mode="chunk",
                           event_loop=asyncio.get_event_loop_policy().get_event_loop(),
                           schema="data/thor_cot_schema.json")

    for ind, col, chunk in data_it:
        callback(chunk=chunk, row=ind, col=col, sheet=sheet)

    sheet.redraw()


def main():
    root = tk.Tk()
    root.title("Sentiment Analysis Demo (meta/meta-llama-3-70b-instruct)")
    root.geometry("1320x800")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    sheet = Sheet(root, total_rows=5, total_columns=len(COLUMNS))
    sheet.grid(row=0, column=0, sticky="nsew")
    
    sheet.set_column_widths([500, 300, 300, 150])
    sheet.set_row_heights([100] * sheet.total_rows())

    button = tk.Button(root, text="Fill Table", command=lambda: on_fill_button_click(sheet))
    button.grid(row=1, column=0, pady=10)

    sheet.enable_bindings()
    root.mainloop()


if __name__ == "__main__":
    API_TOKEN = None
    assert API_TOKEN is not None, "You have to setup API token first!"
    llm = dynamic_init(class_filepath="replicate_104.py",
                       class_name="Replicate")(api_token=API_TOKEN,
                                               model_name="meta/meta-llama-3-70b-instruct",
                                               stream=True)
    main()


