"""micrograd engine — Value class with autograd.

Fill this in as you progress through the video. Final shape:

    class Value:
        def __init__(self, data, _children=(), _op=''): ...
        def __add__(self, other): ...
        def __mul__(self, other): ...
        def tanh(self): ...
        def backward(self): ...
"""


class Value:
    def __init__(self, data, _children=(), _op="", label=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"
