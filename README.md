# karpatkit

Work in progress

This repository contains two python packages:
- [defabipedia](src/defabipedia/README.md)
- karpatkit

## Installation

[Install uv](https://docs.astral.sh/uv/getting-started/installation/)

## Development

Install or update the virtualenv (will be created in .venv):

`make install`

### Run tests

`KKIT_CFG=path/to/config.json uv run pytest -vs` or use `KKIT_CFG=path/to/config.json make test`

### Format

`make pretty`