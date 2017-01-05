from sinc2d import *

import numpy as np


def test_sinc2d_normal():
    """Testing case x, y non-zero in sinc2d()"""
    expected_value = 0.25*np.sin(2.0)*np.sin(2.0)
    calculated_value = sinc2d(2.0,2.0)
    assert expected_value == calculated_value



    
#edge case for x:
def test_edgex():
    y=1.0
    calc=sinc2d(0.0,y) 
    expc=np.sin(y) / y
    assert calc == expc
    
#edge case for y:
def test_edgey():
    x=1.0
    calc=sinc2d(x,0.0) 
    expc=np.sin(x) / x
    assert calc == expc
    
#corner case:
def test_corner():
    x,y=0.0,0.0
    calc=sinc2d(x,y) 
    expc=1
    assert calc == expc


    