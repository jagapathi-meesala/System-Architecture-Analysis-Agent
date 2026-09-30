"""Environment-backed runtime configuration."""
from __future__ import annotations
import os
from dataclasses import dataclass


def _required(name: str) -> str:
    value=os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable {name} is not set")
    return value.strip()

@dataclass(frozen=True)
class Settings:
    max_files: int
    max_file_bytes: int
    report_format: str

    @classmethod
    def from_env(cls) -> "Settings":
        def integer(name: str) -> int:
            raw=_required(name)
            try:
                value=int(raw)
            except ValueError as exc:
                raise RuntimeError(f"{name} must be an integer") from exc
            if value <= 0:
                raise RuntimeError(f"{name} must be greater than zero")
            return value
        fmt=_required("ARCHITECTURE_REPORT_FORMAT").lower()
        if fmt not in {"json", "markdown"}:
            raise RuntimeError("ARCHITECTURE_REPORT_FORMAT must be json or markdown")
        return cls(integer("ARCHITECTURE_MAX_FILES"), integer("ARCHITECTURE_MAX_FILE_BYTES"), fmt)
