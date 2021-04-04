#!/usr/bin/env python
# coding: utf-8

# # <center> PROGRAM 1:MUTABLE AND IMMUTABLE TYPES </center>

#   **Requirement:**
#   
#     Mr.Hulk is tired of body building.He now wants to exercise his brain.He has found his interest in Python.As a 1st initiative he wants to build a program to store university details of CHIRST (DoE,Campuses,Administrators details,Department details, Programmes,Course details,Student details,etc). Since you are the budding data scientists please help hi in achieving his accomplishments.
# 
#    **Note:** For the sake of simplicity course,teachhers and students details can be restricted to MDS program of computer science department.

# In[1]:


# Importing Libraries

import pandas as pd # importing panda
import numpy as np  # importing Numpy


# In[2]:


#Function for Date of Establishment [tuple]

def DoE(): 
    print("\n")
    my_tuple = ("\t    DATE OF ESTABLISHMENT  \n\t\t\t    ======================",
                "Christ (Deemed To Be University) Bangalore, Karnataka",
                "Founded by St Kuriakose Elias Chavara on", [(15),"july",(1969)])
    print("\t\t",my_tuple[0])
    print("\t\t",my_tuple[1])
    print("\t\t",my_tuple[2])
    print("\t\t\t\t",my_tuple[3])


# In[3]:


#Function for Campuses Details [tuple]

def Campus_Details():
    print("\n")
    print("\t\t\t CAMPUSES  \n\t\t\t=========\n")
    Campuses = ("Central Campuse,Bangalore",
                "Bennerghatta Road Campus",
                "Kengeri campus",
                "Delhi NCR campus",
                "Pune lavasa campus")
    for i in Campuses:
        print("\t\t",i)


# In[4]:


#Function for Administrations Details [List]

def Administrations_Details():
    print("\n")
    print("\t\t\t\t   GENERAL ADMINISTRATION  \n\t\t\t\t   ======================\n")
    Admin1 = ["CHANCELLOR : Dr Fr George Edayadiyil, CMI",
              "VICE CHANCELLOR: Dr Fr Abraham V M, CMI",
              "PRO-VICE CHANCELLOR: Dr Fr Jose",
              "REGISTRAR:Dr Anil Joseph Pinto",
              "CHIEF FINANCE OFFICER: Fr Jobi Xavier, CMI",
              "CONTROLLER OF EXAMINATIONS: Prof. Johny Joseph",
              "PERSONNEL OFFICER: Dr Fr Joseph Varghese"]
    for i in Admin1:
        print("\t\t\t",i)
        
    print("\n\n\t\t\t\t   ACADEMIC ADMINISTRATION  \n\t\t\t\t   ======================\n")
    Admin2 = ["DEAN - ARTS AND HUMANITIES                  : Dr John Joseph Kennedy",
              "DEAN - SOCIAL SCIENCES                      : Dr Tony Sam George",
              "DEAN - SCIENCES                             : Dr George Thomas C",
              "DEAN - COMMERCE                             : Dr Tomy K Kallarakal",
              "DEAN - MANAGEMENT                           : Dr Jain Mathew",
              "DEAN - BUSINESS STUDIES & SOCIAL SCIENCES   : Dr Jyothi Kumar",
              "DEAN - FACULTY OF ENGINEERING               : Dr Iven Jose",
              "DEAN - SCHOOL OF LAW                        : Dr Jayadevan S Nair",
              "DELHI NCR CAMPUS                            : Dr Fr Viju P D",
              "PUNE LAVASA CAMPUS                          : Dr Fr Jossy P George",
              "DEAN - INTERNATIONAL RELATIONS              : Dr Suniti Phadke",
              "ASSOC. DEAN - INSTITUTE OF MANAGEMENT       : Dr Georgy P Kurien",
              "ASSOC. DEAN - INSTITUTE OF MANAGEMENT       : Dr Jeevananda S",
              "ASSOC. DEAN - SCIENCE AND CHOICE BASED INTERDISCIPLINARY MASTERS PROGRAMME  : Dr JOSEPH T V  "]
    for i in Admin2:
        print("\t",i)


