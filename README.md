# TkSheet Client for `bulk-chain`
<p align="center">
  <a href="https://github.com/nicolay-r/bulk-chain"><b>bulk-chain</b>↗️</a>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/5bc8cddc-6d22-41ec-80f9-9df433f2d566" width="300" height="auto"/>
</p>

> This project illustrates embedding of a no-string framework `bulk-chain` for reasoning over your data using predefined scheme. 
It supports streamed output for filling table content.

# Installation

```bash
pip install -r dependencies.txt
```

## API

Please take a look at the [**related Wiki page**](https://github.com/nicolay-r/bulk-chain/wiki)


# Embed your LLM

All you have to do is to implement `BaseLM` class, that includes:
* `__init__` -- for setting up *batching mode support* and (optional) *model name*;
* `ask(prompt)` -- infer your model with the given `prompt`.

See examples with models [at nlp-thirdgate 🌌](https://github.com/nicolay-r/nlp-thirdgate?tab=readme-ov-file#llm).


# Dependencies
Powered by `bulk-chain`
* https://github.com/nicolay-r/bulk-chain

<img src="https://github.com/user-attachments/assets/dc17a0bf-3e6d-4331-897e-7c8eef55f139" width="200" height="auto"/>
