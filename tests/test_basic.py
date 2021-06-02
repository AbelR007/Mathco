from mathco import Basic

# Creating Instances
x = Basic()

# Testing Modules
def test_add_check():
    assert x.add(1,2) == 3

def test_subtract_check():
    assert x.subtract(1,2) == -1

def test_multiply_check():
    assert x.multiply(1,2) == 2

def test_divide_check():
    assert x.divide(1,2) == 0.5
