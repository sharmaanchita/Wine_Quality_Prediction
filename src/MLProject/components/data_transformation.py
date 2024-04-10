import os 
from MLProject import logger
from sklearn.model_selection import train_test_split
from MLProject.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config #Instance access the passed configuration data

  #data is already cleaned up thus no need for EDA & model cycles


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        #default 0.75,0.25 split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)