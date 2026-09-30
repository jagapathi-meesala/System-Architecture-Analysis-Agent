from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def test_manifest_minimal_shape():
 d=yaml.safe_load((ROOT/'agent.yaml').read_text())
 assert d['spec_version']=='0.1.0'; assert d['name']=='system-architecture-analysis-agent'; assert isinstance(d['skills'],list); assert isinstance(d['tools'],list)
 assert all(isinstance(x,str) for x in d['skills']+d['tools'])
 for x in d['skills']+d['tools']: assert (ROOT/x).is_file()
 assert set(d)-{'spec_version','name','version','description','skills','tools'}==set()
