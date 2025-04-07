from lab4 import lab4_

def test_lab4():
    assert lab4_(3, 4) == 12  # Example test
    assert lab4_(5, 0) == 0   # Testing with zero
    assert lab4_(-1, 10) == -10  # Testing with a negative number