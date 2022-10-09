import pandas as pd

columns = ["Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape", "Marginal Adhesion","Single Epithelial Cell Size", "Bare Nuclei","Bland Chromatin ", "Normal Nucleoli ","Mitoses","class"]
df = pd.read_csv('breast-cancer-wisconsin.data',names = columns)
df

#Nombramos las columnas de nuestros features
df_x = df[["Clump Thickness","Uniformity of Cell Size","Uniformity of Cell Shape", "Marginal Adhesion","Single Epithelial Cell Size", "Bare Nuclei","Bland Chromatin ", "Normal Nucleoli ","Mitoses"]]

#Nombramos nuestra columna de clases 
df_y = df[["class"]]
df_y.head()

#Dividimos nuestro dataset en train y test data

df_x_train = df_x[:-20]
df_x_test = df_x[-20:]
df_y_train = df_y[:-20]
df_y_test = df_y[-20:]

import numpy as np
from sklearn.tree import DecisionTreeClassifier

#Definimos la profundidad de nuestro arbol
tree_clf = DecisionTreeClassifier(max_depth = 6)
tree_clf.fit(df_x_train,df_y_train)

print("tree classiefier configuration")
tree_clf

#Eplicamos las clases con sus definiciones
print(""" #class 2 for benign, 
#class 4 for malignant""")

#Probamos el arbol con un ejemplo 
#le damos los 9 valores de x para que nos devuelva y 

probs = tree_clf.predict_proba([[10,5,5,3,6,7,7,10,1]])
print("probability of class for query",[[10,5,5,3,6,7,7,10,1]],probs)

pred =  tree_clf.predict([[10,5,5,3,6,7,7,10,1]])
print("prediction of class for query",[[10,5,5,3,6,7,7,10,1]],pred)

from sklearn.metrics import accuracy_score
y_pred_rf= tree_clf.predict(df_x_test)
#vemos cuál es el nivel de presicion
print("tree score", accuracy_score(df_y_test, y_pred_rf))

df_x_test.columns[:]
df_y_test.head

from sklearn import tree
import graphviz

# dot is a graph description language
dot = tree.export_graphviz(tree_clf, out_file=None, 
                           feature_names=df_x_test.columns[:],
                           class_names=["benign","malignant"],
                           filled=True, rounded=True,  
                           special_characters=True)

# we create a graph from dot source using graphviz.Source
graph = graphviz.Source(dot) 
graph

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

#Hcemos un forest y checamos la presicion de resultados
rnd_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=5, n_jobs=-1, random_state=42)
rnd_clf.fit(df_x_train, df_y_train)
y_pred_rf= rnd_clf.predict(df_x_test)
print("random forest", accuracy_score(df_y_test, y_pred_rf))

print(rnd_clf)

#definimos una funcion para poder hacer calculos independientes al dataset
def comeon(let): 
  print(""" #class 2 for benign, 
  #class 4 for malignant""")

  probs = tree_clf.predict_proba(let)
  print("probability of class for query : ", probs)
  

  pred =  tree_clf.predict(let)
  if pred == 4:
    print("prediction of class for query : ",pred," --> malignant")
  else :
    print("prediction of class for query : ",pred," --> benign")

#framework
print("characteristics : \n 1 Clump Thickness \n 2 Uniformity of Cell Size \n 3 Uniformity of Cell Shape \n 4 Marginal Adhesion \n 5 Single Epithelial Cell Size \n 6 Bare Nuclei \n 7 Bland Chromatin \n 8 Normal Nucleoli \n 9 Mitoses")
#let = [[10,5,5,3,6,7,7,10,1]]

sd = [[input("Valor: " ) for x in range(9)]]


#10,5,5,3,6,7,7,10,1
print(sd)
comeon(sd)
