data = [55,2,778,43,13,99,77,82]
data_len = len(data)
for x in range(0, data_len-1):
    for y in range(0, data_len-1-x):
        if data[y]>data[y+1]:
            flag = data[y]
            data[y] = data[y+1]
            data[y+1] = flag        
print(data)
    
