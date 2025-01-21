"""`ExampleChecker`."""

import logging

import idstools.rule
from suricata_check.checkers.interface import CheckerInterface
from suricata_check.utils import checker
from suricata_check.utils.checker_typing import ISSUES_TYPE, Issue


class ExampleChecker(CheckerInterface):
    """The `ExampleChecker` contains several arbitrary checks to showcase how one may extend `suricata-check`.

    Codes E000-E009 report on bogus issues.
    """

    codes = {
        "E000": {"severity": logging.INFO},
        "E001": {"severity": logging.INFO},
    }

    def _check_rule(
        self: "ExampleChecker",
        rule: idstools.rule.Rule,
    ) -> ISSUES_TYPE:
        issues: ISSUES_TYPE = []

        if checker.is_rule_option_set(rule, "msg"):
            issues.append(
                Issue(
                    code="E000",
                    message="This rule sets the `msg` field!",
                )
            )

        if checker.is_rule_option_equal_to(rule, "sid", "1234"):
            issues.append(
                Issue(
                    code="E001",
                    message="This rule has sid `1234`, which seems temporary.\nDo not forget to change it to an actual sid!",
                )
            )

        return issues
