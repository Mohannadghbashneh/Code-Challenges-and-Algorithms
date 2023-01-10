# Write your test here
import pytest 
from challenge02 import*
def test_repition():
    input = 'ASAC is a department at LTUC. ASAC teaches programming in LTUC '
    assert first_repeated_word(input)== 'ASAC'

def test_no_repitition():
    input = 'ASAC is a department at LTUC'
    assert first_repeated_word(input)== "No Repetition"

def test2_no_repitition():
    input = 'My name is Mohannad'
    assert first_repeated_word(input)== "No Repetition"