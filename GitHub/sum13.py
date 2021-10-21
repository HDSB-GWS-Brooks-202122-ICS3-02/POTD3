'''
CodingBat Python Activity "sum13" from list-2.
codingbat.com
'''

failures = 0

def sum13(nums):
    '''
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
'''
    total = 0
    found13 = False
    for i in range (len(nums)):
        if nums[i] == 13:
            found13 = True
        else:
            if found13 == True:
                found13 = False
            else:
                total += nums[i]
    return total





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('sum13([1, 2, 2, 1])', 6)
    catchFailures('sum13([1, 1])', 2)
    catchFailures('sum13([1, 2, 2, 1, 13])', 6)
    catchFailures('sum13([1, 2, 13, 2, 1, 13])', 4)
    catchFailures('sum13([13, 1, 2, 13, 2, 1, 13])', 3)
    catchFailures('sum13([])', 0)
    catchFailures('sum13([13])', 0)
    catchFailures('sum13([13, 13])', 0)
    catchFailures('sum13([13, 0, 13])', 0)
    catchFailures('sum13([13, 1, 13])', 0)
    catchFailures('sum13([5, 7, 2])', 14)
    catchFailures('sum13([5, 13, 2])', 5)
    catchFailures('sum13([0])', 0)
    catchFailures('sum13([13, 0])', 0)

    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()