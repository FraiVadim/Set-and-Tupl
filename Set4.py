A={1,2,3,'A','B','C'}
print({1,2,3,'A','B','C'})
print({})
temp=list(A)
for i in temp[1:5]:
    print({1,i})
for i in temp[2:5]:
    print({1,2,i})
print()
