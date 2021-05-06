#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# demo.py module will be imported later
import inspect
def getInfo():
    print(inspect.stack()[1])
    print()
    print()
    print("Caller Module: ",inspect.stack()[1][1])
    print("Caller Function Name: ",inspect.stack()[1][3])

