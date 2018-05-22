import random

username = input('Name: ')
print('Welcome', username)
inp = input('How many characters?: ')
try:
    len = int(inp)
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s,len))
    print (p)

except:
    print('Please enter a number')
