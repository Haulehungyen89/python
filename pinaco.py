a = 0
b = 1
list = [a,b]

for i in range(0,8,1):
  d = a+b
  list.append(d)
  a=b
  b=d
 
print(list)