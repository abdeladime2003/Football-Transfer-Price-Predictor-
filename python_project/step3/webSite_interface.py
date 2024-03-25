import streamlit as st
import pandas as pd
import numpy as np
from python_project.step3.dataPreprocessingClass import dataPreprocessing
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import PCA
st.title("Football Transfer Price Predictor 💰")
st.video(r"whatsapp-video-2024-03-22-at-171246-ab2a28a1_4aDFAO4r.mp4", start_time=0)  # Add loop=True for infinite looping
st.write(" "*30 + "**Welcome! Please enter your name and click the button below to proceed:**" + " "*30)
user_name = st.text_input("Enter Your Name", "")

if st.button("Continue"):
    st.sidebar.header("User Input Parameters")
    def user_input_features():
        age = st.sidebar.slider('Age', 16, 40, 20)
        positions = ['Attacking Midfield', 'Central Midfield', 'Centre-Back', 'Centre-Forward',
                 'Defensive Midfield', 'Goalkeeper', 'Left Midfield', 'Left Winger', 'Left-Back',
                 'Right Midfield', 'Right Winger', 'Right-Back', 'Second Striker']
        position = st.sidebar.selectbox("Select Player Position", positions) 
        ATT = st.sidebar.slider('Attacking', 1, 100, 50)
        SKI = st.sidebar.slider("Skill", 1, 100, 50)
        MOV = st.sidebar.slider("Movement", 1, 100, 50)
        POW = st.sidebar.slider("Power", 1, 100, 50)
        MEN = st.sidebar.slider("Mentality", 1, 100, 50)
        DEF = st.sidebar.slider("Defending", 1, 100, 50)
        GK = st.sidebar.slider("Goalkeeping", 1, 100, 50)

        data = {
            'name': user_name,
            'age': age,
            "position": position,
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

    st.subheader('📊 Player Statistics Input')
    st.write(user_input)
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

    df = pd.read_csv(r"C:\Users\Lenovo\Desktop\projet_baina\nouveau_projet\python_project\step1\data\model_training_data.csv")

    # Model training section
    X = df.drop(["Unnamed: 0", "fee", "name", "market_value"], axis=1)
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

    # Predicting the estimated price
    y_pred = best_reg.predict(user_input.drop("name", axis=1))

    st.subheader("Prediction in millions of euros 💶 ")
    st.write(abs(np.round(y_pred)))