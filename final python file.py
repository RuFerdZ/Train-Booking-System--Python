# 5 sample passengers ID cards
# 5 sample records from userDB
def user1():
    print("Welcome Miss.Hasani Dilhari")
    currentbalance=600
    costCalculation(currentbalance)
        
    
def user2():
    print("Welcome Mr.Janindu Alwis")
    currentbalance=4562
    costCalculation(currentbalance)
    
    
def user3():
    print("Welcome Miss.Thamadie Goonawardhana")
    currentbalance=21
    costCalculation(currentbalance)
  

def user4():
    print("Welcome Miss.Sayagi Asogan")
    currentbalance=2127
    costCalculation(currentbalance)
    

def user5():
    print("Welcome Mr.Rusiru Fernando")
    currentbalance=2100
    costCalculation(currentbalance)
        
    
#cost calculating algorithm
def costCalculation(currentbalance):
    print("Your current account balance is : $",currentbalance) #displays current balancein account
    print("-----------------------------------------")
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
def userDB():
    passengerID=input("Swipe your ID : ")
    print("-----------------------------------------")

    if passengerID=="0001":
        user1()
    elif passengerID=="0002":
        user2()
    elif passengerID=="0003":
        user3()
    elif passengerID=="0004":
        user4()
    elif passengerID=="0005":
        user5()
    


#main program
#also checks for number of seats available in a train
#in this case we consider only that 100 passengers can fit in one train
for emptySeats in range(100):    
    print("-----------------------------------------")
    print("       Welcome to the Railway Systems")
    print("-----------------------------------------")
    userDB()
    cardstate=True   #making the ticket active until destination is reached
    print("============================================================")
    
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
