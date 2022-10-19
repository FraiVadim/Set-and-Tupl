X={1,63,4,56,8,24} 
Y={24,86,4,9,3,45}
Z={123,34,3,2,12,3,4} 
temp=[]
for i in range(1,200):
    temp.append(i)
douasute=set(temp)
print((douasute-(X|Y|Z))==((douasute-X)&(douasute-Y)&(douasute-Z)))
