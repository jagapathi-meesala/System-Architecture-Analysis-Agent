from pathlib import Path
from tools.analyze_architecture import execute

def test_analysis(tmp_path: Path):
 (tmp_path/'main.py').write_text('print(1)')
 out=execute({'path':str(tmp_path),'max_files':10,'max_file_bytes':1000})
 assert out['file_count']==1 and out['language_counts']['Python']==1
