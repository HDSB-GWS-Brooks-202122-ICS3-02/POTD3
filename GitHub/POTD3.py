'''
CodingBat Python Activity "sum_double" from warmup-1.
codingbat.com
'''

failures = 0

def sum_double(a, b):
    '''
Given two int values, return their sum. Unless the two values are the same,
then return double their sum.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
    if a == b:
        return (a * 4)
    else:
        return (a + b)





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('sum_double(1, 2)', 3)
    catchFailures('sum_double(3, 2)', 5)
    catchFailures('sum_double(2, 2)', 8)
    catchFailures('sum_double(-1, 0)', -1)
    catchFailures('sum_double(3, 3)', 12)
    catchFailures('sum_double(0, 0)', 0)
    catchFailures('sum_double(0, 1)', 1)
    catchFailures('sum_double(3, 4)', 7)

    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()