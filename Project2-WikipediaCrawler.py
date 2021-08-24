#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[4]:


from urllib.request import urlopen


# In[6]:


from bs4 import BeautifulSoup


# In[10]:


wiki_url = urlopen('https://en.wikipedia.org/wiki/Database')


# In[12]:


wiki_url2 = requests.get('https://en.wikipedia.org/wiki/Database').text


# In[11]:


wiki_soup = BeautifulSoup(wiki_url, 'lxml')


# In[13]:


wiki_soup = BeautifulSoup(wiki_url2, 'lxml')


# In[15]:


for link in wiki_soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])


# In[ ]:




