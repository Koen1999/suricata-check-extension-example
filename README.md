# The `suricata-check` project - Extension Example

[![Static Badge](https://img.shields.io/badge/docs-suricata--check-blue)](https://suricata-check.teuwen.net/checker.html#releasing-checkers-as-a-package)
[![GitHub License](https://img.shields.io/github/license/Koen1999/suricata-check-extension-example)](https://github.com/Koen1999/suricata-check-extension-example/blob/master/LICENSE)

[![Quick Test, Build, Lint](https://github.com/Koen1999/suricata-check-extension-example/actions/workflows/python-pr.yml/badge.svg?event=push)](https://github.com/Koen1999/suricata-check-extension-example/actions/workflows/python-pr.yml)
[![Extensive Test](https://github.com/Koen1999/suricata-check-extension-example/actions/workflows/python-push.yml/badge.svg)](https://github.com/Koen1999/suricata-check-extension-example/actions/workflows/python-push.yml)

[`suricata-check`](https://github.com/Koen1999/suricata-check) is a command line utility to provide feedback on [Suricata](https://github.com/OISF/suricata) rules.
The tool can detect various issues including those covering syntax validity, interpretability, rule specificity, rule coverage, and efficiency.

## How to use this template

1. Choose a name for your extension (e.g. `suricata-check-foobar`) and replace `suricata-check-extension-example` by your chosen name in all folder names, file names, and file contents. Similarly, replace `suricata_check_extension_example` by your chosen name with the dashes (`-`) substituted by underscores (`_`).
2. Rename `suricata_check_extension-example/checkers/example.py` and the class contained therein and make refactor accordingly in that file, and in `suricata_check_extension-example/checkers/init.py`.
3. Similarly, rename `tests/checkers/test_example.py` and adjust the reference to the renamed checker file/class in that file and in `tests/test_suricata_check.py`.
4. Implement tests for your checker in `tests/checkers/test_example.py` and implement the checker in `suricata_check_extension-example/checkers/example.py`.
5. You can now package, distribute and install the extension like any other Python package. When installed, the extension will be automatically selected by `suricata-check` when ran from the command line.

## Contributing

If you would like to contribute, please check out [CONTRIBUTING.md](https://github.com/Koen1999/suricata-check-extension-example/blob/master/CONTRIBUTING.md) some helpful suggestions and instructions.

## License

This project (Extension Example) is licensed under the [Apache 2.0 license](https://github.com/Koen1999/suricata-check-extension-example/blob/master/LICENSE).
