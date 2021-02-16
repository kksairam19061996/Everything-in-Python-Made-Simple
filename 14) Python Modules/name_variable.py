#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def f1():
    if __name__=="__main__":
        print("Direct Execution, Since The code executed as a program hence __name__ :",__name__)
    else:
        print("Indirect Execution, The code executed as a module from some other program with import statement. Hence __name__ :",__name__)
f1() 

