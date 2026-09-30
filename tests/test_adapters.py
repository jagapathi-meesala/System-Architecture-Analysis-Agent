from adapters.portable_adapter import PortableAdapter

def test_adapter():
 a=PortableAdapter(lambda n,x:{'tool':n,'args':x}); assert a.invoke('x',{'a':1})['args']['a']==1
