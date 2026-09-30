from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['agent.yaml','SOUL.md','README.md','AGENTS.md','DUTIES.md','RULES.md','EXPLAINABILITY.md','.env.example','.gitignore','requirements.txt','pytest.ini']
DIRS=['adapters','config','contracts','core','skills','tools','tests','verification']

def audit(root=ROOT):
    results=[]; ok=True
    for f in REQUIRED:
        present=(root/f).is_file(); results.append((f,present)); ok &= present
    for d in DIRS:
        present=(root/d).is_dir(); results.append((d+'/',present)); ok &= present
    text=(root/'EXPLAINABILITY.md').read_text(encoding='utf-8') if (root/'EXPLAINABILITY.md').exists() else ''
    headings=['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']
    for h in headings:
        present=text.count(h)==1; results.append((h,present)); ok &= present
    for bad in ['## Inputs\n','## Decision\n','## Limits\n']:
        absent=bad not in text; results.append(('no '+bad.strip(),absent)); ok &= absent
    for h in headings:
        start=text.index(h)+len(h)
        next_positions=[text.find('\n## ',start), text.find('\n# ',start)]
        ends=[p for p in next_positions if p != -1]
        sec=text[start:min(ends) if ends else len(text)]
        enough=len(re.findall(r'(?<=[.!?])\s+',sec))>=2
        results.append((h+' has two sentences',enough)); ok &= enough
    return ok, results

if __name__=='__main__':
    ok, results=audit()
    for name,state in results: print(('PASS' if state else 'FAIL')+' '+name)
    raise SystemExit(0 if ok else 1)
