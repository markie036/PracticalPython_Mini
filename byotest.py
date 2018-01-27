def number_of_evens(numbers):
    return 2 #should return 0 even numbers

#this function is expecting 2 even numbers and it has returned 0, which is
#correct as this is what our function wants us to do on line 2
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    #This message gives a more specific error message using .format

#Now we are calling in our testing function, with an array of 1-5, and we are 
#expecting to get back the number 2 (as there are 2 even numbers in the array).
#This won't work as we are returning 0 on line 2.
test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2);
#THIS TEST WORKS. Error message is Expected 2, got 0.


#TEST 2
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
test_not_equal(1,2);
#TEST 2 ends


#TEST 3
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection,item)
    
test_is_in([1,2,3,4],5)
#TEST 3 ends

"""
def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection,item)

test_not_in([1,2,3,4],3)

"""

print("All tests so far have passed");