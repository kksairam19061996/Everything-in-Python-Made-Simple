#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[loggers]
keys=root,demologger

[handlers]
keys=fileHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=fileHandler

[logger_demologger]
level=DEBUG
handlers=fileHandler
qualname=demoLogger

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=sampleFormatter
args=("Supportive_Files/test123.log",'w')

[formatter_sampleFormatter]
format = %(asctime)s:%(name)s:%(levelname)s:%(message)s
datefmt = %d/%m/%Y', '%I:%M:%S %p

