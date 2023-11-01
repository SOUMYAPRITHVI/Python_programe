from postfix import evaluate

def test_single_operand():
    assert evaluate("5")==5

def test_add():
    assert evaluate("52+")==7