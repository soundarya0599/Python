#!/usr/bin/env python
# coding: utf-8

# # <center> PROGRAM 2: FUNCTIONS IN PYTHONS</center>  
# ---

#    **Requirement:**
#    
#      India's first Miss Universe Sushmita Sen,the most eligible spinster in town is planning to get married soon. She wants to do her marriage shopping from Dubai Mall,the world's biggest shopping mall. Help her to plan some happy shopping by developing an interactive program.
# 
#    **Note:** All the financial transactions are to be done in cash through AED.
# 
#    So my dear data wizards make sure to have an eye at currency conversion.You are free to use builtin,userdefined and lamda functions to perform various tasks such as tax calculation,discount and billing,etc.

# In[1]:


#Function for clothing section
def Clothing():
    d=[]
    a=[]
    cost=0
    response = "y"
    cloths1=["1.Banarasi Silk - 200 د.إ ",
             "2.Chanderi Saree - 300 د.إ",
             "3.Paithani Saree - 400 د.إ",
             "4.Gota Patti Saree - 500 د.إ"]
    cloths2=["1.Lace Saree - 200 د.إ",
             "2.Printed Satin Saree -300 د.إ",
             "3.Sequin Work Saree - 400 د.إ",
             "4.Hand-Embroidered Saree - 500 د.إ"]
    cloths3=["1.Anarkali Suits & Gowns - 200 د.إ",
             "2.Light Lehengas - 300 د.إ",
             "3.Designer Lehenga - 400 د.إ",
             "4.Kerala Saree - 500 د.إ"]
    cloths4=["1.Mermaid gown - 200 د.إ ",
             "2.Sheath gown - 300 د.إ",
             "3.Bouffant skirt gown - 400 د.إ",
             "4.Circular skirt gown - 500 د.إ"]
    shops=['&OtherStories','Bloomingdales','Forever21','GoSport']
    while (response =='y'):
        print("\n\t Clothing shop names")
        print("\n\t --------------------\n")
        for c in shops:
            print("\t",c)
        shop=input("\n\nEnter the shop name:")
        print("\n")
        if (shop=="&OtherStories"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to &OtherStories\n\n")
            for cloth in cloths1:
                print(cloth)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            d.append(s)
            a.append(amt)
            cost=sum(a,cost)     #Sum function to sum the values
            print ("\nClothing Section TOTAL:",cost,"د.إ")
            print("**************************************************************************")
        elif (shop=="Bloomingdales"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Bloomingdales\n\n")
            for cloth in cloths2:
                print(cloth)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            d.append(s)
            a.append(amt)
            cost=sum(a)
            print ("\nClothing Section TOTAL:",cost,"د.إ")
            print("**************************************************************************")
        elif (shop=="Forever21"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Forever21\n\n")
            for cloth in cloths3:
                print(cloth)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            d.append(s)
            a.append(amt)
            cost=sum(a)
            print ("\nClothing Section TOTAL:",cost,"د.إ")
            print("**************************************************************************")
        elif (shop=="GoSport"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Gosport\n\n")
            for cloth in cloths4:
                print(cloth)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            d.append(s)
            a.append(amt)
            cost=sum(a)
            print ("\nClothing Section TOTAL:",cost,"د.إ")
            print("**************************************************************************")
        
        response = input("\nOrder anything else(y/n):")
        
    return cost,d,a


# In[2]:


#Function for Jewellery section
def Jewellery():
    j=[]
    am=[]
    cost1=0
    response = "y"
    shops=['Claires','La Bella','Louis Vuitton','Diamond World']
    jewel=["1.Earrings - 200 د.إ",
            "2.Bangles - 300 د.إ",
            "3.Kolar Fashion - 400 د.إ",
            "4.Neckpeice - 500 د.إ"]
    jewel2=["1.Ring - 200 د.إ",
              "2.choker - 200 د.إ",
              "3.jhumkis - 300 د.إ",
              "4.Bracelet - 400 د.إ"]
    jewel3=["1.Stud - 200 د.إ",
              "2.Nose Pin - 100 د.إ",
              "3.Brooch - 200 د.إ",
              "4.Armlet - 300 د.إ "]
    jewel4=["1.Wristlet - 300 د.إ",
              "2.Head-Locket - 200 د.إ",
              "3.Anklet - 300 د.إ",
              "4.Necklace - 500 د.إ"]
    while (response =='y'):
        print("\n\t Jewellery shop names")
        print("\n\t --------------------\n")
        for c in shops:
            print("\t",c)
        shop=input("\n\nEnter the shop name:")
        print("\n")
        if (shop=="Claires"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Claires\n\n")
            for i in jewel:
                print(i)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            j.append(s)
            am.append(amt)
            cost1=sum(am)
            print ("\nJewellery Section TOTAL:",cost1,"د.إ")
            print("**************************************************************************")
        elif (shop=="La Bella"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to La Bella\n\n")
            for i in jewel2:
                print(i)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            j.append(s)
            am.append(amt)
            cost1=sum(am)
            print ("\nJewellery Section TOTAL:",cost1,"د.إ")
            print("**************************************************************************")
        elif (shop=="Louis Vuitton"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Louis Vuitton\n\n")
            for i in jewel3:
                print(i)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            j.append(s)
            am.append(amt)
            cost1=sum(am)
            print ("\nJewellery Section TOTAL:",cost1,"د.إ")
            print("**************************************************************************")
        elif (shop=="Diamond World"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Diamond World\n\n")
            for i in jewel4:
                print(i)
            opt = str(input("\nName:"))
            amt = int(input("Cost in د.إ:"))
            s=[opt,amt]
            j.append(s)
            am.append(amt)
            cost1=sum(am)
            print ("\nJewellery Section TOTAL:",cost1,"د.إ")
            print("**************************************************************************")
        
        response = input("\nOrder anything else(y/n):")
        
       
    return cost1,j,am


# In[3]:


#Function for Cosmetics section
def cosmetics():
    cost2=0
    cs=[]
    amt=[]
    response = "y"
    shops=['Bloomingdales','Clarins','Bobbi Brown','MAC']
    cosmetics1=["1.Bronzer - 200 د.إ",
                "2.Hilighter - 300 د.إ",
                "3.Eyeshadow - 400 د.إ",
                "4.Maskara - 500 د.إ",
                "5.Eyelashes - 200 د.إ "]
    cosmetics2=["1.lipstick - 200 د.إ",
                "2.BB cream -300 د.إ ",
                "3.Hair oil -300 د.إ",
                "4.skin cream - 200 د.إ"]
    cosmetics3=["1.Eye gel - 200 د.إ",
                "2.Lip gloss - 300 د.إ",
                "3.Hair spray - 100 د.إ",
                "4. gel wax -200 د.إ"]
    cosmetics4=["1.Bronzer - 200 د.إ",
                "2.Hilighter - 300 د.إ",
                "3.Eyeshadow - 400 د.إ"]
    while (response =='y'):
        print("\n\t Cosmetics shop names")
        print("\n\t --------------------\n")
        for c in shops:
            print("\t",c)
        shop=input("\n\nEnter the shop name:")
        print("\n")
        if (shop=="Bloomingdales"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Bloomingdales\n\n")
            for i in cosmetics1:
                print(i)
            opt = str(input("\nName:"))
            am = int(input("Cost in د.إ:"))
            s=[opt,am]
            cs.append(s)
            amt.append(am)
            cost2=sum(amt)
            print ("\nCosmetics Section TOTAL:",cost2,"د.إ")
            print("**************************************************************************")
        elif (shop=="Clarins"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Clarins\n\n")
            for i in cosmetics2:
                print(i)
            opt = str(input("\nName:"))
            am = int(input("Cost in د.إ:"))
            s=[opt,am]
            cs.append(s)
            amt.append(am)
            cost2=sum(amt)
            print ("\nTOTAL:",cost2,"د.إ")
            print("**************************************************************************")
        elif (shop=="Bobbi Brown"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to Bobbi Brown\n\n")
            for i in cosmetics3:
                print(i)
            opt = str(input("\nName:"))
            am = int(input("Cost in د.إ:"))
            s=[opt,am]
            cs.append(s)
            amt.append(am)
            cost2=sum(amt)
            print ("\nCosmetics Section TOTAL:",cost2,"د.إ")
            print("**************************************************************************")
        elif (shop=="MAC"):
            print("**************************************************************************")
            print("\n\n\t\t\t\tWelcome to MAC\n\n")
            for i in cosmetics4:
                print(i)
            opt = str(input("\nName:"))
            am = int(input("Cost in د.إ:"))
            s=[opt,am]
            cs.append(s)
            amt.append(am)
            cost2=sum(amt)
            print ("\nCosmetics Section TOTAL:",cost2,"د.إ")
            print("**************************************************************************")
        
        response = input("\nOrder anything else(y/n):")
        
       
    return cost2,cs,amt


# In[4]:


# Initializing bill_number 
bill_number=100


# In[5]:


# Main driven code
from datetime import date
print("__________________________________________________________________________________________________________")
text=" welcome to the dubai mall"
fbill=0
bill=[]
shops=[]
rate=[]
response="yes"

# string methods- upper():converts string to uppercase
print("\n\t\t\t\t",text.upper()) 
print("\n\t\t\t\t  *************************")

# about dubai mall
print("\n\n\t\t'The Dubai Mall - A place like no other. A new day, a new dawn.'")
print("\t\t From the windswept sands, a new legend rises; a mall of epic")
print("\t\t proportions that is named The Dubai Mall.")
print("__________________________________________________________________________________________________________")

# customer details
cust_name=str(input("Enter your name: "))
cust_phone=int(input("Enter your phone number: "))
#validation for phone number- len(): length of variable 
phone=str(cust_phone)
for i in [3]:
    if (len(phone)!=10):
        cust_phone=int(input("Enter your correct phone number: "))
        phone=str(cust_phone)
    else:
        break

today=date.today()

print("__________________________________________________________________________________________________________")
while (response=="yes"):
    print("\nWhich Section You want to purchase ?? ")
    print("\n 1.Clothing")
    print("\n 2.Jewellery ")
    print("\n 3.Cosmetics")
    ch=int(input("\n Enter the option number: "))
    print("__________________________________________________________________________________________________________")


    if (ch == 1):
        c1,s1,a1=Clothing()
        for i in s1:
            shops.append(i)
        for j in a1:
            rate.append(j)
        bill.append(c1)
        fbill=sum(bill)

    elif (ch == 2):
        c2,s2,a2=Jewellery()
        for i in s2:
            shops.append(i)
        for j in a2:
            rate.append(j)
        bill.append(c2)
        fbill=sum(bill)
    
    elif (ch == 3):
        c3,s3,a3=cosmetics()
        for i in s3:
            shops.append(i)
        for j in a3:
            rate.append(j)
        bill.append(c3)
        fbill=sum(bill)
    
    else:
        print("Invalid option")
    response=str(input("Do want visit section menu (yes/no):"))    
    

total=fbill
GST_Amount=0
GST_per=5
conversion=lambda total:fbill * 20.38
before_gst=conversion(total)
tax= lambda GST_Amount:(conversion(total)*GST_per)/100
Net_Price=conversion(total)+tax(GST_Amount)
print("__________________________________________________________________________________________________________")
print("\n\t\t\t\t\t 🅣🅗🅔 ⒹⓊⒷⒶⒾ 🅜🅐🅛🅛")
print("\n")
print("\t Bill Number  : ",bill_number,"\t\t\t\t         Customer Name  : ",cust_name)
print("\t Date         : ",today.day,"/",today.month,"/",today.year,"\t\t\t\t Phone Number   : ",cust_phone)

print("__________________________________________________________________________________________________________")
print("\n")
print("\t\t\t\t"+"*"+'-'*36+"*")
print("\t\t\t\t"+"|{:^20s}|{:^16s}|".format('ITEM NAME',"COST in د.إ"))
print("\t\t\t\t"+"*"+'-'*36+"*")
for i in shops:
    print("\t\t\t\t"+"|{:^20s}|{:^15d}|".format(*i))
print("\t\t\t\t"+"*"+'-'*36+"*")
print("\t\t\t\t"+"_"*36)
print("\t\t\t\t Total Price in AED(د.إ)  :",float(fbill))
print("\t\t\t\t Total price in INR(₹)   :",float(before_gst))
print("\t\t\t\t GST Price in INR(₹)     :",float(tax(GST_Amount))) 
print("\t\t\t\t Net Price in INR(₹)     :",float(Net_Price))
bill_number=bill_number+ 1
print("\n")
print("\t\t\t THANK YOU ❤️️❤️️❤️️ VISIT AGAIN TO 🅣🅗🅔 ⒹⓊⒷⒶⒾ 🅜🅐🅛🅛")
print("__________________________________________________________________________________________________________")

