
slash = 'Dash Slash'

#startswith and endswith this checks the string for begins with some word and end with another wordd
print(slash.startswith('Dash'))
print(slash.endswith('slash'))

#join and split

#join adds anything you want between every single character in list
sampleJoin = ' ;'.join(['c', 'c++', 'python', 'java', 'javascript'])
print(sampleJoin)

#split function see the string and eliminate the script according to given script
# for example 
sampleSplit = 'I have never seen the language even close to C . Linus Torvalds'.split('a')
print(sampleSplit)

#partition is similar with split but unlike split it does not elimate items
#for example:
samplePartition = 'I am not the person like you'.partition('a')
print(samplePartition)