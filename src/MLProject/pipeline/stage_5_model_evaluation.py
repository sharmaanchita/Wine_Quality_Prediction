from MLProject import logger
from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_evaluation import ModelEvaluation

STAGE_NAME= "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation = ModelEvaluationTrainingPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e    