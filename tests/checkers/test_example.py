import logging
import os
import sys

import idstools.rule
import pytest
from suricata_check.tests import GenericChecker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import suricata_check_extension_example


class TestExample(GenericChecker):
    @pytest.fixture(autouse=True)
    def __run_around_tests(self):
        logging.basicConfig(level=logging.DEBUG)
        self.checker = suricata_check_extension_example.checkers.ExampleChecker()

    def test_e000_bad(self):
        rule = idstools.rule.parse(
            """alert ip any any -> any any (msg:"Test"; sid:1;)""",
        )

        self._test_issue(rule, "E000", True)

    def test_e000_good(self):
        rule = idstools.rule.parse(
            """alert ip any any -> any any (sid:1;)""",
        )

        self._test_issue(rule, "E000", False)

    def test_e001_bad(self):
        rule = idstools.rule.parse(
            """alert ip any any -> any any (msg:"Test"; sid:1234;)""",
        )

        self._test_issue(rule, "E001", True)

    def test_e001_good(self):
        rule = idstools.rule.parse(
            """alert ip any any -> any any (msg:"Test"; sid:20101234;)""",
        )

        self._test_issue(rule, "E001", False)


def __main__():
    pytest.main()
