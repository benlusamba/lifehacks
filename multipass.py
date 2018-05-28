#Multiple passwords:
import random
import prettytable

inp = input('How many characters?: ')
iterations = input('How many passwords: ')
len = int(inp)
iter = int(iterations)

for i in range (iter):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s,len))
    print (p)


#Write results as csv or txt
result = str(p)
output = open('passwords' + '.csv','w')
output.write('%s' % result)
output.close()
