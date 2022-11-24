#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. write a python program to convert a srting to lower case.

x="HEMANTH"
print(x.lower())


# In[6]:


# 2.write a python program to convert only even index charecters to lower case.

str1=input()
x=" "
for char in range(len(str1)):
    if char%2==0:
        x=x+str1[char].lower()
    else:
        x=x+str1[char].upper()
print(x)


# In[ ]:





# In[3]:


# 3.write a python program to convert only odd index charecters to lower case.

str2=input()
p=" "
for char in range(len(str2)):
    if char%2==0:
        p=p+str2[char].upper()
    else:
        p=p+str2[char].lower()
print(p)


# In[8]:


# 4.write a program to convert only odd index charecter to upper case.

str3=input()
y=" "
for char in range(len(str3)):
    if char%2==0:
        y=y+str3[char].lower()
    else:
        y=y+str3[char].upper()
print(y)
        


# In[10]:


# 5.write a program to convert only even index charecter to upper case.

str4=input()
x=" "
for char in range(len(str4)):
    if char%2==0:
        x=x+str4[char].upper()
    else:
        x=x+str4[char].lower()
print(x)


# In[12]:


# 6.write a python program to where you have dofferent variable which contains your name,sex,age,phone no,father name and  mother name .and by using this variable create a variable named bio-data where you will use all this variable

name=input("Enter your name ")
sex=input("Enter your sex ")
age=input("Enter your age ")
phoneno=input("Enter your phone no ")
father_name=input("Enter your father_name ")
mother_name=input("Enter your mother_name ")
bio_data= "My name is {} my sex is {} my age is {} my phoneno is {} my father_name is {} my mother_name is {}"
bio_data.format(name,sex,age,phoneno,father_name,mother_name)


# In[14]:


# 7.write a program to count how many times"@" occured

l=input("enter your list")
l.count("@")


# In[15]:



# 8.write a programm to get only names from the string "name1.@gmail.com,name2.@gmail.com,name3.@gmail.com" output-name1,name2,name3

s1="name1.@gmail.com,name2.@gmail.com,name3.@gmail.com" 
s1=s1.split( ".")
print(s1[0],s1[2][4:],s1[4][4:])


# In[17]:


# 9.Given a string of odd lenthg greater that 9,return a new string made of the middle three characters of a given

name=input("")
b=int(len(name)/2)
name[b-1:b+2]


# In[18]:


# 10.write a python program to insert a 2 string in middle of 1 string

str1=input("")
str2=input("")
print(str1[:len(str1)//2:]+str2+str1[len(str1)//2:])


# In[19]:


# 11.write aprogram to remove vowels from the entire alphabets

vowels=["a","e","i","o","u","A","E","I","O","U"]
name=input()
a=""
for k in name:
    if k not in vowels:
        a+=k
print(a)


# In[ ]:




