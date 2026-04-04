import sys
from src.loggers import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{error}]"
    
    return error_message
    
class CustomException(Exception):#inheriting exception class 
    def __init__(self, error_message, error_detail: sys): #constructor 
        super().__init__(error_message) #calling parent class constructor
        self.error_message = error_message_detail(error_message, error_detail=error_detail) 
        #here we are overriding the actual error message in the real excpetion class
    def __str__(self): 
        return self.error_message
    # rewriting error in our custom way
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e :
        logging.info("Divide by zero")
        raise CustomException(e,sys)