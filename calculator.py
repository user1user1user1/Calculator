print ('Welcome in calculator in Python')
q1 = int (input('Enter number 1: '))
q2 = int (input('Enter number 2: '))

v = int (input('Wnen operation you want complete? \n 1 + \n 2 - \n 3 / \n 4 * \n'))

if v == 1:
    r = q1 + q2
    p = '+'
    t = p
if v == 2:
    r = q1 - q2
    l = '-'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = '/'
    t = m
if v == 4:
    r = q1 * q2
    n = '*'
    t = n
print (r)