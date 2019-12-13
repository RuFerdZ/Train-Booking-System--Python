
file=open('userdata.txt','r')
count=0
while True:
    if file.readline()=="":
        prevData=file.read(count-1)
        print(prevData)
        break
    count+=1
file.close()

file=open('userdata.txt','a')
for x in range(1):
    prevID=(prevData[0:4])
    print(prevID)
    #thisID=int(prevID)+1
    name=input("Enter name (Mr/Mrs/Miss): ")
    recharge=int(input("Enter recharge amount ($) : "))
    userRecord=("000"+'str(thisID)'+"/"+name+","+str(recharge))
    file.write(userRecord)
file.close()
