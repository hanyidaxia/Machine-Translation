#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import torch
import tensorflow
import keras


# In[40]:


import numpy as np


# In[41]:


with open("J:/machine_translation/modelA.losses") as fileA:
    a = fileA.readlines()
    print(len(a))
    


# In[42]:


with open("J:/machine_translation/modelB.losses") as fileB:
    b = fileB.readlines()
    print(len(b))


# In[43]:


import xlwt


# In[44]:


workbook = xlwt.Workbook(encoding = 'UTF-8')


# In[45]:


import matplotlib.pyplot as plt


# In[46]:


print(a)
print(b)


# In[53]:


idx = 5
idx_a = []
prob_a = []
for _ in range( len( a ) ):
    idx_a.append( idx )
    if _ % 2 == 1:
        idx += 5
    len_pre = len( str( idx ) )
    prob_a.append( float( a[_][len_pre:-1] ) )
print( list( zip( idx_a, prob_a ) ) )

idx = 5
idx_b = []
prob_b = []
for _ in range( len( b ) ):
    idx_b.append( idx )
    if _ % 2 == 1:
        idx += 5
    len_pre = len( str( idx ) )
    prob_b.append( float( b[_][len_pre:-1] ) )
print( list( zip( idx_b, prob_b ) ) )


# In[56]:


len(idx_a)
for j in range(len(idx_a)):
    if (j%2) != 0:
        c = prob_a[j]
        prob_a[j] = prob_b[j]
        prob_b[j] = c
        


# In[27]:


# a_epoc = []
# a_loss = []
# for i in a:
#     a_epoc.append(int(i.split(".")[0]))
#     a_loss.append(float(i.split(" ")[1].split("\n")[0]))


# In[34]:


# b_epoc = []
# b_loss = []
# for j in b:
#     b_epoc.append(int(j.split(" ")[0]))
#     b_loss.append(float(j.split(" ")[1].split("\n")[0]))


# In[65]:


print(prob_a[0], prob_b[0])
print(prob_a[1], prob_b[1])
a_nll = []
a_ce = []
idx_ou = []
idx_ji = []
b_nll = []
b_ce = []
for j in range(len(idx_a)):
    if (j%2) == 0:
        a_nll.append(prob_a[j])
        b_ce.append(prob_b[j])
        idx_ou.append(idx_a[j])
    else:
        a_ce.append(prob_a[j])
        b_nll.append(prob_b[j])
        idx_ji.append(idx_a[j])


# In[77]:


a_pic_nll = plt.plot(idx_ou, a_nll,  label = "NLL loss")
a_pic_ce = plt.plot(idx_ji, a_ce, label =  "CE loss" )

plt.legend()
plt.xlabel("epoch")
plt.ylabel("loss")


# In[78]:


b_pic_nll = plt.plot(idx_ji, b_nll,  label = "NLL loss")
b_pic_ce = plt.plot(idx_ou, b_ce, label =  "CE loss" )
plt.legend()
plt.xlabel("epoch")
plt.ylabel("loss")


# In[36]:


print(b_epoc)


# In[37]:


b_pic = plt.plot(b_epoc, b_loss)
plt.show(b_pic)


# In[ ]:




