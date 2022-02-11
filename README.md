Flatter
==============

Flat any list object with N dimensions on Python

# Installation

1. Install using pip:

```bash
$ pip install git+https://github.com/nietzscheson/flatter.git
```
2. Import the library:

```python
$ from flatter import flatter
```
3. Flat your object:
```python
...

flatter = flatter([1, 2, [3, [4]]])
# [1, 2, 3, 4]

```
# For testing

1. Please clone this repository:
```bash
$ git clone https://github.com/nietzscheson/flatter
```
2. Create the virtual environment:
```bash
$ python -m venv venv
```
4. Install the dev dependencies:
```bash
$ make dependencies.dev
```
5. Run test:
```bash
$ make test
```
