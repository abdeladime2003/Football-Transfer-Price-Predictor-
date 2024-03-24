import streamlit as st
import pandas as pd
import numpy as np
from dataPreprocessingClass import dataPreprocessing
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import PCA





# Building the basics of the website
st.write("""
# Player Price Prediction

Estimate the **PRICE** of a Player with Machine Learning!
""")

st.sidebar.header("user input parameteres")

def user_input_features():
    name = st.text_input("Enter Player Name", "")
    age = st.sidebar.slider('Age', 16, 40, 20)
    positions = ['Attacking Midfield', 'Central Midfield', 'Centre-Back', 'Centre-Forward',
             'Defensive Midfield', 'Goalkeeper', 'Left Midfield', 'Left Winger', 'Left-Back',
             'Right Midfield', 'Right Winger', 'Right-Back', 'Second Striker']
    position = st.selectbox("Select Player Position", positions) 
    ATT = st.sidebar.slider('Attacking', 1, 100, 50)
    SKI = st.sidebar.slider("Skill", 1, 100, 50)
    MOV = st.sidebar.slider("Movement", 1, 100, 50)
    POW = st.sidebar.slider("Power", 1, 100, 50)
    MEN = st.sidebar.slider("Mentality", 1, 100, 50)
    DEF = st.sidebar.slider("Defending", 1, 100, 50)
    GK = st.sidebar.slider("Goalkeeping", 1, 100, 50)

    data = {
        'name': name,
        'age': age,
        'position': position,
        'ATT': ATT,
        'SKI': SKI,
        'MOV': MOV,
        'POW': POW,
        'MEN': MEN,
        'DEF': DEF,
        'GK': GK,
    }

    index = range(1)
    features = pd.DataFrame(data, index=index)
    return features

user_input = user_input_features()

st.subheader('User input parameters')
st.write(user_input)



# Preprocessing the user data
instance = dataPreprocessing(user_input)
instance.clean_data()
instance.encode_categorical_data()

new_order = ['name', 'age', 'ATT', 'SKI', 'MOV', 'POW', 'MEN', 'DEF', 'GK',
        'position_Attacking Midfield', 'position_Central Midfield',
       'position_Centre-Back', 'position_Centre-Forward',
       'position_Defensive Midfield', 'position_Goalkeeper',
       'position_Left Midfield', 'position_Left Winger', 'position_Left-Back',
       'position_Right Midfield', 'position_Right Winger',
       'position_Right-Back', 'position_Second Striker']
position = user_input.columns[-1]
instance.add_reorder_columns(position, new_order)

user_input = instance.data_frame().copy()




# Reading the training data for the model
df = pd.read_csv(r"C:\Users\Badr Lakhal\Downloads\model_training_data.csv")



# Model trainig section
X = df.drop(["Unnamed: 0", "name", "fee"], axis=1)
pca = PCA(n_components=10)  

X_pca = pca.fit_transform(X)
y = df["fee"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1937)

alphas = [0.001, 0.01, 0.1, 1, 10, 100]
reg = Ridge()
param_grid = {'alpha': alphas}

grid_search = GridSearchCV(reg, param_grid, cv=5, scoring='neg_mean_squared_error')

grid_search.fit(X_train, y_train)

best_reg = grid_search.best_estimator_

# Estimating the player's price
y_pred = best_reg.predict(user_input.drop("name", axis=1))




# Printing the estimated price on the website
st.subheader("Prediction in millions of euros")
st.write(abs(np.round(y_pred)))