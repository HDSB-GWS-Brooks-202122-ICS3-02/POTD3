'''
CodingBat Python Activity "centered_average" from list-2.
codingbat.com
'''

failures = 0

def centered_average(nums):
    '''
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value, ignore just one copy,
and likewise for the largest value. Use int division to produce the final average.
You may assume that the array is length 3 or more.
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''

    nums.sort()
    del nums[0]
    del nums[-1]
    average = 0
    for i in range (len(nums)):
        average += nums[i]
    return round(average/len(nums))





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('centered_average([1, 2, 3, 4, 100])', 3)
    catchFailures('centered_average([1, 1, 5, 5, 10, 8, 7])', 5)
    catchFailures('centered_average([-10, -4, -2, -4, -2, 0])', -3)
    catchFailures('centered_average([5, 3, 4, 6, 2])', 4)
    catchFailures('centered_average([5, 3, 4, 0, 100])', 4)
    catchFailures('centered_average([100, 0, 5, 3, 4])', 4)
    catchFailures('centered_average([4, 0, 100])', 4)
    catchFailures('centered_average([0, 2, 3, 4, 100])', 3)
    catchFailures('centered_average([1, 1, 100])', 1)
    catchFailures('centered_average([7, 7, 7])', 7)
    catchFailures('centered_average([1, 7, 8])', 7)
    catchFailures('centered_average([1, 1, 99, 99])', 50)
    catchFailures('centered_average([1000, 0, 1, 99])', 50)
    catchFailures('centered_average([4, 4, 4, 4, 5])', 4)
    catchFailures('centered_average([4, 4, 4, 1, 5])', 4)
    catchFailures('centered_average([6, 4, 8, 12, 3])', 6)
    
    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()