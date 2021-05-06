#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging
logger = logging.getLogger('Studentlogger')
logger.setLevel(logging.DEBUG)


fileHandler=logging.FileHandler("Supportive_Files/Student1.log",mode='w')
fileHandler.setLevel(logging.WARNING)

formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.critical("It is a critical message")
logger.error("It is error message")
logger.warning("It is warning message")
logger.info("It is info message")
logger.debug("It is debug message")

