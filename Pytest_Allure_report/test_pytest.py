# content of test_sample.py
import pytest
def test_add():
    assert 1+1!=2


@pytest.mark.smoke
def test_subtraction():
    assert 5-5==0

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5