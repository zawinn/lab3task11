from main.task11 import calculator

def test_divide():
    assert calculator(0.001).divide(1,3) == 0.333

def test_convert():
    assert calculator(0.00001).convert_precision() == 5