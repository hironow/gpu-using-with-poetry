# gpu(cuda) using pytorch with poetry

## install

```bash
# create venv
$ python -m venv .venv
...

# install dependency
$ poetry install
...
```

## Usage

```bash
# run check script
$ poetry run python main.py
numpy:  1.24.3
torch:  2.0.1+cu118
torch cuda:  True
```

### add dependency

```bash
# install for prod
$ poetry add numpy
...
```

```bash
# install for dev
$ poetry add --group dev black
...
```

## reference

* <https://stackoverflow.com/questions/59158044/poetry-and-pytorch>
