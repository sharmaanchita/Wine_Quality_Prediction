from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path   
    

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path:Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    alpha:float
    l1_ratio: float
    target_column: str
    model_name: str
    train_data_path: Path
    test_data_path: Path
    root_dir: Path