import logging
import os
import subprocess
from importlib.metadata import PackageNotFoundError, version

SURICATA_CHECK_DIR = os.path.dirname(__file__)

_logger = logging.getLogger(__name__)


def __get_git_revision_short_hash() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .decode("ascii")
        .strip()
    )


def get_version() -> str:
    v = "unknown"

    git_dir = os.path.join(SURICATA_CHECK_DIR, "..", ".git")
    if os.path.exists(git_dir):
        v = __get_git_revision_short_hash()
        _logger.debug(
            "Detected suricata-check-extension-example version using git: %s", v
        )
    else:
        try:
            v = version("suricata-check-extension-example")
            _logger.debug(
                "Detected suricata-check-extension-example version using importlib: %s",
                v,
            )
        except PackageNotFoundError:
            _logger.debug(
                "Failed to detect suricata-check-extension-example version: %s", v
            )

    return v


__version__: str = get_version()
