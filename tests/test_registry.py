import pytest
from core.agent_core import ToolRegistry
from contracts.tool_contract import ToolContract

def test_registry_dynamic():
 r=ToolRegistry(); r.register(ToolContract('a','',{},lambda x:None,lambda x:{})); assert r.discover()==['a']
 with pytest.raises(ValueError): r.register(ToolContract('a','',{},lambda x:None,lambda x:{}))
