from whiteboard.whiteboard import stringComp
import pytest

@pytest.fixture
def string1():
    return "rochelle"

@pytest.fixture
def string2():
    return "eric"

def test_stringCompMC(string1, string2):
    nsc = stringComp(string1, string2)
    nscmc = nsc.missingChars()
    assert nscmc == ['o', 'h', 'l', 'l']

def test_stringCompEC(string1, string2):
    nsc = stringComp(string1, string2)
    nscec = nsc.extraChars()
    assert nscec == ['i']

def test_stringCompAOD(string1, string2):
    nsc = stringComp(string1, string2)
    nscmc = nsc.missingChars()
    nscec = nsc.extraChars()
    nscdcc = nsc.amountOfDifference()
    assert nscdcc == 5
