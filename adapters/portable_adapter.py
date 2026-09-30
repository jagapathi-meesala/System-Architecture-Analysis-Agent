"""Framework-neutral adapter boundary.

The adapter exposes plain Python operations so an external runtime can map its
own tool-calling mechanism to this agent without coupling core logic to a
specific SDK.
"""
from __future__ import annotations
from typing import Any, Callable

class PortableAdapter:
    def __init__(self, executor: Callable[[str, dict[str, Any]], dict[str, Any]]):
        self._executor=executor

    def invoke(self, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(tool_name, str) or not tool_name.strip():
            raise ValueError("tool_name must be a non-empty string")
        if not isinstance(arguments, dict):
            raise TypeError("arguments must be an object")
        return self._executor(tool_name, arguments)
