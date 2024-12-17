#!/usr/bin/env python
# coding: utf-8

# In[6]:


from add import add
import pytest

def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0



# In[1]:


pytest test_add.py


# In[ ]:




