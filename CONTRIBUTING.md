# Contributing

If you would like to contribute, below you can find some helpful suggestions and instructions.

## Preparing the development environment

To install packages required for running tests and linting, run the following command:

```bash
pip install pip-tools
pip-compile --all-extras -o requirements-dev.txt pyproject.toml
pip install -r requirements-dev.txt
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

### Markdownlint

If you made changes to `.md` file and want to lint them locally, you have to install `markdownlint` using `npm`.

```bash
npm install -g markdownlint-cli2
```

Now you can lint markdown files using to automatically detect all issues and fix some:

```bash
markdownlint-cli2 --fix "**/*.md"
```

## Docs

To automatically generate the documentation from the code, run the following commands:

```bash
./docs/make.bat clean
./docs/make.bat html
```

To locally view the docs, run the following command:

```bash
python -m http.server -b localhost -d docs/_build/html 8000
```

and inspect the docs at `localhost:8000`
