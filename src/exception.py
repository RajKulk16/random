import sys # Any exception that is being controlled, sys will have that information.
import logging
from src.logger import logging

def error_message_detail(error,error_detail:sys): # Here, error_detail is present in sys module.
    _,_,exc_tb=error_detail.exc_info()
    # First 2 return values are not required, so we are using _.
    # 3rd return value tells information like on which file the exception occurred, on which line, etc.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in file {} occurred on line {} with error {}".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    
# Whenever error occurs, we will call this function.

class CustomException(Exception):
    def __init__(self, error_message,error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    