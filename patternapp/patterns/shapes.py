#!/usr/bin/env python
# coding: utf-8

# **To Print Square Pattern with * sumbols**

# In[2]:


def square():
    inp=int(input("Enter n Value:"))
    for i in range(inp):
        print("* "*inp)


# **To print Right Angle Triangle pattern with *
# symbols**

# In[5]:


def right_angle_triangle():
    inp=int(input("Enter n Value:"))
    for i in range(inp):
        for j in range(i+1):
            print('*',end=" ")
        print()     


# **To print Inverted Right Angle Triangle
# pattern with * symbols**

# In[8]:


def inverted_right_angle_triangle():
    inp=int(input("Enter n Value:"))
    for i in range(inp):
        print('*'*(inp-i))
    print()    


# **To print Pyramid pattern with * symbols**

# In[11]:


def pyramid():
    n=int(input("Enter n Value:"))
    for i in range(n):
        print(' '*(n-i-1)+'* '*(i+1))
    print()    


# **To print Inverted Pyramid Pattern with *
# symbols**

# In[13]:


def inverted_pyramid():
    n=int(input("Enter n Value:"))
    for i in range(n):
        print(' '*(i)+'* '*(n-i))
    print()    


# **To print Diamond Pattern with * symbols**

# In[15]:


def diamond():
    n=int(input("Enter n Value:"))
    for i in range(n):
        print(' '*(n-i-1)+'* '*(i+1))
    for i in range(n-1):
        print(' '*(i+1)+'* '*(n-i-1))
    print()
    
diamond()    


# In[ ]:




