'''
CodingBat Python Activity "count_hi" from string-2.
codingbat.com
'''

failures = 0

def count_hi(strIn):
    '''
Return the number of times that the string "hi" appears anywhere in the given string.
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''
    hiFound = 0
    for i in range (len(strIn)-1):
        if strIn[i] == 'h' and strIn[i+1] == 'i':
            hiFound += 1
    return hiFound





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures("count_hi('abc hi ho')", 1)
    catchFailures("count_hi('ABChi hi')", 2)
    catchFailures("count_hi('hihi')", 2)
    catchFailures("count_hi('hiHIhi')", 2)
    catchFailures("count_hi('')", 0)
    catchFailures("count_hi('h')", 0)
    catchFailures("count_hi('hi')", 1)
    catchFailures("count_hi('Hi is no HI on ahI')", 0)
    catchFailures("count_hi('hiho not HOHIhi')", 2)

        
    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()