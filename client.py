import tkinter as tk

from bulk_chain.api import iter_content
from bulk_chain.core.utils import dynamic_init
from tksheet import Sheet

from utils import iter_test_jsonl_samples


def callback(chunk, info, context, sheet):

    reg = context["cols"]

    # Register column number.
    if info["param"] not in reg:
        reg[info["param"]] = len(reg)

    # Defining row index.
    row = info["ind"] + context["row_ind"]

    # Update cell data.
    col = reg[info["param"]]
    new_cell_data = sheet.get_cell_data(r=row, c=col) + chunk
    sheet.set_cell_data(r=row, c=col, value=new_cell_data, redraw=True)

    # Setup color.
    bg = "lightblue"
    if info["param"] == "r_label":
        content = new_cell_data.lower()
        if "positive" in content and "negative" not in content:
            bg = "lightgreen"
        elif "positive" not in content and "negative" in content:
            bg = "lightcoral"
        else:
            bg = "lightyellow"

    sheet.highlight_cells(row, col, bg=bg, fg="black")  # Apply cell coloring

    sheet.update()


def on_fill_button_click(sheet):
    """Event handler for the button to populate the sheet."""

    batch_size = 1

    ctx = {"row_ind": 0, "cols": {}}

    data_it = iter_content(input_dicts_it=iter_test_jsonl_samples("data/sample.jsonl"),
                           llm=llm,
                           return_batch=False,
                           batch_size=1,
                           callback_stream_func=lambda chunk, info: callback(chunk, info, ctx, sheet),
                           schema="data/thor_cot_schema.json")

    for _ in data_it:
        ctx["row_ind"] += batch_size

    sheet.redraw()


def main():
    root = tk.Tk()
    root.title("Sentiment Analysis Demo (meta/meta-llama-3-70b-instruct)")
    root.geometry("850x800")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    sheet = Sheet(root, total_rows=10, total_columns=8)
    sheet.grid(row=0, column=0, sticky="nsew")
    
    sheet.set_column_widths([200] * 8)
    sheet.set_row_heights([100] * 10)

    button = tk.Button(root, text="Fill Table", command=lambda: on_fill_button_click(sheet))
    button.grid(row=1, column=0, pady=10)

    sheet.enable_bindings()
    root.mainloop()


if __name__ == "__main__":
    llm = dynamic_init(class_dir=".",
                       class_filepath="replicate_104.py",
                       class_name="Replicate")(api_token="<NONE>",
                                               model_name="meta/meta-llama-3-70b-instruct",
                                               stream=True)
    main()


