"""Portable adapter registry for external framework bridges."""
from __future__ import annotations
from .portable_adapter import PortableAdapter

class AdapterRegistry:
    def __init__(self): self._adapters: dict[str, PortableAdapter]={}
    def register(self, name: str, adapter: PortableAdapter) -> None:
        if not name or not name.strip(): raise ValueError("Adapter name is required")
        if name in self._adapters: raise ValueError(f"Adapter already registered: {name}")
        self._adapters[name]=adapter
    def get(self, name: str) -> PortableAdapter:
        try: return self._adapters[name]
        except KeyError as exc: raise KeyError(f"Unknown adapter: {name}") from exc
    def names(self) -> list[str]: return sorted(self._adapters)
