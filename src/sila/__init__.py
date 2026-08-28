# Sila — Forensic evidence management.
# © 2026 Strategos Pty Ltd. All rights reserved.
# Aut Viam Inveniam Aut Faciam

try:
    from sila_sierra import *  # noqa: F401, F403
    from sila_sierra import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "sila requires sila-sierra. "
        "Install with: pip install sila-sierra"
    )
