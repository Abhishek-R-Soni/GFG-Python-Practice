
# input  : 1,2,3,4,5,6,7
# output : 7,5,3,1,2,4,6

data = [11,12,31,14,5]
data.sort()
temp = []
i = len(data) - 1

while i >= 0:
    temp.append(data[i])
    i -= 2

i = 1
while i < len(data):
    temp.append(data[i])    
    i += 2

print(temp)