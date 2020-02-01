#simple regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =1/3,random_state = 0)
#fitting simple linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
y_pred = regressor.predict(X_test)

#visualing
plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary vs Experince')
plt.xlabel('year of experince')
plt.ylabel('Salary')
plt.show()

#using seaborn 
import seaborn as sn
fig,ax1 = plt.subplots(figsize=(15,10))
sn.scatterplot(x='YearsExperience',y= 'Salary',data = dataset,ax=ax1)
plt.show(fig)