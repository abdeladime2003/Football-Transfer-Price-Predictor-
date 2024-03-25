 **Uniting Web Scraping, Data Analysis, ML Modeling, and Streamlit Visualization**

Our project endeavors to integrate three key processes essential for data scientists. Firstly, we focus on data acquisition, achieved through web scraping of Transfermarkt and FIFA Stats websites. Secondly, we delve into data manipulation and preprocessing, laying the foundation for constructing a predictive model using techniques like linear regression. Lastly, we embark on deploying our model. To accomplish this, we employ the Streamlit framework to develop an application. This application allows users to interactively adjust features and predict player fees, thereby providing an intuitive and customizable experience.

## Project Structure

The project is organized into the following directories:

1. **python_project**: Contains the main Python code for the project.
   - **step1**: Initial steps of the project.
     - `data_preprocessing.ipynb`: Jupyter Notebook for data preprocessing.
     - `scrap_fifa_stats.ipynb`: Jupyter Notebook for scraping FIFA stats.
     - `scrap_transfer_market.ipynb`: Jupyter Notebook for scraping transfer market data.
      - `data`:  comprises four CSV files, each containing specific datasets. Firstly, there's "transfert_market.csv," housing data obtained from the Transfermarkt website. Secondly, "stats.csv" holds data sourced from the FIFA Stats website. Thirdly, "names.csv" contains player names, serving as a crucial column facilitating the merging of the two datasets. Lastly, "model_training_data.csv" encompasses data subjected to cleaning, preprocessing, and feature engineering, ready for model training.
   - **step2**: Intermediate steps of the project.
     - `Final_Model.ipynb`: Jupyter Notebook for the final model.
   - **step3**: Final steps of the project.
     - `dataPreprocessingClass.py`: Python file for data preprocessing class.
     - `Video.mp4`: Video file demonstrating the final result.
     - `webSite_interface.py`: Python file for website interface.

2. **virtuel_environement**: Virtual environment for the project.
   - `pyvenv.cfg`: Configuration file for the virtual environment.
   - `requirements.txt`: File containing required dependencies.

## Project Demonstration

For a demonstration of the project, please refer to the following Google Drive link:
[Project Demonstration](https://drive.google.com/drive/folders/1GaEaL5FcIDnKLFAjXfP5KcYzHhOQi2np?usp=sharing)

## Usage

To use the project, follow these steps:
1. **Clone the repository** : git clone https://github.com/votre-nom-utilisateur/projet_baina.git
2. **Install virtual environment** : python -m venv venv
3. **Activate  virtual environment** : venv\Scripts\activate
4. **Install  dependencies** :pip install -r requirements.txt
5. Navigate to the desired step within the `python_project` directory.
6. Execute the relevant scripts or notebooks.

## Dependencies

Ensure you have installed the required dependencies listed in `virtuel_environement/requirements.txt` before running the project.


## for additional details, please refer to the "Project Demonstration" file, which includes the video presentation.
