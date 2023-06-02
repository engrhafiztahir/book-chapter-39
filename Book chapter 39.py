#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Code of list of dictionary
customers = [
{
"customer id": 0,
"first name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
},
{
"customer id": 1,
"first name":"Ann",
"last name": "Sattermyer",
"address": "PO Box 1145",
},
{
"customer id": 2,
"first name":"Jill", 
"last name": "Somers",
"address": "3 Main St.",
},
]

a = len(customers)
print(a)


# In[10]:


customers = {
0:
    {
"first name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
    },
1:
    {
"first name":"Ann",
"last name": "Sattermyer",
"address": "PO Box 1145",
    },
2:    
    {
"first name":"Jill", 
"last name": "Somers",
"address": "3 Main St.",
    },
}

a = len(customers)
print(a)
print(customers[2])


# In[ ]:




