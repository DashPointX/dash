
# islower - this method check the strings for lower if it is lower it releases true unless not it releases false
dash3 = "Hello, motherfucker!"
if dash3.islower() == True:
    print('THis is True')
else:
    print('THis is false')

#isupper - this method exact opposite of islower
dash4 = ("Hello, motherfucker!")
if dash4.isupper() == True:
    print('It is true')
else:
    print('FALSE!')

dash = 'Dash'

#isalpha - this checks for True and False another words this returns True if value only consist of strings and not blanks
# strings = True
print(dash.isalpha())

#isalnum - this kinda similar with isalpha it is more expanded it returns true for string and also number but not blanks
#strings and number = True
print(dash.isalnum())

#isdecimal - this checks for only numbers and returns True if only numbers(only numeric characters)
#numbers = True
print(dash.isdecimal())

#isspace - this checks for only space, but not blanks, tabs and new lines
# empty = True 
print(dash.isspace())

#istitle - this is not similar with others this checks for words begins with uppecase followed by lowercase letters == True
#Something = True
print(dash.istitle())