# Steps:
# 1. Import the Data
# 2. Clean the Data
# 3. Split data into Training/Test Sets
# 4. Create a Model
# 5. Train the Model
# 6. Make Predictions
# 7. Evaluate and Improve

import pandas as pd #import pandas module
from sklearn.tree import DecisionTreeClassifier #implements decision tree algorithm
from sklearn.model_selection import train_test_split #for splitting
from sklearn.metrics import accuracy_score #for accuracy
import joblib #for saving and loading models
from sklearn import tree #for visualisation

data = pd.read_csv('music.csv')
data

#no need to clean data, no duplicates or other problems

#train model

# X = data.drop(columns=['genre']) #X what we want to predict
# y = data['genre'] #y 
#                                                                                #80% for training
# model = DecisionTreeClassifier() #create model, apply algorithm tree decision
# model.fit(X,y)

#joblib.dump(model, 'music-recommender.joblib') #save training model
model = joblib.load('music-recommender.joblib') #load model

predictions = model.predict([ [21, 1], [22, 0] ]) #predict this values
predictions

tree.export_graphviz(model, out_file='music-recomender.dot', feature_names=['age', 'gender'], class_names=sorted(y.unique()),label='all', rounded=True, filled=True)

