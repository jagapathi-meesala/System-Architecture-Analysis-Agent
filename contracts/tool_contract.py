"""Framework-independent tool contract."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: dict[str, Any] | None = None
    error: str | None = None

@dataclass(frozen=True)
class ToolContract:
    name: str
    description: str
    input_schema: dict[str, Any]
    validator: Callable[[dict[str, Any]], None]
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, arguments: dict[str, Any]) -> None:
        if not isinstance(arguments, dict): raise TypeError("Tool arguments must be an object")
        self.validator(arguments)

    def execute(self, arguments: dict[str, Any]) -> ToolResult:
        try:
            self.validate(arguments)
            return ToolResult(True, self.executor(arguments), None)
        except (ValueError, TypeError, OSError) as exc:
            return ToolResult(False, None, str(exc))
