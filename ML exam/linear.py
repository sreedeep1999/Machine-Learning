import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score
df=datasets.load_diabetes()
df=['feature_names']
diabetes_x,diabetes_y=datasets.load_diabetes(return_X_y=True)
diabetes_x.shape
diabetes_y.shape
diabetes_x=diabetes_x[:,np.newaxis,2]
diabetes_x.shape
diabetes_x_train=diabetes_x[:-20]
diabetes_x_test=diabetes_x[-20:]
diabetes_y_train=diabetes_y[:-20]
diabetes_y_test=diabetes_x[-20:]
regr=linear_model.LinearRegression()
regr.fit(diabetes_x_train,diabetes_y_train)
diabetes_y_pred=regr.predict(diabetes_x_test)
print("coefficients:\n",regr.coef_)
print("Mean squared error:%.2f"%mean_squared_error(diabetes_y_test,diabetes_y_pred))
print("coefficient ofc determination:%2f"%r2_score(diabetes_y_test,diabetes_y_pred))
plt.scatter(diabetes_x_test,diabetes_y_test,color="black")
plt.plot(diabetes_x_test,diabetes_y_pred,color="blue",linewidth=3)
plt.xlabel("age")
plt.ylabel("diabetes progression")
plt.xticks(())
plt.yticks(())
plt.show()