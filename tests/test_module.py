from src.module import foo

def test_foo():
    assert foo(1,1) == 2
    assert foo(0,0) == 0