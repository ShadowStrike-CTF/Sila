# © 2026 Strategos. All rights reserved.
# sila — stub package. Redirects to sila-sierra.
# See: https://github.com/ShadowStrike-CTF/shadowstrike-suite

try:
    from sila_sierra import *  # noqa: F401, F403
    from sila_sierra import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "sila requires sila-sierra. "
        "Install with: pip install sila-sierra"
    )
