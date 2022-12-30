from sklearn.linear_model import LinearRegression
from email import header
import matplotlib.pyplot as pit
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
data = pd.read_excel('price.xlsx',index_col=None,na_values=['NA'],usecols="B,E")
df_binary = pd.DataFrame(data)
x=np.array(df_binary['OPEN']).reshape(-1,1)
y=np.array(df_binary['CLOSE']).reshape(-1,1)
df_binary.dropna(inplace=True)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)
reg=LinearRegression().fit(x_train,y_train.reshape((-1,1)))
newvalue=float(input('enter todays opening '))
y_pred = reg.intercept_ + reg.coef_ *newvalue
print(y_pred)