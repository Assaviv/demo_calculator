import main


def calculate(formula) -> str:
    return str(main.calculate(formula))


def test_addition():
    assert calculate("1+1") == "2.0"
    assert calculate("10+20") == "30.0"


def test_spaces():
    assert calculate("1 + 1 ") == "2.0"
    assert calculate("   10 + 20    ") == "30.0"
