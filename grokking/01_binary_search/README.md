# grokking
## 01_binary_search

### Run

```sh
$ make run
python main.py
numbers: [30, 31, 34, 35, 37, 44]
x: 45
result: None

$ make run
python main.py
numbers: [29, 32, 34, 38, 40, 42, 44, 45]
x: 42
result: 5
```

### Test

```sh
$ make test
python -m unittest algorithms_tests.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.001s

OK
```