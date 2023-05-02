from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent)) #It is actually only appending "." to sys.path

import os
import sys
from src.exception import CustomException #In src, there is exception.py file. From there importing CustomException class
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #used to create class variables

@dataclass # (decorator) directly define class variable without using __init__ method
class DataIngestionConfig: # Class is used for input variables
    train_data_path : str=os.path.join("artifact","train.csv") #stores the data_ingestion component output (train.csv) in artifact folder
    test_data_path : str=os.path.join("artifact","test.csv") 
    raw_data_path : str=os.path.join("artifact","data.csv") #how raw data looks
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #creating object of DataIngestionConfig class
        #all the variables of DataIngestionConfig class are stored in ingestion_config variable
        
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            df = pd.read_csv('notebook\data\student.csv')
            logging.info("Dataset read")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #create folder if not exist
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #save raw data in artifact folder
            
            logging.info('Train test split initiated')
            
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingestion completed')
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()