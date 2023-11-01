from postfix import evaluate

def test_single_operand():
    assert evaluate("5")==5
def test_add():
    assert evaluate("52+")==7
def test_minus():
    assert evaluate("52-")==3
def test_minus1():
    assert evaluate("25-")==-3
def test_mul():
    assert evaluate("25*")==10
def test_div():
    assert evaluate("52/")==2
def test_exp():
    assert evaluate("542/*6+")==16
def test_alpha():
    assert not evaluate("2b+?")
