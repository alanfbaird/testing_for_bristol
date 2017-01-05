from fib import *

def test_0():
    calculated_value = fib(0)
    expected_value = 1
    assert calculated_value == expected_value
    
def test_1():
    calculated_value = fib(1)
    expected_value = 1
    assert calculated_value == expected_value

def test_2():
    calculated_value = fib(2)
    expected_value = 1 + 1 
    assert calculated_value == expected_value
    
def test_3():
    calculated_value = fib(3)
    expected_value = 3 
    assert calculated_value == expected_value