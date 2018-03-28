f1 = open('cd-w5b1.txt', 'r')
f2 = open('2b1.txt', 'r')
s3 = set(f1)
s4 = set(f2)

#將兩者集合
print ('二乙缺席名單:')

print (list(s3.symmetric_difference(s4)))