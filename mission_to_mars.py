#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from urllib.request import urlopen


# ## NASA Mars News

# In[2]:


# browser = init_browser()
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = "https://redplanetscience.com/"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

news_title = soup.find('div', class_='content_title').text
news_p = soup.find('div', class_='article_teaser_body').text

# news_data = {
#         "news_title": news_title,
#         "news_p": news_p,
#     }

# Return results
print(news_title)
print(news_p)


# ## JPL Mars Space Images - Featured Image

# In[4]:


url = "https://spaceimages-mars.com/"
browser.visit(url)


# In[5]:


browser.links.find_by_partial_text('FULL').click()


# In[6]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[7]:


relative_image_path = soup.find('img', class_='fancybox-image')["src"]
featured_image_url = url + relative_image_path
featured_image_url


# ## Mars Facts

# In[8]:


url = 'https://galaxyfacts-mars.com/'


# In[9]:


table = pd.read_html(url)
table


# In[10]:


mars_data = table[0]
mars_data.columns = ['Description', 'Mars', 'Earth']
mars_data.set_index('Description', inplace=True)
mars_data.head()


# ## Mars Hemispheres

# In[11]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[12]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")

section = soup.find_all('div', class_='item')

image_urls = []

for items in section:
    # Finding title
    title = items.find('h3').text
    
    # Find link to click for high res photoe, click link
    href = items.find('a', class_='itemLink product-item')['href']
    browser.visit('https://marshemispheres.com/' + href)
    
    # Parse this website and get final link
    partial_href = browser.html
    soup = BeautifulSoup(partial_href, 'html.parser')
    image_link = 'https://marshemispheres.com/' + soup.find('img', class_='wide-image')['src']

    # Add title and final link to dictonary
    image_urls.append({"title" : title, "image_link" : image_link})


# In[13]:


image_urls


# In[14]:


# Close the browser after scraping
browser.quit()

