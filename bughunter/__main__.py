"""Console-script entrypoints.

`zh5` / `zh5-scan` -> engine.main   (recon/scan/chat/mcp dispatcher;
                                     install.sh symlinks engine.py as `zh5`)
`zh5-agent`        -> agent.main    (the autonomous session runner)
`bughunter`        -> legacy alias for `zh5`

Both insert this package dir on sys.path first so the package's flat internal
imports (`from brain import ...`, `from tools.scope_checker import ...`) resolve.
"""
import os
import sys

_PKG = os.path.dirname(os.path.abspath(__file__))
if _PKG not in sys.path:
    sys.path.insert(0, _PKG)


def main():
    import engine
    engine.main()


def agent_main():
    import agent
    agent.main()


if __name__ == "__main__":
    main()
