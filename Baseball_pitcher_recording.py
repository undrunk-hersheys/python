import pickle
def Display_all(pitcherlist,rankinglist):
    rankinglist.sort()
    for q in rankinglist:
        for qq in pitcherlist:
            if qq.name==q[1]:
                print(qq)
def Display_team(teamdic,pitcherlist,rankinglist):
    print("NCD,KTW,DSB,LGT")
    team=input("Select team for the display: ")
    while team!="NCD" and team!="KTW" and team!="DSB" and team!="LGT":
        team=input("Wrong input: ")
    for ww in pitcherlist:
        for www in teamdic[team]:
            if ww.name==www:
                print(ww)
def Display_pitcher(pitcherlist):
    name=input("Enter name for display: ")
    for r in pitcherlist:
        if r.name==name:
            print(r)
def Modify_record(pitcherlist,ERAranking0):
    name=input("Enter name for modification: ")
    uu=0
    for u in pitcherlist:
        if u.name==name:
            uu+=1
            win0=input("total win?: ")
            u.win=Checkint(win0)
            loss0=input("total loss?: ")
            u.loss=Checkint(loss0)
            strikeout0=input("total strikeout?: ")
            u.strikeout=Checkint(strikeout0)
            baseonball0=input("total baseonball?: ")
            u.baseonball=Checkint(baseonball0)
            inning0=input("total inning?: ")
            while inning0=='0':
                inning0=input("total inning?: ")
            u.inning=Inningcalc(inning0)
            losspoint0=input("total losspoint?: ")
            u.losspoint=Checkint(losspoint0)
            tempERA=u.ERA
            u.ERA=u.losspoint/(int(u.inning)+u.inning%1*10*0.33333)*9
            Update_ERA_ranking(ERAranking0,tempERA,u.ERA,u.name,pitcherlist)
    if uu==0:
        print("No data")
def Save_all_records(p,t,e):
    with open("2020014348_GyuhoTAE.txt","wb") as filep:
        pickle.dump(p,filep)
        pickle.dump(t,filep)
        pickle.dump(e,filep)
    print("Data saved")
def Update_ERA_ranking(ranking,before,after,name,pitcherlist):
    ranking.remove([before,name])
    ranking.append([after,name])
    ranking.sort()
    temp_era=999
    iii=0
    for i in ranking:
        if temp_era==i[0]:
            iii+=1
        else:
            temp_era=i[0]
            iii=0
        for ii in pitcherlist:
            if ii.name==i[1]:
                ii.ERAranking=ranking.index([ii.ERA,ii.name])+1-iii
def New_pitcher(pitcherlist,teampitches,ranking):
    temp_name=input("Enter the name: ")
    print("NCD,KTW,DSB,LGT")
    temp_team=input("Enter the team name: ")
    while temp_team!="NCD" and temp_team!="KTW" and temp_team!="DSB" and temp_team!="LGT":
        temp_team=input("Wrong input: ")
    if temp_team == "NCD":
        pitcherlist.append(Pitcher(temp_name,temp_team,ranking))
        teampitches["NCD"].append(temp_name)
        Update_ERA_ranking(ranking,0,0,temp_name,pitcherlist)
    elif temp_team == "KTW":
        pitcherlist.append(Pitcher(temp_name,temp_team,ranking))
        teampitches["KTW"].append(temp_name)
        Update_ERA_ranking(ranking,0,0,temp_name,pitcherlist)
    elif temp_team == "DSB":
        pitcherlist.append(Pitcher(temp_name,temp_team,ranking))
        teampitches["DSB"].append(temp_name)
        Update_ERA_ranking(ranking,0,0,temp_name,pitcherlist)
    elif temp_team == "LGT":
        pitcherlist.append(Pitcher(temp_name,temp_team,ranking))
        teampitches["LGT"].append(temp_name)
        Update_ERA_ranking(ranking,0,0,temp_name,pitcherlist)
def Inningcalc(string):
    if string=="":
        string="TAE"
    templist=[]
    for eee in string:
        templist.append(eee)
    if '0'<=templist[0]<='9':
        e=float(string)%1*10
        ee=int(float(string))
        while e>=3:
            e-=3
            ee+=1
        return ee+e/10
    else:
        return 1
def Checkint(string):
    if string=="":
        string="TAE"
    templist=[]
    for z in string:
        templist.append(z)
    for zz in range(len(string)):
        if not '0'<=templist[zz]<='9':
            zzz=int(0)
            return zzz
    zzz=int(string)
    return zzz
