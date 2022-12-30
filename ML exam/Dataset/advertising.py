import pandas as pd
dataset = pd.read_csv('advertising.csv')
dataset.head()

x = dataset.iloc[:,:-1] 
y = dataset.iloc[:,-1]
x.head()
y.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=100)
m_r = LinearRegression()
m_r.fit(x_train,y_train)

print('intercept:',m_r.intercept_)
print("coefficients:")
list(zip(x,m_r.coef_))


y_pred = m_r.predict(x_test)
print("predictiion:{}".format(y_pred))