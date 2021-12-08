#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[2]:


lst1  = [1234, 4567, 1343, 1224, 1454]


# In[3]:


arr = np.array(lst1)
print(type(arr))
print(arr)


# In[4]:


print(arr.shape)


# In[5]:


list1 = [534, 543, 874, 125, 812]
list2 = [453, 325, 264, 258, 287]
list3 = [998, 894, 345, 248, 934]


arr1 = np.array([list1, list2, list3])

print(type(arr1))
print(arr1)


# In[6]:


print(arr1.shape)


# In[7]:


arr1.reshape(5,3)


# In[8]:


import array


# In[9]:


arr = array.array('i', [101,102,103,104,105])
print(arr[2])


# In[10]:


for i in arr:
    print(i)


# In[11]:


for i in range(len(arr)):
    print('Index no:', i,'Element:', arr[i])


# In[12]:


n = len(arr)
i = 0
while i<n:
    print(arr[i])
    i += 1


# In[13]:


arr.append(106)
print(arr)


# In[14]:


arr1 = array.array('i', [])

n = int(input("Enter the no. of elements: "))

for i in range(n):
    e = int(input("Enter the elements: "))
    arr1.append(e)

print("Your Final Array is:", arr1)


# In[15]:


n = int(input("Enter the no. of elements: "))

i = 0
while i < n:
    e = int(input("Enter the element: "))
    arr1.append(e)
    i += 1
    
print("Your Final Array is:", arr1)


# In[16]:


nparr = np.array([101,102,103,104,105])

for i in range(len(nparr)):
    print('Index no:', i,'Element:', nparr[i])


# In[17]:


lsarr = np.linspace(1, 10, 5, dtype='int')
print(lsarr)


# In[20]:


narr = np.zeros(n, dtype=int)
x = int(input("Enter no. of elements: "))

for i in range(x):
    e = int(input("Enter the element: "))
    narr[i] = e

print("Your array is: ", narr)


# In[3]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a+b
print(c)


# In[4]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a-b
print(c)


# In[5]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a*b
print(c)


# In[ ]:




