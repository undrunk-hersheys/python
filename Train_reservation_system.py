import random
def reservation(list0,ta,list1):
    print("=============================")
    print("You can select your train and seat by your own (1)")
    print("Or you may choose automatic reservation (2)")
    reservationmenu0=input("Operation?: ")
    reservationmenu=checkint(reservationmenu0)
    if reservationmenu==1:
       carnumber0=input("Select the car number(1~5): ")
       carnumber=checkint(carnumber0)
       if 1<=carnumber<=5:
           for c in range(20):
                print("  [%s%2i]%3s"%(ta[carnumber-1],c+1,list0[carnumber-1][c]),end="")
                if c%4==1:
                    print("     ",end="")
                elif c%4==3:
                    print()
           seatnumber0=input("Select the seat number(1~20): ")
           seatnumber=checkint(seatnumber0)
           if 1<=seatnumber<=20:   
               if list0[carnumber-1][seatnumber-1]=='X':
                   print("That seat is already reserved, please find other seat")
               else:
                   name=str(input("Please enter your name here: "))
                   del(list0[carnumber-1][seatnumber-1])
                   list0[carnumber-1].insert(seatnumber-1,'X')
                   del(list1[carnumber-1][seatnumber-1])
                   list1[carnumber-1].insert(seatnumber-1,[name,ta[carnumber-1],seatnumber])
           else:
               print("Wrong number")
       else:
            print("Wrong number")
    elif reservationmenu==2:
        print("Your train number and seat will be randomly chosen")
        n=0
        m=0
        booked=0
        while True:
            if list0[n][m][0]=='O':
                break
            else:
                m+=1
                if m==20:
                    n+=1
                    m=0
                    if n==5:
                        booked=1
                        break
        if booked==0:
            name=input("Please enter you name here: ")
            while True:
                tr=random.randint(0,4)
                sr=random.randint(0,19)
                if list0[tr][sr]=='O':
                    del(list0[tr][sr])
                    list0[tr].insert(sr,'X')
                    del(list1[tr][sr])
                    list1[tr].insert(sr,[name,ta[tr],sr+1])
                    print("Your seat is placed in",list1[tr][sr])
                    break
        else:
            print("Sorry, all seats are booked")
    else:
        print("You've pressed the wrong number")
    input("Press enter to continue")
def show_states(list2,ta):
    while True:
        print("=============================")
        shownumber0=input("Select the car number to show state.(1~5,0 exit,6 all): ")
        shownumber=checkint(shownumber0)
        if not 0<=shownumber<7:
            print("Wrong number")
            input("Press enter to continue")
            break
        if shownumber==0:
            break
        if shownumber==6:
            for shownumber in range(5):
                print("Train[%s]"%ta[shownumber])
                for c in range(20):
                    print("  [%s%2i]%3s"%(ta[shownumber],c+1,list2[shownumber][c]),end="")
                    if c%4==1:
                        print("     ",end="")
                    elif c%4==3:
                        print()
                print()
        else:
            print("Car%s states"%ta[shownumber-1])
            for c in range(20):
                print("  [%s%2i]%3s"%(ta[shownumber-1],c+1,list2[shownumber-1][c]),end="")
                if c%4==1:
                    print("     ",end="")
                elif c%4==3:
                    print()
def cancellation(list3,ta,list4):
    print("=============================")
    name=input("Enter your name to cancel: ")
    n=0
    m=0
    while True:
        if list4[n][m][0]==name:
            del(list3[n][m])
            list3[n].insert(m,'O')
            del(list4[n][m])
            list4[n].insert(m,'O')
            print("Cancelled successfully")
            break
        else:
            m+=1
            if m==20:
                n+=1
                m=0
                if n==5:
                    print("Not found")
                    print("Please check your reserved name again")
                    break
    input("Press enter to continue")
def record_guest(ta,list5):
    print("=============================")
    print("This contains personal information, authorized personnel only")
    password=input("Enter the password(0000): ")
    if password==pswd:
        for carnumber in range(5):
            print("Train[%s]"%ta[carnumber])
            for c in range(20):
                print("[%s%2i]%s"%(ta[carnumber],c+1,list5[carnumber][c]),end="")
                print()
            print()
    else:
        print("Wrong password")
    input("Press enter to continue")
def guest_retrieval(list6):
    print("=============================")
    name=input("Enter your name to check whether you have reserved a seat: ")
    n=0
    m=0
    while True:
        if list6[n][m][0]==name:
            print("You have reserved",list6[n][m])
            break
        else:
            m+=1
            if m==20:
                n+=1
                m=0
                if n==5:
                    print("Not found")
                    print("Please check your reserved name again")
                    break
    input("Press enter to continue")