# In[5]:


#Function for Department Details [Tuple]

def Department_Details():
    print("\n")
    print("\n\t\t\t\t   ARTS AND HUMANTIES   \n\t\t\t\t   ===================\n")
    Dean1 = ( "ENGLISH",
              "LANGUAGES",
              "MEDIA STUDIES",
              "PERFORMING ARTS,THEATRE STUDIES AND MUSIC",
              "PHILOSOPHY AND THEOLOGY")
    for i in Dean1:
        print("\t\t\t",i)
    print("\n")    
    print("\n\t\t\t\t   SOCIAL SCIENCES   \n\t\t\t\t   ================\n")
    Dean2 = ( "ECONOMICS",
              "INTERNATIONAL STUDIES,POLITICAL SCIENCE AND HISTORY",
              "PSYCHOLOGY",
              "SOCIOLOGY AND SOCIAL WORK")
    for i in Dean2:
        print("\t\t\t",i)
    print("\n")
    print("\n\t\t\t\t   SCIENCES   \n\t\t\t\t   ===========\n")
    Dean3 = ("CHEMISTRY",
              "COMPUTER SCIENCES",
              "LIFE SCIENCES",
              "MATHEMATICS",
              "PHYSICS AND ELECTRONICS",
              "STATISTICS")
    for i in Dean3:
        print("\t\t\t",i)
    print("\n")
    print("\n\t\t\t\t     COMMERCE   \n\t\t\t\t   ===========\n")
    Dean4 = ( "COMMERCE",
              "PROFESSIONAL STUDIES")
    for i in Dean4:
        print("\t\t\t",i)
        
    print("\n")
    print("\n\t\t\t    SCHOOL OF BUSINESS AND MANAGEMENT   \n\t\t\t  ======================================\n")
    Dean5 = ( "BUSINESS MANAGEMENT",
              "HOTEL MANAGEMENT",
              "TOURISM MANAGEMENT")
    for i in Dean5:
        print("\t\t\t",i)

    print("\n")
    print("\n\t\t\t  BANGALORE BANNERGHATTA ROAD CAMPUS   \n\t\t\t  ====================================\n")
    Dean6 = ( "ARTS & HUMANITIES,SOCIAL SCIENCES,BUSINESS & MANAGEMENT")
    print("\t\t\t",Dean6)

    print("\n")
    print("\n\t\t\t  SCHOOL OF ENGINEERING AND TECHNOLOGY   \n\t\t\t\t  =================================\n")
    Dean7 = ( "Mechanical and Automobile Engineering",
              "Civil Engineering",
              "Electrical and Electronics Engineering",
              "Sciences and Humanities",
              "Computer Science and Engineering")
    for i in Dean7:
        print("\t\t\t",i)
        
    print("\n")
    print("\n\t\t\t\t     SCHOOL OF LAW   \n\t\t\t\t   ==================\n")
    Dean8 = ("SCHOOL OF LAW")
    print("\t\t\t\t  ",Dean8)

    print("\n")
    print("\n\t\t\t\t    SCHOOL OF EDUCATION   \n\t\t\t\t   ======================\n")
    Dean9 = ("SCHOOL OF EDUCATION")
    print("\t\t\t\t  ",Dean9)
        
    print("\n")
    print("\n\t\t\t\t    SCHOOL OF ARCHITECTURE   \n\t\t\t\t   ======================\n")
    Dean10 = ("ARCHITECTURE")
    print("\t\t\t\t  ",Dean10)


# In[6]:


#Function for Programmes Details in COMPUTER SCIENCES [Tuple]

