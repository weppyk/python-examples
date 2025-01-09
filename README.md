# Python examples
This is a playground for Python code snippets and examples.
It's configured to automatically prepare environment.

## How to use
1. Clone this repository
2. install direnv https://formulae.brew.sh/formula/direnv
3. run `direnv allow .` to allow the .envrc file
4. your code should be in the `src` directory
5. your tests should be in the `tests` directory

How to add libraries
1. add library by running `poetry add <library_name>`
2. install the library by running `poetry install`

## New Example: Parsing JSON
A new example for parsing JSON has been added in the `src` directory. You can find the code in `src/parse_json_example.py`.

## New Test: Parsing JSON
A new test for parsing JSON has been added in the `tests` directory. You can find the test in `tests/test_parse_json_example.py`.

## How to execute tests
To execute the tests, run the following command:
```
make test
```
