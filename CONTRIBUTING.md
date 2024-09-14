# Contributing

If you would like to contribute, below you can find some helpful suggestions and instructions.

## Preparing the development environment

To install packages required for running tests and linting, run the following command:

```bash
pip install -r requirements.txt
```

## Running tests

If you wish to run the majority of the tests whilst skipping the slow integration tests on large third-party rulesets, use the following command:

```bash
pytest
```

To run the slower integration tests at the end of your development cycle, use the following command instead:

```bash
pytest -m "slow" -k "not train"
```

## Linting

To automatically fix some linting issues and check for remaining issues, run the following commands:

```bash
black .
ruff check . --fix
pyright
```

## Docs

To automatically generate the documentation from the code, run the following commands:
```bash
./docs/make.bat clean
./docs/make.bat html
```

## Pull requests

When you create a pull request (PR), several checks are automatically run. These include some basic code style checks, as well as running all non-slow tests.