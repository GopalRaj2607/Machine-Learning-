# -*- coding: utf-8 -*-
"""Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wuGUx0Afx1465zeRhPnvgoN8uh6HN8pt

Real Life Regression Case Study
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import seaborn as sns

ice = pd.read_csv('IceCreamData.csv')
ice

"""Revenue: Depends on Air Temp
Temp: Its Totally Unique & Independent
"""

ice.info()

sns.jointplot(x='Temperature',y='Revenue',data=ice,kind='reg')

"""From the EDA We Came to Know that this Graphical Representation of Data going to State y = mx + c

X( Temp ) - Independent
y(Revenue)= mx + c

Basically to Solve the Eqn. we need m & c

First We have to Divide Our Dataset into Two Parts
1. Dependent
2. Independent
"""

y=ice['Revenue']
X=ice[['Temperature']]

y

X

"""Whenever We will Perform Any Kind of Regression We have to Divide Our Dataset into X , y already we did it

After this division we have to Sub Divide Our Dataset into Two Sub Parts

1. Test data
2. Train Data
"""

ice.info()

"""We have 500 Rows But We are going to Run One Testing Mode - So We have to Take Few % from the Entire Data and We can Make a Trial Run - And We match it with Remaining Data"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.24)

# We have 500 Rows and From that 500 Rows we have taken 24%
X_test

X_train

from sklearn.linear_model import LinearRegression

linear = LinearRegression(fit_intercept=True)

X_test

X_train

"""From 500 Rows We have Cut Down 24% Means 120 Rows from Mother Data , So Internal Allignment of the CSV File Destroyed

Now We Performed All Task For X_test & y_test But Our Main 380 Rows or 76% Data Alignment Also Damanged.
"""

linear.fit(X_train,y_train)

"""We have to Find m & c Value

m = Coef (mx)
c = Intercept(c)

y = mx also Possible , May be C not Available in that case
"""

print('Linear Model Coefficient(m):',linear.coef_)
print('Linear Model Coefficient(c):',linear.intercept_)

"""y (Revenue ) = 21.41 * 25.42 + 45.622

y = 589 INR
"""

ice.iloc[197:199]

