from basics._06_functions.functions import add, apply_twice

def test_add():
    assert add(2, 3) == 5

def test_apply_twice():
    assert apply_twice(lambda x: x + 1, 10) == 12
