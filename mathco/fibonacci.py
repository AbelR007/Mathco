# Fibonacci Command Module

class Fibonacci:
    def __init__(self):
        pass

    def series(self, number):
        a = 1
        b = 1
        li = [a,b]
        for i in range(number-2):
            c = a + b
            li.append(c)
            a,b = b,c
        return li

x = Fibonacci()
x.series(5)
