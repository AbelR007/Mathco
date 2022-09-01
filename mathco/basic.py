# BASIC Commands Module

class Basic:
    """
    Basic Commands:
    Add - Add two numbers
    Subtract - Subtract two numbers
    Divide - Divide two numbers
    Multiply - Multiply two numbers

    Note :
    Mathco is still in development stage. This is just a simple part of it, and we are planning to do more.
    """

    def __init__(self):
        pass

    # ADD
    def add(self, a, b):
        return a + b

    # SUBTRACT
    def sub(self, a, b):
        return a - b

    # MULTIPLY
    def mul(self, a, b):
        return a * b

    # DIVIDE
    def div(self, a, b):
        if b == 0 :
            return "Not Defined"
        else :
            return a / b

# =========================================================
# CREATED with ❤️ by AbelR007
# =========================================================
