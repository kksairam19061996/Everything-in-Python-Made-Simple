#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[loggers]
keys=root,demologger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_demologger]
level=DEBUG
handlers=consoleHandler
qualname=demoLogger

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format = %(asctime)s:%(name)s:%(levelname)s:%(message)s
datefmt = d/%m/%Y %I:%M:%S %p

