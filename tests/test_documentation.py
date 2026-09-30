from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_explainability_headings():
    t=(ROOT/'EXPLAINABILITY.md').read_text()
    for h in ['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']:
        assert t.count(h)==1
    for h in ['## Inputs\n','## Decision\n','## Limits\n']:
        assert h not in t
