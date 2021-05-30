#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    def __init__(self,eno,ename,esal,eaddress):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddress = eaddress
    
    def display(self):
        print('Eno:{},EName:{},ESal:{},EAddress:{}'.format(self.eno,self.ename,self.esal,self.eaddress))

