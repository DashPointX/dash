import random
#THere are three stripping types out there
#First - ...strip
# dash = 'AAAfkjhdfhAAA'
# print(dash.strip('AAA'))
#THis type of strip just cut the spaces tabs

# the second type of strip is rstrip
# print(dash.rstrip('AAA'))
#this type of string cut right side of string

#the third type of strip is... lstrip
#print(dash.lstrip('AAA'))
#this type of string exact opposit of rstrip

#this is mini program for practice strips
# >
while True:
    randomA = random.randint(1, 5)
    wa = ''
    if randomA == 1:
        wa  = wa + 'A'
    elif randomA == 2:
        wa = wa + 'B'
    elif randomA == 3:
        wa = wa + 'C'
    elif randomA == 4:
        wa = wa + 'D'
    elif randomA == 5:
        wa = wa + 'E'

    randomB = random.randint(1, 5)
    wb = ''
    if randomB == 1:
        wb  = wb + 'A'
    elif randomB == 2:
        wb = wb + 'B'
    elif randomB == 3:
        wb = wb + 'C'
    elif randomB == 4:
        wb = wb + 'D'
    elif randomB == 5:
        wb = wb + 'E'
    randomC = random.randint(1, 5)
    wc = ''
    if randomC == 1:
        wc  = wc + 'A'
    elif randomC == 2:
        wc = wc + 'B'
    elif randomC == 3:
        wc = wc + 'C'
    elif randomC == 4:
        wc = wc + 'D'
    elif randomC == 5:
        wc = wc + 'E'

    randomD = random.randint(1, 5)
    wd = '' 
    if randomD == 1:
        wd  = wd + 'A'
    elif randomD == 2:
        wd = wd + 'B'
    elif randomD == 3:
        wd = wd + 'C'
    elif randomD == 4:
        wd = wd + 'D'
    elif randomD == 5:
        wd = wd + 'E'

    randomE = random.randint(1, 5)
    we = ''
    if randomE == 1:
        we  = we + 'A'
    elif randomE == 2:
        we = we + 'B'
    elif randomE == 3:
        we = we + 'C'
    elif randomE == 4:
        we = we + 'D'
    elif randomE == 5:
        we = we + 'E'

    totalWorld = wa + wb + wc + wd + we
    randomSide = random.randint(0, 1)
    if randomSide == 0:
        leftSide = totalWorld.ljust(10, '.')
        print(leftSide)
        print('Cut the side\nr - right, l - left\nq - quit')
        rightChoice = input('')
        if rightChoice == 'r':
            print('<<<RIGHT!>>>')
        elif rightChoice == 'q':
            break
        else:
            print('<<<WRONG!>>>')

    elif randomSide == 1:
        rightSide = totalWorld.rjust(10, '.')
        print(rightSide)
        print('Cut the side\nr - right, l - left\nq - quit')
        leftChoice = input('')
        if leftChoice == 'l':
            print('<<<RIGHT!>>>')
        elif leftChoice == 'q':
            break
        else:
            print('<<<WRONG!>>>')
