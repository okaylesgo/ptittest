import pytest
import MAMAMIA

def test_DIV():
    with pytest.raises(ZeroDivisionError):
        MAMAMIA.DIV(1,0)
    

def test_fact():
    with pytest.raises(ValueError):
        MAMAMIA.fact(-50)

def test_integrate():
    # À compléter...
    pass
