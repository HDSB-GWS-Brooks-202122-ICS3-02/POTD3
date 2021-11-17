'''
CodingBat Python Activity "count_code" from string-2.
codingbat.com
'''

failures = 0

def count_code(strIn):
    '''
Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
    counter = 0
    for i in range(len(strIn)-3):
        if strIn[i] == 'c' and strIn[i+1] == 'o' and strIn[i+3] == 'e':
            counter += 1
    return counter





def catchFailures(testCase, result):
    global failures
    
    try:
        assert eval(testCase) == result, "Test Case Failed: "+testCase+ " → "+str(result)
    except Exception as e:
        failures += 1
        print(e)
            


def test():
    global failures
    
    catchFailures("count_code('aaacodebbb')", 1)
    catchFailures("count_code('codexxcode')", 2)
    catchFailures("count_code('cozexxcope')", 2)
    catchFailures("count_code('cozfxxcope')", 1)
    catchFailures("count_code('xxcozeyycop')", 1)
    catchFailures("count_code('cozcop')", 0)
    catchFailures("count_code('abcxyz')", 0)
    catchFailures("count_code('code')", 1)
    catchFailures("count_code('ode')", 0)
    catchFailures("count_code('c')", 0)
    catchFailures("count_code('')", 0)
    catchFailures("count_code('AAcodeBBcoleCCccoreDD')", 3)
    catchFailures("count_code('AAcodeBBcoleCCccorfDD')", 2)
    catchFailures("count_code('coAcodeBcoleccoreDD')", 3)

        
    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()