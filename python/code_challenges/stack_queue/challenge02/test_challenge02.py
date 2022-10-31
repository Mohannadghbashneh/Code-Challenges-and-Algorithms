# Write your test here
import pytest
from challenge02 import is_Valid

def test_is_Valid():
    actual = is_Valid('()')
    expected = True
    assert actual == expected

def test_is_Valid2():
    actual = is_Valid('(){}[]')
    expected = True
    assert actual == expected

def test_is_Valid3():
    actual = is_Valid('(]')
    expected = False
    assert actual == expected

def test_is_Valid4():
    actual = is_Valid('"[(hello)()]"')
    expected = True
    assert actual == expected

def test_is_Valid5():
    actual = is_Valid('{[Hello]}')
    expected = True
    assert actual == expected

def test_is_Valid6():
    actual = is_Valid('{[Hello]')
    expected = False
    assert actual == expected