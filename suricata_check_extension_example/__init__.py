"""`suricata_check` is a module and command line utility to provide feedback on Suricata rules."""

from suricata_check_extension_example import checkers
from suricata_check_extension_example._version import (
    SURICATA_CHECK_DIR,
    __version__,
)

__all__ = (
    "SURICATA_CHECK_DIR",
    "__version__",
    "checkers",
)
