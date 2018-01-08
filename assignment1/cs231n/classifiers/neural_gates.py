from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from past.builtins import xrange

class UnimplementedException(Exception):
    pass

class ComputationalGraphGate(object):
    """
    A computational graph operator gate. In the forward process, it computes the
    output of X OP Y where OP is a specific operator such as addition or 
    multiplication. In the backward process, it computes the paritial gradient 
    using chain rule.
    """
    def forward(self, X, Y):
        raise UnimplementedException("Not implemented")
    
    def backward(self, DZ):
        raise UnimplementedException("Not implemented")