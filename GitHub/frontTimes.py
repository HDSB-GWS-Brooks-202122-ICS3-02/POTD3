'''
CodingBat Python Activity "front_times" from warmup-2.
codingbat.com
'''

failures = 0

def front_times(strIn, n):
    '''
Given a string and a non-negative int n,
we'll say that the front of the string is the first 3 chars,
or whatever is there if the string is less than length 3.
Return n copies of the front;
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''
    return ((strIn[:3]) * n)





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures('front_times("Chocolate", 2)', 'ChoCho')
    catchFailures('front_times("Chocolate", 3)', 'ChoChoCho')
    catchFailures('front_times("Abc", 3)', 'AbcAbcAbc')
    catchFailures('front_times("Ab", 4)', 'AbAbAbAb')
    catchFailures('front_times("A", 4)', 'AAAA')
    catchFailures('front_times("", 4)', '')
    catchFailures('front_times("Abc", 0)', '')
    
    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()