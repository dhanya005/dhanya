#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT-1

# In[5]:


#task1 #program2


l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


# In[14]:


#task1 #program3

fname=input('first name\n')
lname=input('last name\n')
fn=fname[::1]
ln=lname[::1]
print(ln,'',fn)


# In[15]:


#task1 #program4

pi=3.142
r=6
v=4/3*3.142*r*r*r
print('the volume of speare',v)


# In[73]:


#task2 #program1

values=input('enter th comma separated numbers\n')
list=values.split(',')
print('list',list)


# In[90]:


#task2 #program2
n=5;
for i in range(5):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[52]:


#task2 #program3

string=input('enter the string to reverse\n')
s=string[::-1]
print(s)


# In[88]:


#task2 #program4

print('WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN, !\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\t\tand to secure to all its citizens')


# In[ ]:





# In[ ]:




