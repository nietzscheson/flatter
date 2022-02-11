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
This results in the following running containers:
```bash
> $ docker-compose ps
               Name                              Command                  State                        Ports
------------------------------------------------------------------------------------------------------------------------------
core                                  /bin/sh -c gunicorn --bind ...   Up             0.0.0.0:8000->8000/tcp,:::8000->8000/tcp
postgres                              docker-entrypoint.sh postgres    Up (healthy)   0.0.0.0:5432->5432/tcp,:::5432->5432/tcp
raizen-iot-challenge_default-core_1   python3                          Exit 0
```
4. Testing features:
```bash
$ make test
```
4. Import the dataset:
```bash
$ make import
```
The resources are:

- http://localhost:8000/highest-co2
- http://localhost:8000/hottest-temperature
- http://localhost:8000/highest-humidity
