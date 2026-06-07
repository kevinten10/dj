"""Helpers for loading local MiniMax configuration safely."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import MutableMapping


MINIMAX_API_KEY_PLACEHOLDER = "PASTE_YOUR_MINIMAX_API_KEY_HERE"
MINIMAX_ENV_RELATIVE_PATH = Path("13_tools") / "configs" / "minimax_env.ps1"
MINIMAX_ENV_NAMES = {"MINIMAX_API_KEY", "MINIMAX_API_BASE"}

_PS_ENV_ASSIGNMENT_RE = re.compile(
    r"""^\s*\$env:(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<value>.*?)\s*$"""
)


def _strip_inline_comment(value: str) -> str:
    quote: str | None = None
    escaped = False
    chars: list[str] = []

    for char in value:
        if escaped:
            chars.append(char)
            escaped = False
            continue
        if char == "`":
            escaped = True
            chars.append(char)
            continue
        if char in {"'", '"'}:
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
            chars.append(char)
            continue
        if char == "#" and quote is None:
            break
        chars.append(char)

    return "".join(chars).strip()


def _parse_power_shell_value(value: str) -> str:
    value = _strip_inline_comment(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.replace("`\"", '"').replace("`'", "'").replace("``", "`").strip()


def parse_minimax_env_file(path: Path) -> dict[str, str]:
    """Parse MiniMax variables from the local PowerShell env file."""
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = _PS_ENV_ASSIGNMENT_RE.match(line)
        if not match:
            continue
        name = match.group("name")
        if name not in MINIMAX_ENV_NAMES:
            continue
        values[name] = _parse_power_shell_value(match.group("value"))
    return values


def load_minimax_env_file(
    repo_root: Path,
    environ: MutableMapping[str, str] | None = None,
) -> dict[str, str]:
    """Load local MiniMax config into missing environment variables."""
    target_environ = os.environ if environ is None else environ
    values = parse_minimax_env_file(repo_root / MINIMAX_ENV_RELATIVE_PATH)
    loaded: dict[str, str] = {}

    for name, value in values.items():
        if not value:
            continue
        if target_environ.get(name):
            continue
        target_environ[name] = value
        loaded[name] = value

    return loaded
