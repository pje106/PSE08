import pytest
from kth_Missing import kth_missing_positive_number

def test_kth_missing_positive_number(numbers, k):
    
    #arrange #act
    result = kth_missing_positive_number([2,3,4,7,11],5)
    
    #assert
    assert result == 9