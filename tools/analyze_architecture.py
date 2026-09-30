"""Deterministic repository architecture analyzer."""
from __future__ import annotations
from pathlib import Path
from collections import Counter

SKIP={'.git','.venv','venv','node_modules','__pycache__','.pytest_cache','dist','build'}
EXTENSIONS={'.py':'Python','.ts':'TypeScript','.tsx':'TypeScript React','.js':'JavaScript','.jsx':'JavaScript React','.java':'Java','.go':'Go','.rs':'Rust','.cs':'C#','.cpp':'C++','.c':'C','.sql':'SQL','.yaml':'YAML','.yml':'YAML','.json':'JSON'}

def validate(arguments):
    from .validate_architecture_input import validate as v
    v(arguments)

def execute(arguments):
    validate(arguments)
    root=Path(arguments['path']).expanduser().resolve()
    max_files=int(arguments.get('max_files',5000))
    max_bytes=int(arguments.get('max_file_bytes',500_000))
    counts=Counter(); files=[]; dirs=[]
    for p in root.rglob('*'):
        if any(part in SKIP for part in p.parts): continue
        if p.is_dir(): continue
        if len(files)>=max_files: break
        try: size=p.stat().st_size
        except OSError: continue
        if size>max_bytes: continue
        files.append(str(p.relative_to(root)))
        counts[EXTENSIONS.get(p.suffix.lower(), 'Other')]+=1
    top_dirs=Counter((Path(f).parts[0] if len(Path(f).parts)>1 else '.') for f in files)
    return {'root':str(root),'file_count':len(files),'language_counts':dict(counts),'top_level_distribution':dict(top_dirs),'files_sample':files[:100]}
