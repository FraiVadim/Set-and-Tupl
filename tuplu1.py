elev1=("Vadim","Frai","masculin",10,10,10)
elev2=("Tolic","Ursachi","masculin",8,7,8)
elev3=("Andrei","Malanciuc","masculin",5,4,5)
elev4=("Ana","Bitco","femenin",10,8,6)
elev5=("Ira","Paduraru","femenin",8,9,9)
media1=sum(elev1[3:])/3
media2=sum(elev2[3:])/3
media3=sum(elev3[3:])/3
media4=sum(elev4[3:])/3
media5=sum(elev5[3:])/3
medii=[media1,media2,media3,media4,media5]
for i in medii:
    print('Media elevului',medii.index(i)+1,'este:',i)
    if i<5:
        print("Elevul",medii.index(i)+1,"este restanțier")
if media1>=9 and elev1[3]>=9 and elev1[4]>=9 and elev1[5]>=9:
    print('Elevul',elev1[0],elev1[1],'este eminent')
if media2>=9 and elev2[3]>=9 and elev2[4]>=9 and elev2[5]>=9:
    print('Elevul',elev2[0],elev2[1],'este eminent')
if media3>=9 and elev3[3]>=9 and elev3[4]>=9 and elev3[5]>=9:
    print('Elevul',elev3[0],elev3[1],'este eminent')
if media4>=9 and elev4[3]>=9 and elev4[4]>=9 and elev4[5]>=9:
    print('Elevul',elev4[0],elev4[1],'este eminent')
if media5>=9 and elev5[3]>=9 and elev5[4]>=9 and elev5[5]>=9:
    print('Elevul',elev5[0],elev5[1],'este eminent')