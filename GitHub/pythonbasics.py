dayNum = input('''What day # is it?
: ''')

dateNum = int(dayNum)

if dateNum == 0:
    print('It is Monday')
if dateNum == 1:
    print('It is Tuesday')
if dateNum == 2:
    print('It is Wednesday')
if dateNum == 3:
    print('It is Thursday')
if dateNum == 4:
    print('It is Friday')
if dateNum == 5:
    print('It is Saturday')
if dateNum == 6:
    print('It is Sunday')
if dateNum >=7:
    print('Thats not a day lmao')