import numpy as np
import pandas as pd



class dataPreprocessing:
    file_paths = {'transfer_market': 'transfer_market.csv', 'stats': 'stats.csv'}
    output_path = 'model_training_data.csv'
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
        self.dataF['market_value'] = self.dataF['market_value'].apply(lambda value: float(value[:-1]) * 1000 if isinstance(value, str) and value[-1] == 'k' else pd.to_numeric(value))
        self.dataF['age'] = self.dataF['age'].astype(int)



        self.dataF = self.dataF.reset_index(drop=True)
    
    def group_categories(self, column_list):
        for column in column_list:
            counts = self.dataF[column].value_counts()
            categories_autre = counts[counts < 4].index.tolist()
            self.dataF[column] = self.dataF[column].apply(lambda x: 'Autre' if x in categories_autre else x)


    def encode_categorical_data(self):
        colonnes_categorielles_1 = ['league_from', 'league_to']
        colonnes_categorielles_2 = ['club_to', 'club_from']
        
        self.group_categories(colonnes_categorielles_1)
        self.group_categories(colonnes_categorielles_2)

        self.df_encoded = pd.get_dummies(self.dataF, columns=colonnes_categorielles_1 + colonnes_categorielles_2 + ['position'] + ['loan'], dtype=int)


    def save_data(self):
        self.df_encoded.to_csv('trainig_example.csv')


    def df(self):
      return self.df_encoded








user_input = data_dict = {
    "name": "Erling Haaland",
    "position": "Centre-Forward",
    "age": 21,
    "market_value": 150.0,
    "league_from": "Bundesliga",
    "club_from": "Borussia Dortmund",
    "league_to": "Premier League",
    "club_to": "Manchester City",
    "loan": False,
    "ATT": 76.0,
    "SKI": 70.0,
    "MOV": 82.0,
    "POW": 86.0,
    "MEN": 75.0,
    "DEF": 72.0,
    "GK": 10.0,
}


index = range(1)
df = pd.DataFrame(user_input, index=index)


preprocessor = dataPreprocessing(df)
preprocessor.clean_data()
preprocessor.encode_categorical_data()
preprocessor.save_data()


print(preprocessor.df())