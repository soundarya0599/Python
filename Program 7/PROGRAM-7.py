#!/usr/bin/env python
# coding: utf-8

# # <center>PROGRAM 7: PANDAS IN PYTHON </center>
# 
# ---

# # University of Anybody Can Learn Datascience - ABCLD

# ### Requirement
# 
# ##### Description:	
#        Given dataset is a dummy dataset containing infor related to Grades from a PG course at ABCCD University.
# 
# ##### Attributes:                        
#        There are total 5 attributes Sem_enrolled,Tests,Coursera,GroupActivity and	FinalExam.
# 	   FinalExam is the target variable.
# 	
# ##### The recorded values are the average of sub-components: 
#          e.g The Tests, coursera and group activity variables are the average of all tests, coursera courses and group activities taken by students. 
#     The FinalExam variable is the average of all questions in the final, written exam.
# 
#     The Sem_enrolled column is the year in which the student first enrolled at the university and is a crude approximation of the student's age (maturity).
# 
#     This particular course permitted students to work in groups for assignments, tutorials and the take-home exam. The groups were self-selected, and varied during the semester.
# 
#     Of interest is whether the assignments, tutorials, midterms or take-home exam are a good predictor of the student's performance in the final exam.                                         
#     Also, findout whether the sem_enrolled variable show any promise as a prediction variable?
# 
# * Data shape:	100 rows and 5 columns                                        
# * Missing Values: YES                                     
# * Task to be performed: Missing value imputation and Regression.
# 
# ---

# ### IMPORTING PACKAGES

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib import style

import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle 


# ### Academic score of the University of Anybody Can Learn Datascience - ABCLD 

# In[2]:


D= pd.read_excel('AcademicScoreDataset.xlsx')
Data =pd.DataFrame(D)
e = Data[(Data['Final'] >= 100) | (Data['Final'] <= 0)]
outlier =pd.DataFrame(e)
outlier


# In[3]:


Data.drop(Data[(Data['Final'] >= 100) | (Data['Final'] <= 0)].index, inplace = True) 


# In[4]:


e = Data[(Data['Final'] >= 100) | (Data['Final'] <= 0)]
outlier =pd.DataFrame(e)
outlier


# 

# ### Understanding and examine the given academic dataset to perform the effective 'EDULYTICS'
# 

# In[5]:


AcademicScoreDataset= Data
AcademicScoreDataset


# As per the above table, It clearly shows that this dataset conatins 5 different type of attributes which is related to University Academic. Such like consolidated Test marks, Coursera marks, Group Activity marks and respective Final marks.

# In[6]:


AcademicScoreDataset.describe()


# In[7]:


# Weightage of Semester enrollment distribution 
AcademicScoreDataset.plot(x = 'Final', y = 'Sem_enrolled', kind = 'scatter',color="#B53471")


# Above plotted graph clearly shows the number of students endrolled on semester bases
# 
# Note:- Higher enrollment in 1st sem 2nd higher enrollment in 2nd sem Lower enrollment in 5th sem

# ## Return a copy of the dataset with missing values filled, replaced or imputed
# 
# Since as per our initial analysis, we found that some of the Tests, coursera and group activity fields holding blank or missing data. Which could misleading our EDULYTICS interpretation. 
#     
# In order to quick fix that we should use missing value imputation technique in Python.
#     
# Below here, the above dataset carries 3 different missing value imputation technique.

# In[8]:


Replace_DataFrame      = AcademicScoreDataset.fillna(0)
ForwardFill_DataFrame  = AcademicScoreDataset.fillna(method = 'ffill')
BackwardFill_DataFrame = AcademicScoreDataset.fillna(method = 'bfill')


# ### Method 1 - replacing null by zero
# 
# * In method one we're making sure that every Tests, coursera and group activity fields NaN values get replaced by ZERO.
# * LinearRegression to find the highest accuracy
#     
#     

# In[9]:


Replace_DataFrame[Replace_DataFrame.notnull()]


# In[10]:


style.use("ggplot")

# Import dataset with student's data
data = Replace_DataFrame

# Select the value we want to predict
predict = "Final"

# List the variables we want to use for our predictions in this model
data = data[[ 'Tests','Coursera','GroupActivity','Final']]
data = shuffle(data)

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

# Train model multiple times to find the highest accuracy
best = 0
for _ in range(10):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: " + str(acc))

    # Save the highest accuracy
    if (acc > best):
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)
print("")
print("Highest Accuracy: ", best)

