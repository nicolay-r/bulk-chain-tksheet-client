# TkSheet Client for `bulk-chain`
![](https://img.shields.io/badge/Python-3.9-brightgreen.svg)
[![PyPI bulk-chain downloads](https://img.shields.io/pypi/dm/bulk-chain.svg)](https://pypistats.org/packages/bulk-chain)

> **Update 16/05/2025:** We support `batch-stream-async` output in `bulk-chain-1.1.0` 🔥

<p align="center">
  <a href="https://github.com/nicolay-r/bulk-chain"><b>bulk-chain</b>↗️</a>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/81e62b7b-a3cf-42ce-88cd-d648ffdf3b41" width="900" height="auto"/>
</p>

> This project illustrates embedding of a no-string framework `bulk-chain` for reasoning over your data using predefined scheme. 
It supports streamed output for filling table content.

# Installation

```bash
pip install -r dependencies.txt
```

## Usage

Please take a look at the [**related Wiki page**](https://github.com/nicolay-r/bulk-chain/wiki)

```python
data_it = iter_content(
  input_dicts_it=islice(iter_test_jsonl_samples("data/sample.jsonl"), sheet.total_rows()),
  llm=llm,
  return_batch=False,
  batch_size=5,
  infer_mode="batch_stream_async",  # <- async stream batching mode.
  return_mode="chunk",              # <- return chunks.
  schema="data/thor_cot_schema.json"
)

for ind, col, chunk in data_it:
    callback(chunk=chunk, row=ind, col=col, sheet=sheet)
```


# Embed your LLM

All you have to do is to implement `BaseLM` class, that includes:
* `__init__` -- for setting up *batching mode support* and (optional) *model name*;
* `ask(prompt)` -- infer your model with the given `prompt`.

See examples with models [at nlp-thirdgate 🌌](https://github.com/nicolay-r/nlp-thirdgate?tab=readme-ov-file#llm).


# Dependencies
Powered by `bulk-chain`
* https://github.com/nicolay-r/bulk-chain

<img src="https://github.com/user-attachments/assets/dc17a0bf-3e6d-4331-897e-7c8eef55f139" width="200" height="auto"/>
