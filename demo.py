from src.logger import logging


#logging.debug("This is a debug message.")
#logging.info("This is an info message.")
#logging.warning("This is a warning message.")
#logging.error("This is an error message.")
#logging.critical("This is a critical message.")


from src.logger import logging
from src.exception import MyException
import sys

#try:
    #### raise MyException(e, sys) from e


from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()