"""Validate a repository-analysis request."""
from pathlib import Path

def validate(arguments: dict) -> None:
    if not isinstance(arguments, dict): raise TypeError("arguments must be an object")
    path=arguments.get("path")
    if not isinstance(path, str) or not path.strip(): raise ValueError("path is required")
    target=Path(path).expanduser().resolve()
    if not target.exists(): raise ValueError("path does not exist")
    if not target.is_dir(): raise ValueError("path must be a directory")

def execute(arguments: dict) -> dict:
    validate(arguments)
    target=Path(arguments["path"]).expanduser().resolve()
    return {"path": str(target), "valid": True}
