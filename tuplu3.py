t1=(15,1.60,55,'masculin','nu')
t2=(25,1.85,85,'masculin','da')
p=0
if t1[0]<20:
    p+=1
if t2[0]<20:
    p+=1
print('persoane sub 20 sunt:',(p/2)*100,'%')
p=0
if t1[1]>1.70:
    p+=1
if t2[1]>1.70:
    p+=1
print('persoane cu înălțimea mai mare de 170 cm sunt:',(p/2)*100,'%')
p=0
n=0
if t1[0]>18:
    p+=t1[2]
    n+=1
if t2[0]>18:
    p+=t2[2]
    n+=1
masamed=p/n
print('masa medie a unei persoane de peste 18 ani:',masamed)
p=0
if t1[3]=='femenin' and t1[0]>20 and t1[4]=='nu':
    p+=1
if t2[3]=='femenin' and t2[0]>20 and t2[4]=='nu':
    p+=1
print('procentul persoanelor de sex feminin au peste 20 de ani și nu sunt căsătorite:',(p/2)*100,'%')
p=0
if 50>t1[0]>20 and t1[2]>((t1[2]+t2[2])/2):
    p+=1
if 50>t2[0]>20 and t2[2]>((t1[2]+t2[2])/2):
    p+=1
print('procentul persoanelor între 20 și 50 ani au greutatea mai mare decât greutatea medie:',(p/2)*100,'%')
