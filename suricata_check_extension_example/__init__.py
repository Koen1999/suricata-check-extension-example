"""`suricata_check` is a module and command line utility to provide feedback on Suricata rules."""

from suricata_check_extension_example import checkers
from suricata_check_extension_example._version import (
    __version__,
)

__all__ = (
    "__version__",
    "checkers",
)
