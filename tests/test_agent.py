from core.agent_core import ToolRegistry, ArchitectureAgentCore
from contracts.tool_contract import ToolContract

def test_core_execution():
 r=ToolRegistry(); r.register(ToolContract('echo','echo',{},lambda a:None,lambda a:{'x':a['x']}))
 c=ArchitectureAgentCore(r); assert c.run('echo',{'x':1})['data']['x']==1