def Programmes_Details():
    print("\n")
    print("\t\t\t\t\t  Doctoral (PhD)   \n\t\t\t\t\t   =============\n")
    P1 = ( "DOCTOR OF PHILOSOPHY (PHD) IN DATA SCIENCE",
           "DOCTOR OF PHILOSOPHY (PHD) IN COMPUTER SCIENCE")
    for i in P1:
        print("\t\t\t",i)
    print("\n")    
    print("\t\t\t\t\t  M Phil   \n\t\t\t\t\t   =========\n")
    P2 = ( "DOCTOR OF PHILOSOPHY (PHD) IN DATA SCIENCE")
    print("\t\t\t",P2)
    print("\n")    
    print("\t\t\t\t\t     Postgraduate   \n\t\t\t\t\t   =================\n")
    P3 = ( "MASTER OF SCIENCE (DATA SCIENCE)",
           "MSC (DATA ANALYTICS)",
           "MASTER OF SCIENCE (COMPUTER SCIENCE)",
           "MASTER OF SCIENCE (COMPUTER SCIENCE AND APPLICATIONS)",
           "MASTER OF COMPUTER APPLICATIONS (MCA)")
    for i in P3:
        print("\t\t\t",i)
    print("\n")    
    print("\t\t\t\t\t    Undergraduate   \n\t\t\t\t\t   ===============\n")
    P4 = ( "BSC CME-BACHELOR OF SCIENCE (BSC) IN COMPUTER SC, MATHS, ELECTRONICS",
           "BSC CMS-BACHELOR OF SCIENCE (BSC) IN COMPUTER SC, MATHS, STATISTICS",
           "BCA-BACHELOR OF COMPUTER APPLICATIONS")
    for i in P4:
        print("\t\t\t",i)


# In[7]:


#Function for Course Details in MDS [Dictionary]

def Course_Detail():
    print("\n")
    Fac={'Course code':('MDS161A','MDS131','MDS133','MDS134','MDS171','MDS173','MDS132','MDA172'),
         'Course name':('Introduction to Statistics','Mathematical Foundation','Principles of Data Science','Research Methodology','Data Base Technologies','Programming for Data Science in Python','Probability and Distribution Theory','Inferential Statistics'),
         'Instructor':('Dr.Sahana Prasad','Dr Jayanta Biswas','Dr Rajesh R','Dr Deepa V Jose','Dr Senthilnathan T','Dr Ummesalma M','Dr Sharon Varghese','Dr Azarudheen S')}
    for i,j in Fac.items():
        print("{}:{}\n".format(i,j))


# In[8]:


#Function for Student Details [Dictionary]

import csv
def Student_Detail():
    print("\n")
    stud=csv.DictReader(open("Python_list.csv"))
    for i in stud:
        print(i)


# In[9]:


#Function for Student Details [Dictionary with pandas]

def Student_Details():
    print("\n")
    stud=pd.read_csv('Python_list.csv')
    return stud


# In[11]:


#Function for Course Details in MDS [Dictionary with pandas]

def Course_Details():
    print("\n")
    Faculty={'Course code':pd.Series(('MDS161A','MDS131','MDS133','MDS134','MDS171','MDS173','MDS132','MDA172')),
              'Course name':pd.Series(('Introduction to Statistics','Mathematical Foundation','Principles of Data Science','Research Methodology','Data Base Technologies','Programming for Data Science in Python','Probability and Distribution Theory','Inferential Statistics')),
             'Instructor':pd.Series(('Dr.Sahana Prasad','Dr Jayanta Biswas','Dr Rajesh R','Dr Deepa V Jose','Dr Senthilnathan T','Dr Ummesalma M','Dr Sharon Varghese','Dr Azarudheen S'))}
    MDS_Faculty=pd.DataFrame(Faculty)
    return MDS_Faculty


# In[13]:


# Function for About christ