class Pitcher:
    def __init__(self,name,team,ERAranking0):
        self.name=name
        self.team=team
        self.win=0
        self.loss=0
        self.strikeout=0
        self.baseonball=0
        self.inning=0
        self.losspoint=0
        self.ERA=0
        self.ERAranking=0
        ERAranking0.append([self.ERA,self.name])
    def __str__(self):
        msg="\n"
        msg+="Name: "+str(self.name)+"\n"
        msg+="Team: "+str(self.team)+"\n"
        msg+="Win: "+str(self.win)+"\n"
        msg+="Loss: "+str(self.loss)+"\n"
        msg+="Strike out: "+str(self.strikeout)+"\n"
        msg+="Base on ball: "+str(self.baseonball)+"\n"
        msg+="Inning: %.1f \n"%float(self.inning)
        msg+="Losspoint: "+str(self.losspoint)+"\n"
        msg+="ERA: %.2f \n"%float(self.ERA)
        msg+="ERA ranking: "+str(self.ERAranking)+"\n"
        return msg
    def update_stats(self,ERAranking0,pitcher):
        win0=input("win?(1/0): ")
        while win0!='0' and win0!='1':
            win0=input("win?(1/0): ")
        self.win+=Checkint(win0)
        loss0=input("loss?(1/0): ")
        while loss0!='0' and loss0!='1':
            loss0=input("loss?(1/0): ")
        self.loss+=Checkint(loss0)
        strikeout0=input("strikeout?(0~N): ")
        self.strikeout+=Checkint(strikeout0)
        baseonball0=input("baseonball?(0~N): ")
        self.baseonball+=Checkint(baseonball0)
        inning0=input("inning?(0.1,0.2,1...): ")
        while inning0=='0':
            inning0=input("inning?(0.1,0.2,1...): ")
        self.inning+=Inningcalc(inning0)
        self.inning=Inningcalc(str(self.inning))
        losspoint0=input("losspoint?(0~N): ")
        self.losspoint+=Checkint(losspoint0)
        tempERA=self.ERA
        self.ERA=self.losspoint/(int(self.inning)+self.inning%1*10*0.33333)*9
        Update_ERA_ranking(ERAranking0,tempERA,self.ERA,self.name,pitcher)
Pitchers=[]
ncd=[]
ktw=[]
dsb=[]
lgt=[]
Team_pitches={"NCD":ncd,"KTW":ktw,"DSB":dsb,"LGT":lgt}
ERA_ranking=[]
open_prev_record=input("Open previously saved file?(Y/N): ")
if open_prev_record=='Y':
    with open("2020014348_GyuhoTAE.txt","rb") as fileup:
        Pitchers=pickle.load(fileup)
        Team_pitches=pickle.load(fileup)
        ERA_ranking=pickle.load(fileup)
else:
    print()
while True:
    print()
    print("Select operation")
    print("=============================")
    print("New pitcher generation (1)")
    print("Update a pitcher (2)")
    print("Display all pitchers (3)")
    print("Display a team (4)")
    print("Retrieve a pitcher (5)")
    print("Modify a pitcher (6)")
    print("Save all records (7)")
    print("Open previous records (8)")
    print("Exit (0)")
    select=input("Operation?: ")
    if select=='1':
        M0=input("How many pitchers to upload? :")
        M=Checkint(M0)
        for m in range(M):
            print(m+1,"'s player")
            New_pitcher(Pitchers, Team_pitches, ERA_ranking)
    elif select=='2':
        name=input("What is the name of the pitcher?: ")
        nn=0
        for n in Pitchers:
            if n.name==name:
                n.update_stats(ERA_ranking,Pitchers)
                nn+=1
        if nn==0:
            print("No data")
    elif select=='3':
        Display_all(Pitchers,ERA_ranking)
    elif select=='4':
        Display_team(Team_pitches,Pitchers,ERA_ranking)
    elif select=='5':
        Display_pitcher(Pitchers)
    elif select=='6':
        Modify_record(Pitchers,ERA_ranking)
    elif select=='7':
        Save_all_records(Pitchers,Team_pitches,ERA_ranking)
    elif select=='8':
        with open("2020014348_GyuhoTAE.txt","rb") as fileup:
            Pitchers=pickle.load(fileup)
            Team_pitches=pickle.load(fileup)
            ERA_ranking=pickle.load(fileup)
    elif select=='0':
        exits=input("Save before exit?(Y/N): ")
        if exits=='Y':
            Save_all_records(Pitchers,Team_pitches,ERA_ranking)
        break
    else:
        print("Wrong input")
#감사합니다.
