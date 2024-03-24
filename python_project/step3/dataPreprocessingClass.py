import numpy as np
import pandas as pd



class dataPreprocessing:
    file_paths = {'transfer_market': 'transfer_market.csv', 'stats': 'stats.csv'}
    output_path = 'model_training_data.csv'
    L = ['position_Attacking Midfield', 'position_Central Midfield',
       'position_Centre-Back', 'position_Centre-Forward',
       'position_Defensive Midfield', 'position_Goalkeeper',
       'position_Left Midfield', 'position_Left Winger', 'position_Left-Back',
       'position_Right Midfield', 'position_Right Winger',
       'position_Right-Back', 'position_Second Striker']


    def __init__(self, df):
        self.dataF = df.copy()



    @staticmethod
    def handle_k_values(value):
        try:
            return float(value)
        except ValueError:
            if value[-1] == 'k':
                return float(value[:-1]) * 1000
            else:
                return np.nan


    def clean_data(self):
        #self.dataF['market_value'] = self.dataF['market_value'].apply(lambda value: float(value[:-1]) * 1000 if isinstance(value, str) and value[-1] == 'k' else pd.to_numeric(value))
        self.dataF['age'] = self.dataF['age'].astype(int)

        self.dataF = self.dataF.reset_index(drop=True)

        #self.data = self.dataF.drop(columns=["league_from", "club_from", "league_to", "club_to", "loan"])
    
    def group_categories(self, column_list):
        for column in column_list:
            counts = self.dataF[column].value_counts()
            categories_autre = counts[counts < 4].index.tolist()
            self.dataF[column] = self.dataF[column].apply(lambda x: 'Autre' if x in categories_autre else x)


    def encode_categorical_data(self):
     #   colonnes_categorielles_1 = ['league_from', 'league_to']
      #  colonnes_categorielles_2 = ['club_to', 'club_from']
       
        #self.group_categories(colonnes_categorielles_1)
        #self.group_categories(colonnes_categorielles_2)

        self.df_encoded = pd.get_dummies(self.dataF, columns=['position'], dtype=int)


    def add_reorder_columns(self, position, new_order: list):
        for value in self.L:
            if value != position:
                self.df_encoded[value] = 0

        self.df_encoded = self.df_encoded.reindex(columns=new_order)


    def data_frame(self):
      return self.df_encoded




