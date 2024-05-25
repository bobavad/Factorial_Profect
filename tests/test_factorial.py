from Project.factorial import factorial

def test_factorial_zero():
     """! 1.
    @param 0   Num 1.
    @return  1.
    """
    assert factorial(0) == 1

def test_factorial_one():
     """! 2.
    @param 1  Num 1.
    @return  1.
    """
    assert factorial(1) == 1

def test_factorial_positive():
     """! 3.
    @param 5  Num 1.
    @return  120.
    """
    assert factorial(5) == 120
    
def test_4():
     """! 4.
    @param 3   Num 1.
    @return  6.
    """
    assert factorial(3) == 6
