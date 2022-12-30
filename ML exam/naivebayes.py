weather=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']
from cProfile import label
from cgi import MiniFieldStorage
from heapq import merge
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print("Weather",weather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Temp",temp_encoded)
print("Play",label)
features=list(zip(weather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,label)
predicted=model.predict([[0,2]])
print("Predicted value",predicted)
