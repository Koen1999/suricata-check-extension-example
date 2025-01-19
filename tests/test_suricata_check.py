import logging
import os
import shutil
import sys
import tarfile
import urllib.request
import warnings

import pytest
from click.testing import CliRunner

# Ignore warnings by the main suricata-check module
warnings.filterwarnings("ignore", module="suricata_check.")

import suricata_check

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import suricata_check_extension_example

_regex_provider = suricata_check.utils.regex.get_regex_provider()

ET_OPEN_URLS = {
    "v7": "https://rules.emergingthreats.net/open/suricata-7.0.3/emerging-all.rules.tar.gz",
}


@pytest.fixture(autouse=True)
def __run_around_tests():
    # Clean up from previous tests.
    if os.path.exists("tests/data/out") and os.path.isdir("tests/data/out"):
        for f in os.listdir("tests/data/out"):
            os.remove(os.path.join("tests/data/out", f))

    yield

    # Optionally clean up after the test run.
    logging.shutdown()


@pytest.mark.slow()
@pytest.mark.serial()
@pytest.hookimpl(trylast=True)
@pytest.mark.parametrize(("version", "et_open_url"), ET_OPEN_URLS.items())
def test_main_cli_integration_et_open(version, et_open_url):
    os.environ["SURICATA_CHECK_FORCE_LOGGING"] = "TRUE"

    # Retrieve the latest ET Open rules if not present.
    if not os.path.exists(f"tests/data/emerging-all-{version}.rules"):
        if not os.path.exists(f"tests/data/emerging-all-{version}.rules.tar.gz"):
            urllib.request.urlretrieve(
                et_open_url,
                f"tests/data/emerging-all-{version}.rules.tar.gz",
            )

        tarfile.open(f"tests/data/emerging-all-{version}.rules.tar.gz").extract(
            "emerging-all.rules",
            "tests/data/temp",
        )
        os.remove(f"tests/data/emerging-all-{version}.rules.tar.gz")
        shutil.move(
            "tests/data/temp/emerging-all.rules",
            f"tests/data/emerging-all-{version}.rules",
        )
        shutil.rmtree("tests/data/temp")

    runner = CliRunner()
    result = runner.invoke(
        suricata_check.main,
        (
            f"--rules=tests/data/emerging-all-{version}.rules",
            "--out=tests/data/out",
            "--log-level=INFO",
        ),
        catch_exceptions=False,
    )

    __check_log_file()

    if result.exit_code != 0:
        pytest.fail(result.output)


def test_get_checkers():
    logging.basicConfig(level=logging.DEBUG)
    checkers = suricata_check.get_checkers()
    for checker in checkers:
        if (
            checker.__class__.__name__
            == suricata_check_extension_example.checkers.ExampleChecker.__name__
        ):
            return

    pytest.fail("Extension was not discovered by `suricata_check.get_checkers`.")


def test_version():
    logging.basicConfig(level=logging.DEBUG)
    if not hasattr(suricata_check, "__version__"):
        pytest.fail("suricata_check has no attribute __version__")
    from suricata_check._version import __version__

    if __version__ == "unknown":
        warnings.warn(RuntimeWarning("Version is unknown."))


def __check_log_file():
    log_file = "tests/data/out/suricata-check.log"

    if not os.path.exists(log_file):
        warnings.warn(RuntimeWarning("No log file found."))
        return

    with open(log_file) as log_fh:
        for line in log_fh.readlines():
            if _regex_provider.match(
                r".+ - .+ - (ERROR|CRITICAL) - .+(?<!Error parsing rule)",
                line,
            ):
                pytest.fail(line)


def __main__():
    pytest.main()
