import pandas as pd  
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression  
from sklearn.metrics import accuracy_score  

iris = load_iris() 

X = iris.data 
y = iris.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)  
model.fit(X_train, y_train) 
y_pred = model.predict(X_test)  
accuracy = accuracy_score(y_test, y_pred) 

print(f'Accuracy: {accuracy:.2f}')  

sample = [[5.1, 3.5, 1.4, 0.2]] 
species_index = model.predict(sample)[0] 
print(f'Predicted species: {iris.target_names[species_index]}')
