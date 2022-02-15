import pytest
import MAMAMIA

def test_DIV():
    with pytest.raises(ZeroDivisionError):
        MAMAMIA.DIV(1,0)
    
    

def test_fact():
    with pytest.raises(ValueError):
        MAMAMIA.fact(-50)
    assert MAMAMIA.fact(7)==5040
def test_roots():
    assert MAMAMIA.roots(2,1,-1)==(-1,1/2)

def test_integrate(): 
    pass
