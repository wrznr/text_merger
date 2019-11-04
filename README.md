# text_merger
Simple approach to align and merge two versions of the same (OCR) text

## Installation
`text_merger` is implemented in Python 3. In the following, we assume a working Python 3 (tested version on 3.6) installation.

### Virtual environment
Using a [virtual environment](https://www.python.org/dev/peps/pep-0405/) is highly recommended, although not strictly necessary for installing `text_merger`. Create a virtual environement in a subdirectory of your choice (e.g. `env`) using
```console
$ python3 -m venv env
```
and activate it.
```console
$ . env/bin/activate
```

### Python requirements
`text_merger` uses various 3rd party Python packages which may best be installed using `pip`:
```console
(env) $ pip install -r requirements.txt
```
Finally, `text_merger` itself can be installed via `pip`:
```console
(env) $ pip install .
```

## Invocation
`text_merger` shipes with a help message explaining its usage:
```console
(env) $ text_merger --help
Usage: text_merger [OPTIONS]

Options:
  -t, --text FILENAME        Text file 1  [required]
  -T, --Text FILENAME        Text file 2  [required]
  -d, --dictionary FILENAME  Gold dictionary  [required]
  --help                     Show this message and exit.
```
A sample invocation could look like:
```console
(env) $ text_merger -t left.txt -T right.txt -d dict.txt
```
