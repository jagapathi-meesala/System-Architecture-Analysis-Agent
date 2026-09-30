import pytest
from tools.validate_architecture_input import validate

def test_invalid_input_rejected():
 with pytest.raises(ValueError): validate({'path':'/definitely/not/a/real/path'})
 with pytest.raises(ValueError): validate({'path':__file__})
