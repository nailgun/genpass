import os

def set_niceness():
    os.nice(20)

here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
