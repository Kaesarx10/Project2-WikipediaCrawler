#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests





from urllib.request import urlopen





from bs4 import BeautifulSoup


import re


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


for link in wiki_soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])