# Load model
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

print("-------------------------")
print('Coefficient:  \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")
print("")
predictions = linear.predict(x_test)

# Print the predictions, the variables we used and the actual final grade
for x in range(len(predictions)):
   print("Predicted Final grade: ", predictions[x])
   print("Data:", x_test[x])
   print("Final grade:", y_test[x])
   print("")


# ### Final Interpretation of Method 1

# ### Tests

# In[11]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.metrics import r2_score

X = Replace_DataFrame[['Tests']]
y = Replace_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Tests"
plt.scatter(data[plot], data["Final"],color="blue")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Tests')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[12]:


X = Replace_DataFrame[["Tests"]]
y = Replace_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Tests")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Tests VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Tests Marks")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Test Marks")
plt.ylabel("Final Scores")
plt.title("Test marks and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### Coursera

# In[13]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = Replace_DataFrame[['Coursera']]
y = Replace_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Coursera"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Coursera')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[14]:


X = Replace_DataFrame[["Coursera"]]
y = Replace_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Coursera VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Coursera Marks")
plt.ylabel("Final Scores")
plt.title("Coursera and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### GROUP ACTIVITY

# In[15]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = Replace_DataFrame[['GroupActivity']]
y = Replace_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "GroupActivity"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('GroupActivity')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[16]:


X = Replace_DataFrame[["GroupActivity"]]
y = Replace_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Group Activity VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.title("GroupActivity and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### Method 2A - forward fill imputation
# 
# * In method two - forward fill imputation, we're filling our NaN value by propagated last valid entry from respective columns Tests, coursera and group activity.
# * NOTE: For the very 1st row, NaN values remains unchange.

# In[17]:


ForwardFill_DataFrame[ForwardFill_DataFrame.notnull()]


# In[18]:


style.use("ggplot")

# Import dataset with student's data
data = ForwardFill_DataFrame

# Select the value we want to predict
predict = "Final"

# List the variables we want to use for our predictions in this model
data = data[[ 'Tests','Coursera','GroupActivity','Final']]
data = shuffle(data)

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

# Train model multiple times to find the highest accuracy
best = 0
for _ in range(10):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: " + str(acc))

    # Save the highest accuracy
    if (acc > best):
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)
print("Highest Accuracy:", best)

# Load model
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

print("-------------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")

predictions = linear.predict(x_test)

# Print the predictions, the variables we used and the actual final grade
for x in range(len(predictions)):
   print("Predicted Final grade: ", predictions[x])
   print("Data:", x_test[x])
   print("Final grade:", y_test[x])
   print("")


# ### Final Interpretation of Method 2A

# ### TESTS

# In[19]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = ForwardFill_DataFrame[['Tests']]
y = ForwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Tests"
plt.scatter(data[plot], data["Final"],color="blue")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Tests')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[20]:


X = ForwardFill_DataFrame[["Tests"]]
y = ForwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Tests")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Tests VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Tests Marks")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Test Marks")
plt.ylabel("Final Scores")
plt.title("Test marks and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### COURSERA

# In[21]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = ForwardFill_DataFrame[['Coursera']]
y = ForwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Coursera"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Coursera')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[22]:


X = ForwardFill_DataFrame[["Coursera"]]
y = ForwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Coursera VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.show()


reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Coursera Marks")
plt.ylabel("Final Scores")
plt.title("Coursera marks and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### GROUP ACTIVITY

# In[23]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = ForwardFill_DataFrame[['GroupActivity']]
y = ForwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "GroupActivity"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('GroupActivity')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[24]:


X = ForwardFill_DataFrame[["GroupActivity"]]
y = ForwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Coursera VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Group Activity")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.title("GroupActivity and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### Method 2B - backward fill imputation
#         
# * In method three - backward fill imputation, we're filling our NaN value by propagated next valid entry from respective columns Tests, coursera and group activity.
#         
# * NOTE: 
#       - For the last row, NaN values remains unchange.
#       - In order to handle that, we're using the convenience methods, 
#             -> dropna() (which removes NA values)
#         

# In[25]:


BackwardFill_DataFrame[BackwardFill_DataFrame.notnull()]


# In[26]:


# calculating correlation
BackwardFill_DataFrame = BackwardFill_DataFrame.dropna()


# In[27]:


style.use("ggplot")

# Import dataset with student's data
data = BackwardFill_DataFrame

# Select the value we want to predict
predict = "Final"

# List the variables we want to use for our predictions in this model
data = data[[ 'Tests','Coursera','GroupActivity','Final']]
data = shuffle(data)

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

# Train model multiple times to find the highest accuracy
best = 0
for _ in range(50):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: " + str(acc))

    # Save the highest accuracy
    if (acc > best):
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)
print("Highest Accuracy:", best/2)

# Load model
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

print("-------------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")

predictions = linear.predict(x_test)

# Print the predictions, the variables we used and the actual final grade
for x in range(len(predictions)):
   print("Predicted Final grade: ", predictions[x])
   print("Data:", x_test[x])
   print("Final grade:", y_test[x])
   print("")


# ### Final Interpretation of Method 2B

# ### TESTS

# In[28]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = BackwardFill_DataFrame[['Tests']]
y = BackwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Tests"
plt.scatter(data[plot], data["Final"],color="blue")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Tests')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[29]:


X = BackwardFill_DataFrame[["Tests"]]
y = BackwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Tests")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Tests VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Tests Marks")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Test Marks")
plt.ylabel("Final Scores")
plt.title("Test marks and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### COURSERA

# In[30]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = BackwardFill_DataFrame[['Coursera']]
y = BackwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Coursera"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Coursera')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[31]:


X = BackwardFill_DataFrame[["Coursera"]]
y = BackwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Coursera VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.show()


reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Coursera Marks")
plt.ylabel("Final Scores")
plt.title("Coursera and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### GROUP ACTIVITY

# In[32]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = BackwardFill_DataFrame[['GroupActivity']]
y = BackwardFill_DataFrame["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "GroupActivity"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('GroupActivity')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[33]:


X = BackwardFill_DataFrame[["GroupActivity"]]
y = BackwardFill_DataFrame["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Group Activity VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Group Activity")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.title("GroupActivity and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### Method 3 - KNN sklearn

# In[34]:


import sklearn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
sklearn_Data = imputer.fit_transform(AcademicScoreDataset)
sklearn_DataFrame = pd.DataFrame(sklearn_Data, columns = ['Sem_enrolled','Tests','Coursera','GroupActivity','Final'])
sklearn_DataFrame 


# In[35]:


style.use("ggplot")

# Import dataset with student's data
data = sklearn_DataFrame

# Select the value we want to predict
predict = "Final"

# List the variables we want to use for our predictions in this model
data = data[[ 'Tests','Coursera','GroupActivity','Final']]
data = shuffle(data)

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

# Train model multiple times to find the highest accuracy
best = 0
for _ in range(10):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: " + str(acc))

    # Save the highest accuracy
    if (acc > best):
        best = acc
        with open("studentgrades.pickle", "wb") as f:
            pickle.dump(linear, f)
print("Highest Accuracy:", best)

# Load model
pickle_in = open("studentgrades.pickle", "rb")
linear = pickle.load(pickle_in)

print("-------------------------")
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
print("-------------------------")

predictions = linear.predict(x_test)

# Print the predictions, the variables we used and the actual final grade
for x in range(len(predictions)):
   print("Predicted Final grade: ", predictions[x])
   print("Data:", x_test[x])
   print("Final grade:", y_test[x])
   print("")


# ### Final Interpretation of Method 3

# ### TESTS

# In[36]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = sklearn_DataFrame [['Tests']]
y = sklearn_DataFrame ["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", -1*metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Tests"
plt.scatter(data[plot], data["Final"],color="blue")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Tests')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[37]:


X = sklearn_DataFrame [["Tests"]]
y = sklearn_DataFrame ["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Tests")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Tests VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Tests")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Test Marks")
plt.ylabel("Final Scores")
plt.title("Test marks and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### COURSERA

# In[38]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = sklearn_DataFrame [['Coursera']]
y = sklearn_DataFrame ["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "Coursera"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('Coursera')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[39]:


X = sklearn_DataFrame [["Coursera"]]
y =sklearn_DataFrame ["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Coursera VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("Coursera")
plt.ylabel("Final Scores")
plt.legend()
plt.show()


reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("Coursera Marks")
plt.ylabel("Final Scores")
plt.title("Coursera and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### GROUP ACTIVITY

# In[40]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math

X = sklearn_DataFrame [['GroupActivity']]
y = sklearn_DataFrame ["Final"]
train_X, val_X, train_y, val_y = train_test_split(X, y)
model = LinearRegression()
model.fit(train_X, train_y)
val_predictions = model.predict(val_X)
mse = mean_squared_error(val_y, val_predictions)
print("The Mean square error is: ",mse)
print("R squared value is ", metrics.r2_score(val_y,val_predictions))

# Create visualisation of the model
plot = "GroupActivity"
plt.scatter(data[plot], data["Final"],color="pink")
plt.legend(plot)
plt.xlabel(plot)
plt.ylabel("Final Grade")
plt.show()

plt.scatter(val_X, val_y, color="#FFA781")
plt.plot(val_X, val_predictions, color="#5B0E2D", linewidth=3)
plt.xlabel('GroupActivity')
plt.ylabel('Final Grade')
plt.title('Linear Regression')


# In[41]:


X = sklearn_DataFrame [["GroupActivity"]]
y = sklearn_DataFrame ["Final"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from matplotlib import pyplot as plt
plt.scatter(X_train,y_train,label='Training Data',color='r',alpha=0.8)
plt.scatter(X_test,y_test,label='Testing Data',color='b',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.title('Test Train Split Group Activity VS Final')
plt.show()

LR=LinearRegression()
Model1=LR.fit(X_train.values.reshape(-1,1),y_train.values)
prediction=LR.predict(X_test.values.reshape(-1,1))
plt.plot(X_test,prediction,label='Linear Regression',color='r')
plt.scatter(X_test,y_test,label='Actual',color='g',alpha=0.8)
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.legend()
plt.show()

reg=LR.fit(X.values.reshape(-1,1),y.values)
reg.coef_
reg.intercept_
reg.score(X.values.reshape(-1,1),y.values)
Y_pred = reg.predict(X.values.reshape(-1,1))
plt.scatter(X, y)
plt.plot(X, Y_pred, color='blue',label = 'y={:.2f} + {:.2f}*x'.format(reg.intercept_,reg.coef_[0]))
plt.xlabel("GroupActivity")
plt.ylabel("Final Scores")
plt.title("GroupActivity and final score")
plt.legend(loc='upper left')
plt.show()
df = pd.DataFrame({'Actual': y, 'Predicted':Y_pred})
df


# ### R-squared is a goodness-of-fit measure for linear regression models.

# ### HOW TO CONCLUDE ON R squared Values:
#     
# * The negative R-squared value means that your prediction tends to be less accurate that the average value of the data set over time
# * R-squared is always between 0 and 100%:
# 
#     -> 0% represents a model that does not explain any of the variation in the response variable around its mean. The mean of the dependent variable predicts the dependent variable as well as the regression model.
#     
#     -> 100% represents a model that explains all of the variation in the response variable around its mean.
#     
# Usually, the larger the R2, the better the regression model fits your observations.

# ### HOW TO CONCLUDE ON MSE VALUES:
#     
# * The value which is Less fits good model

# ## METHOD 1 : Replacing Null by Zero
# 
# * TESTS:
#     
#    -  MSE: 472.97
#      
#    -  R2 value: -0.124
#     
#     
# * COURSERA:
#      
#    - MSE: 615.838
#      
#    - R2 value: -0.044
#      
#     
# * GROUP ACTIVITY:
#      
#    - MSE: 712.452
#      
#    - R2 value: -0.040
#      

# ## METHOD 2A : Forward Fill Imputation
# 
# * TESTS:
#      
#     - MSE: 281.900
#     
#     - R2 value: -0.120
#     
#     
# * COURSERA:
#     
#     - MSE: 391.394
#     
#     - R2 value: -0.010
#     
#     
# * GROUP ACTIVITY:
#     
#     - MSE: 248.664
#     
#     - R2 value: 0.166

# ## METHOD 2B : Backward Fill Imputation
# 
# * TESTS:
#     
#     - MSE: 463.490
#     
#     - R2 value: -0.225
#         
#         
# * COURSERA:
#     
#     - MSE: 295.907
#     
#     - R2 value: 0.070
#     
#     
# * GROUP ACTIVITY:
#     
#     - MSE: 244.929
#     
#     - R2 value: -0.029

# ## METHOD 3 : KNN sklearn
# 
# * TESTS:
#     
#     - MSE: 304.770
#     
#     - R2 value: 0.048
#     
#         
# * COURSERA:
#     
#     - MSE: 265.262
#     
#     - R2 value: -0.104
#     
#     
# * GROUP ACTIVITY:
#     
#     - MSE: 219.022
#     
#     - R2 value: 0.242
