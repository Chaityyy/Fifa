#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def get_name(teams, lost_team):
    for ele in teams:
        if lost_team in teams[ele]:
            return ele


# In[ ]:


def gen_match(num_players, num_teams, mapp, teams):
    
    status = {}
    for ele in teams:
        status[ele] = num_teams
        
    rem_players = [ele for ele in teams]
    message = ["NIKAL LAVDE", "KEH RAHE THE JYADA GAAND NA PHULAO", "MKC BKL", "BETA TUMNSE NA HO PAYEGA",
               "BHAK BHOSDIKEEE", "HAG DIYA NA :(", "JYADA CHAUD RAHE THE", 
               "CHOTE LUND WAALO KO TOH WAISE HI HARNA THA", "CHALO BETA MAANFI MAANGO BAAP SE", 
               "ISSE BHADIYA TOH GAAND HI MARWA LETA", "CHI CHI GHANGHOOOR BEIZZATI, MAIN TOH NHI SEHTA",
               "NUNNI HOTI NHI KHADI BATAIN KARWALO BADI BADI"]

    while (len(rem_players) > 1):
        l = len(rem_players)
        y = random.randint(0,l-1)
        z = random.randint(0,l-1)
        while y==z:
            y = random.randint(0,l-1)
            z = random.randint(0,l-1)
                
        print(rem_players[y], "Vs", rem_players[z])
        print("Kaun bhadwa haara madarchod (Enter the name of team):", end=" ")
        lost_team = input()
        player = get_name(teams, lost_team)
        status[player] -= 1
        if status[player] == 0:
            rem_players.remove(player)
            lm = len(message)
            if lm:
                x = random.randint(0, lm-1)
                print()
                print("   MITR", player, message.pop(x))
                print()
        else:
            print()
    
    print("HAAN CHAL CHAL AB JYADA KHUSH BHI MAT HO, CHUTIYA", rem_players[0], "BHADWA SAALA")
    print()
    print ("   EK AUR KRNA HAI KYA, ISS BAAR MITR", rem_players[0] ,"KI MAA CHODI JAAYEGI")


# In[ ]:


def gen_teams():
    print ("Enter the number of Players : ")
    num_players = int(input())
    print()

    print ("Please enter the Player names")
    teams = {}
    mapp = []
    for i in range(num_players):
        print("Name of Player", str(i+1) + ":", end=" ")
        s = input()
        teams[s] = []
        mapp.append(s)

    print()
    print ("How many teams does each Player will have? ")
    num_teams = int(input())
    print()

    check = {}
    for _ in range(num_teams*num_players):
        x = random.randint(0,num_players-1)
        while (mapp[x] in check):
            x = random.randint(0,num_players-1)
            
        print("Hey", mapp[x], ", What do you like to pick?", end=" ")
        teams[mapp[x]].append(input())
        
        if len(teams[mapp[x]]) == num_teams:
            check[mapp[x]] = True
        
    print()
    return num_players, num_teams, mapp, teams


# In[ ]:


flag = True
while flag:
    x = gen_teams()
    gen_match(x[0], x[1], x[2], x[3])
    str = input()
    if str != "Y" and str != "y":
        flag = False
    else:
        print()


# In[ ]:




