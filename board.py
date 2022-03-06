def create_checkerboard(x,y):
    output = []
    for i in range(0,x):
        temp = []
        for j in range(0,y):
            temp.append((i+j) % 2)
        output.append(temp)
        
    return output
        
print(create_checkerboard(2,2))