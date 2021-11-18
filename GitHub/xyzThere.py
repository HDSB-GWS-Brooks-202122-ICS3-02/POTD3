import re
'''
CodingBat Python Activity "xyz_there" from string-2.
codingbat.com
'''

failures = 0

def xyz_there(strIn):
    '''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
    counter = 0
    for i in range(len(strIn)-2):
        if strIn[i] == 'x' and strIn[i+1] == 'y' and strIn[i+2] == 'z' and strIn[i-1] != '.':
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
    
    catchFailures("xyz_there('abcxyz')", True)
    catchFailures("xyz_there('abc.xyz')", False)
    catchFailures("xyz_there('xyz.abc')", True)
    catchFailures("xyz_there('abcxy')", False)
    catchFailures("xyz_there('xyz')", True)
    catchFailures("xyz_there('xy')", False)
    catchFailures("xyz_there('x')", False)
    catchFailures("xyz_there('')", False)
    catchFailures("xyz_there('abc.xyzxyz')", True)
    catchFailures("xyz_there('abc.xxyz')", True)
    catchFailures("xyz_there('.xyz')", False)
    catchFailures("xyz_there('12.xyz')", False)
    catchFailures("xyz_there('12xyz')", True)
    catchFailures("xyz_there('1.xyz.xyz2.xyz')", False)

        
    if failures > 0:
        print("\r\n "+ str(failures) + " failed test case(s)   :(")
    else:
        print("Good job -- problem solved!")


test()