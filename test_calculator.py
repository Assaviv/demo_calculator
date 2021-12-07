import main


def calculate(formula) -> str:
    return str(main.calculate(formula))


def test_addition():
    assert calculate("1+1") == "2.0"
    assert calculate("10+20") == "30.0"


def test_spaces():
    assert calculate("1 + 1 ") == "2.0"
    assert calculate("   10 + 20    ") == "30.0"

def test_bitwise_or():
    assert calculate("1|1") == "1.0"
    assert calculate("1|2") == "3.0"
    assert calculate("81|26") == "91.0"
    assert calculate("  1| 68") == "69.0"