def change_seats(list7,ta,list8):
    print("=============================")
    name=input("Enter your name: ")
    n=0
    m=0
    while True:
        if list8[n][m][0]==name:
            print("Select NEW seat for the change")
            carnumber0=input("Select the car number(1~5): ")
            carnumber=checkint(carnumber0)
            if 1<=carnumber<=5:
                for c in range(20):
                    print("  [%s%2i]%3s"%(ta[carnumber-1],c+1,list7[carnumber-1][c]),end="")
                    if c%4==1:
                        print("     ",end="")
                    elif c%4==3:
                        print()
                seatnumber0=input("Select the seat number(1~20): ")
                seatnumber=checkint(seatnumber0)
                if 1<=seatnumber<=20:   
                    if list7[carnumber-1][seatnumber-1]=='X':
                        print("That seat is already reserved, please find other seat")
                    else:
                        del(list7[carnumber-1][seatnumber-1])
                        list7[carnumber-1].insert(seatnumber-1,'X')
                        del(list8[carnumber-1][seatnumber-1])
                        list8[carnumber-1].insert(seatnumber-1,[name,ta[carnumber-1],seatnumber])
                        del(list7[n][m])
                        list7[n].insert(m,'O')
                        del(list8[n][m])
                        list8[n].insert(m,'O')
                        print("Changed successfully")
                else:
                    print("Wrong number")
            else:
                print("Wrong number")
            break
        else:
            m+=1
            if m==20:
                n+=1
                m=0
                if n==5:
                    print("Not found")
                    print("Please check your reserved name again")
                    break
    input("Press enter to continue")
def group_reservation(list9,ta,list10):
    print("=============================")
    print("For group reservation, only consecutive seats can be reserved")
    print("We don't provide this service group over 20")
    n=0
    m=0
    group0=input("Enter the number of your group: ")
    group=checkint(group0)
    if group<=1:
        print("Sorry, we don't provide this service for the individuals")
        print("Please use New reservation service")
    elif 1<group<=100:
        temp0=[]
        temp1=[]
        o=0
        p=0
        while True:
            if list9[n][m]=='O':
                o+=1
                p+=1
                if p>=group:
                    temp1.append([ta[n],m+2-group])
                m+=1
            else:
                m+=1
                p=0
            if m==20:
                p=0
                if o>=group:
                    temp0.append(ta[n])
                o=0
                n+=1
                m=0
                if n==5:
                    break   
        if temp0==[]:
            print("Currently all of your group can't stay in one car")
            print("Please use individual reservation in the menu")
        else:
            print("All member of your group can stay in car",temp0)
            print("You can make reservation on consecutive seats on")
            for q in range(len(temp1)):
                print(temp1[q][0],temp1[q][1],"~",temp1[q][1]+group-1)
                
            carnumber0=input("Select the car number(1~5): ")
            carnumber=checkint(carnumber0)
            k=0
            if 1<=carnumber<=5:
                seatnumber0=input("Select the seat number(start number of the consecutive seats from above)(1~20): ")
                seatnumber=checkint(seatnumber0)
                if 1<=seatnumber<=20:
                    for q in range(len(temp1)):
                        if temp1[q][0]==ta[carnumber-1] and temp1[q][1]==seatnumber:
                            for r in range(group):
                                name=str(input("Please enter your name here: "))
                                del(list9[carnumber-1][seatnumber-1+r])
                                list9[carnumber-1].insert(seatnumber-1+r,'X')
                                del(list10[carnumber-1][seatnumber-1+r])
                                list10[carnumber-1].insert(seatnumber-1+r,[name,ta[carnumber-1],seatnumber+r])
                            k+=1
                    if k==0:
                        print("You must select from the consecutive seats")
                else:
                    print("Wrong number")
            else:
                print("Wrong number")
    else:
        print("Wrong input or number")
        print("Please try it again")
    input("Press enter to continue")
def checkint(string):
    if string=='':
        string='TAE'
    templist=[]
    for z in string:
        templist.append(z)
    for zz in range(len(string)):
        if not '0'<=templist[zz]<='9':
            zzz=int(9999)
            return zzz
    zzz=int(string)
    return zzz

car1=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
car2=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
car3=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
car4=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
car5=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
train=[car1,car2,car3,car4,car5]
trainalpha=['A','B','C','D','E']
carA=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
carB=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
carC=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
carD=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
carE=['O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O','O']
record=[carA,carB,carC,carD,carE]
pswd='0000'

while True:
    print()
    print("Select operation")
    print("=============================")
    print("New reservation (1)")
    print("Reservation states display (2)")
    print("Cancellation (3)")
    print("Guest retrieval (4)")
    print("Change seats (5)")
    print("Group reservation (6)")
    print("All seats and names for staff (7)")
    print("Exit (0)")
    menu0=input("Operation?: ")
    menu=checkint(menu0)
    if menu==1:
        reservation(train,trainalpha,record)
    elif menu==2:
        show_states(train,trainalpha)
    elif menu==3:
        cancellation(train,trainalpha,record)
    elif menu==4:
        guest_retrieval(record)
    elif menu==5:
        change_seats(train,trainalpha,record)
    elif menu==6:
        group_reservation(train,trainalpha,record)
    elif menu==7:
        record_guest(trainalpha,record)
    elif menu==0:
        break
    else:
        print("You've pressed wrong number")
    
print("Thank you for your use.")
