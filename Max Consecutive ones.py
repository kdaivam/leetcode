a = [0]

max_counter, counter, prev_sum = 0, 0, 0
for i,x in enumerate(a):
    print('index: ',i)
    if x == 0:
        print('x=0')
        prev_sum, counter = counter+1, 0
        print('prev_sum---',prev_sum,'counter---',counter)
    else:
        counter += 1
    max_counter = max(max_counter,prev_sum+counter)
    print(x,'---',counter,'----',max_counter)
    
print(max_counter)
