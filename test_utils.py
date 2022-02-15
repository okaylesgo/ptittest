import pytest
import MAMAMIA

def test_DIV():
    with pytest.raises(ZeroDivisionError):
        MAMAMIA.DIV(1,0)
    
    

def test_fact():
    with pytest.raises(ValueError):
        MAMAMIA.fact(-50)
    assert MAMAMIA.fact(7)==5040
import math
def test_roots():
    assert MAMAMIA.roots(2,1,-1)==(-1,1/2)
    assert MAMAMIA.roots(1/4,1,1)==(-2)
    assert MAMAMIA.roots(10,1,10)==tuple()
    x1,x2= MAMAMIA.roots(1,0,-2)
    assert math.isclose(x1,-math.sqrt(2),rel_tol=1e-9)
    assert math.isclose(x2,math.sqrt(2),rel_tol=1e-9)
def test_integrate(): 
    assert MAMAMIA.integr("x+1",2,3)==3.5
