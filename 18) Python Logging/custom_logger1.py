#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import inspect
import logging

def get_custom_logger(level):
    function_name = inspect.stack()[1][3]
    logger_name = function_name+" logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    
    fileHandler=logging.FileHandler("Supportive_Files/{}.log".format(function_name),mode='a')
    fileHandler.setLevel(level)
    
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger

