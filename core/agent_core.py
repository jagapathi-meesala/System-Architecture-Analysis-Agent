"""Dynamic tool registry and execution core."""
from __future__ import annotations
from contracts.tool_contract import ToolContract

class ToolRegistry:
    def __init__(self): self._tools: dict[str, ToolContract]={}
    def register(self, tool: ToolContract) -> None:
        if tool.name in self._tools: raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name]=tool
    def discover(self) -> list[str]: return sorted(self._tools)
    def get(self, name: str) -> ToolContract:
        if name not in self._tools: raise KeyError(f"Unknown tool: {name}")
        return self._tools[name]
    def execute(self, name: str, arguments: dict) -> dict:
        result=self.get(name).execute(arguments)
        if result.ok: return {"ok": True, "tool": name, "data": result.data}
        return {"ok": False, "tool": name, "error": result.error}

class ArchitectureAgentCore:
    def __init__(self, registry: ToolRegistry): self.registry=registry
    def list_tools(self) -> list[str]: return self.registry.discover()
    def run(self, tool: str, arguments: dict) -> dict: return self.registry.execute(tool, arguments)
