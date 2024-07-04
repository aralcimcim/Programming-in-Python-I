# K11720457
# Aral Cimcim

# Consider the following code with custom exceptions ErrorA, ErrorB and ErrorC (they are all independent, i.e., none of them is a special case of another one):

# f(5) -> h1 h2 g1 f1 f3 None
# f(-5) -> ErrorB h1 ErrorB g3 g5 g6 f1 f3 None
# f(11) -> ErrorA h1 ErrorA g2 f1 f3 None
# f(-11) -> ErrorB h1 ErrorB g3 ErrorC f3 ErrorC

class ErrorA(Exception):
    pass

class ErrorB(Exception):
    pass

class ErrorC(Exception):
    pass

def f(x: int):
    try:
        g(x)
        print("f1")
    except ErrorA:
        print("f2")
    finally:
        print("f3")

def g(x: int):
    try:
        h(x)
        print("g1")
    except ErrorA:
        print("g2")
    except ErrorB:
        print("g3")
        if x < -10:
            raise ErrorC
            print("g4")
        else:
            print("g5")
        print("g6")

def h(x: int):
    try:
        if x > 10:
            raise ErrorA
        if x < 0:
            raise ErrorB
    finally:
        print("h1")
    print("h2")

f(-5)