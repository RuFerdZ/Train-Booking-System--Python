
#cost calculating algorithm
def costCalculation(currentbalance,name,passengerID):
    global state
    print("Welcome",name)
    print("Your current account balance is : $",currentbalance) #displays current balancein account
    print("-----------------------------------------")
    state=True
    try:
        ticketCost=destination(currentbalance)
        accountbalance=currentbalance-ticketCost
        print("cost of ticket : $",ticketCost)
        print("your remaining account balance is : $",accountbalance)  #displays account balance after charged
        
        print("-----------------------------------------")
        if accountbalance<=500:                                  #if your account balance is lower than or equal 500,it ill alert you to recharge                
            print("****Your account balance is running low****")
            print("****Please reacharge as soon as possible****")
            print("-----------------------------------------")
        print("you will receive the digital ticket to your mobile phone.......")
        print("         !!! Thank you for travelling !!!")        
    except:
        print("cost of ticket : $",ticketCost)
        print("Not enough money on your account please recharge !!!")
        state=False
        
        



# cost differ from destination to destination
#it is also saved in a seperate destination database

def destination(currentbalance):
    locationdic={1:"colombo",2:"negombo",3:"kandy",4:"Jaffna"}
    print("locations")
    print("-------------")
    print("1:colombo")
    print("2:negombo")
    print("3:kandy")
    print("4:jaffna")
    print("-------------")
    loc=int(input("Enter location number : "))
    print("-----------------------------------------")
    while ((loc>len(locationdic)) or(loc<=0)):
        print("invalid location please re-enter")
        loc=int(input("Enter location number : "))
        print("-----------------------------------------")
    cost=100
    for i in locationdic:
        cost+=100
        if loc==i:
            print("your location is:",locationdic[i])
            if cost>currentbalance:
                break
            else:
                return cost
                break

#it reads the user ID from the passengers smart card and load the information of the passenger from the database 
#user DB
def userDB(passengerID):
    print("-----------------------------------------")
    userfile=open("userdata.txt","r")
    namepos=0
    balancepos=0
    name=''
    balance=0
    while True:    
        userdata=userfile.readline()
        if passengerID==userdata[0:4]:
            #print(userdata)
            namepos=userdata.index("/")+1
            balancepos=userdata.index(",")
            name=userdata[namepos:balancepos]
            balance=int(userdata[balancepos+1:])
            #print(name)
            #print(balance)
            costCalculation(balance,name,passengerID)
            break
    

#main program
#also checks for number of seats available in a train
#in this case we consider only that 100 passengers can fit in one train
emptySeats=100
while (emptySeats >0):    
    print("-----------------------------------------")
    print("       Welcome to the Railway Systems")
    print("-----------------------------------------")
    print(emptySeats,"seats available")
    print("-----------------------------------------")
    passengerID=input("Swipe your ID : ")
    if passengerID=="q":
        break
    userDB(passengerID)
    cardstate=True   #making the ticket active until destination is reached
    print("============================================================")
    if state==False:
        continue
    else:
        emptySeats-=1
    
else:
    print("-----------------------------------------")
    print("No seats availale")
    print('=========================================')

#as the passenger swipes the card he will be directed to a screen which has his details
#it will be a touchscreen display
#passenger has to tap the destination he wants to travel
#The cost will be calculated and displayed
#he will receive a digital ticket to his phone
#ticket expires as soon as he swipes the card on the end station
    


#end station procedure
