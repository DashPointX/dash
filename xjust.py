right = 'this is right'.rjust(20, '>')
left = 'this is left'.ljust(20, '<')

center = 'ThisIsCenter'.center(20, '*')

print(right)
print(left)
print(center)

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():  
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4,'apples': 12,'cups': 4,'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6) 