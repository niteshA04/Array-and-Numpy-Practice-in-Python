#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[18]:


narr = np.zeros(n, dtype=int)
x = int(input("Enter no. of elements: "))

for i in range(x):
    e = int(input("Enter the element: "))
    narr[i] = e

print("Your array is: ", narr)


# In[19]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a+b
print(c)


# In[20]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a-b
print(c)


# In[21]:


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = a*b
print(c)


# In[22]:


nparray = np.array([[1,2,3],[4,5.,6],[7,8,9],[10,11,12]], dtype='int')
nparray


# In[23]:


nparray.size


# In[24]:


nparray.reshape(3,4)


# In[25]:


nparray.reshape(1,12)


# In[26]:


nparray.reshape(12,1)


# In[27]:


nparray.T


# In[28]:


array_1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
array_1


# In[29]:


array_a = array_1.reshape(2,8)
array_a


# In[30]:


array_1.T


# In[31]:


print(array_1[0,3])
print(array_1[2,2])
print(array_1[0,-1])
print(array_1[2,-2])


# In[32]:


print(array_1[:,1])


# In[33]:


array_2 = np.zeros((3,3))
array_2


# In[34]:


arr1 = np.ones((3,3))
arr1


# In[35]:


arr2 = np.full((3,3),5)
arr2


# In[36]:


arr3 = np.random.random((3,3))
arr3


# In[37]:


row_1 = [1,2,3,4,5]
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]


# In[38]:


arr_a = np.array([row_1,row_2,row_3,row_4,row_5])
arr_a


# In[39]:


print(arr_a[:,2:4])


# In[40]:


greater_than_ten = arr_a > 10
greater_than_ten


# In[41]:


print(arr_a[greater_than_ten])


# In[42]:


drop_under_10 = np.where(arr_a > 10, arr_a, 0)
drop_under_10


# In[43]:


drop_under_10_and_20 = np.logical_and(arr_a > 10, arr_a < 20)
drop_under_10_and_20


# In[44]:


print(arr_a[drop_under_10_and_20])


# In[45]:


sam_arr = np.arange(0, 100, 5)
sam_arr


# In[46]:


print(sam_arr.size)
sam_arr_reshape = sam_arr.reshape((4,5))
sam_arr_reshape


# In[47]:


print(sam_arr_reshape[:,-1])


# In[48]:


array_above_50 = np.where(sam_arr_reshape> 50, sam_arr_reshape, 0)
array_above_50


# In[49]:


array_above_50 = sam_arr_reshape[sam_arr_reshape > 50]
array_above_50


# In[50]:


array_above_50 = sam_arr_reshape[sam_arr_reshape >= 50]
array_above_50


# In[51]:


print(array_above_50[0:len(array_above_50):2])


# In[52]:


print(sam_arr_reshape[:, 0:5:2])


# In[53]:


print(np.where(sam_arr_reshape>50, sam_arr_reshape, -1))


# In[54]:


print(np.where(sam_arr_reshape>50, sam_arr_reshape*2, -1))


# In[55]:


array_b = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3]])
array_c = np.array([0,1,2,3])
array_d = np.array([[1], [2], [3]])