def AboutChrist():
    print ("\t\t\t\t   CHRIST DEEMED TO BE UNIVERSITY\n\n")
    
    vision='''CHRIST (Deemed to be University), a premier educational institution, is an academic fraternity of individuals dedicated to the motto of  'EXCELLENCE AND SERVICE.'

We strive to reach out to the star of perfection through an earnest academic pursuit for 'excellence,' and our efforts blossom into 'service' through our creative and empathetic involvement in the society to transform it.

Education prepares one to face the challenges of life by bringing out the best in him/her. If this is well accepted, education should be relevant to the needs of the time and address the problems of the day. Being inspired by Blessed Kuriakose Elias Chavara, the founder of Carmelites of Mary Immaculate and the pioneer in innovative education, CHRIST (Deemed to be University) was proactive to define and redefine its mission and strategies reading the signs of the time.'''
    print("\t\t\t\t  The VISION of the CHRIST")
    print("\t\t\t\t  ========================")
    print(vision) 
    
    
    mission='''CHRIST (Deemed to be University) is a nurturing ground for an individual's holistic development to make an effective contribution to the society in a dynamic environment.'''
    print("\n\n\n\t\t\t\tThe Mission of the CHRIST:")
    print("\t\t\t\t  ========================")
    print(mission)
    
    Core_Values='''The values which guide us at CHRIST (Deemed to be University) are:
•  Faith in God
•  Moral Uprightness
•  Love of Fellow Beings
•  Social Responsibility
•  Pursuit of Excellence'''
    print("\n\n\n\t\t\t\tThe Core Values of the CHRIST:")
    print("\t\t\t\t  ========================")
    print(Core_Values)
    
    print("\n")


# In[14]:


# Function for Admin page

def Admin():
    print("\t\t\t*************************************************************")
    print("\t\t\t\t\t\t\tWELCOME ADMIN")
    print("\t\t\t*************************************************************")
    print("Editing should be done")
#Editing options should be provided here 


# In[15]:


# Main Code

print("\n\n")
print("_______________________________________________________________________________________________________________")
print("\t\t\t\t\t\tCHRIST (Deemed to be University) ")
print("_______________________________________________________________________________________________________________")
print("\n\n")
opt="Y"
while (opt=="Y"):
    print("\nAre you an ADMIN ? (YES/NO)")
    admin=input()
    if(admin=="YES" or admin=="yes" or admin=="Yes"):
        print("Enter the password : ")
        password=input()
        if(password=="christadmin"):
            Admin()
        else:
            print("Invalid Password")
            print("Try again")
            password=input()
        
    elif(admin=="NO" or admin=="no" or admin=="No"):
        print("_______________________________________________________________________________________________________________")
        print("\nSelect any: ")
        print("\n\t\t\t\t0. About Chist")
        print("\n\t\t\t\t1. DoE")
        print("\n\t\t\t\t2. Campuses ")
        print("\n\t\t\t\t3. Administrations")
        print("\n\t\t\t\t4. Department Details")
        print("\n\t\t\t\t5. Programmes Details")
        print("\n\t\t\t\t6. Course Details")
        print("\n\t\t\t\t7. Student Details")
        print("\n")
        print("Enter your choice for particular detials?")
        print("_______________________________________________________________________________________________________________")
        choice=int(input())
        if(choice==0):
            AboutChrist()
           
        elif(choice==1):
            
            DoE()
           
        elif(choice==2):
            
            Campus_Details()
           
        elif(choice==3):
            
            Administrations_Details()
           
        elif(choice==4):
           
            Department_Details()
            
        elif(choice==5):
            
            Programmes_Details()
            
        elif(choice==6):
            
            Course_Details()
            
        elif(choice==7):
           
            Student_Details()
          
        else:
            print("Invalid Option")
    else:
        print("invalid option")
    print("\n")
    print("_______________________________________________________________________________________________________________")
    print("Do you want to go back to home ? (Y/N)")
    opt=input()


# ## OUTPUT OF EACH FUNCTIONS

# In[16]:


# ABOUT CHRIST

AboutChrist()


# In[17]:


# Date of Establishment

DoE()


# In[18]:


# Different Campuses

Campus_Details()


# In[19]:


# Administration details

Administrations_Details()


# In[20]:


# Department Details

Department_Details()


# In[21]:


# Programme Details

Programmes_Details()


# In[22]:


# MDS course details

Course_Details()


# In[23]:


# MDS student details

Student_Details()

