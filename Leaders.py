
leaders = [16,17,4,3,5,2]

min = 0
ans = []

i = len(leaders) - 1
while i >= 0:
    if leaders[i] > min:
        min = leaders[i]
        ans.append(min)        
        i -= 1
print(ans)