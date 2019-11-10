#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[9]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[10]:



url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[11]:


browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[13]:


slide_elem = soup.select_one('ul.item_list li.slide').find("div", class_='content_title')



# In[14]:


most_recent_title = slide_elem.find("div", class_='content_title').get_text()
most_recent_title


# In[15]:


most_recent_paragraph = slide_elem.find('div', class_="article_teaser_body").get_text()
most_recent_paragraph


# # JPL Mars Space Images - Featured Image

# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(img_url)
html = browser.html
soup = BeautifulSoup(html, 'lxml')


# In[ ]:


image_results = soup.find_all('div', class_ = "carousel_items")


# In[ ]:


for image_result in image_results:
    image = image_result.find('article',class_='carousel_item')
    print(image)
featured_image = image['style'].split("'")[1]
featured_image_url = "https://www.jpl.nasa.gov"+ featured_image


# In[ ]:


featured_image_url


# # Mars Weather

# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'lxml')


# In[ ]:


posts = soup.find_all('div', class_='js-tweet-text-container')


# In[ ]:


weather_of_Mars = []
for post in posts:
    weather = post.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    weather_of_Mars.append(weather)
weather_of_Mars


# In[ ]:


mars_weather = weather_of_Mars[0]
print(mars_weather)


# # Mars Facts

# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://space-facts.com/mars/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'lxml')


# In[ ]:


tables = soup.find_all('table', class_='tablepress tablepress-id-p-mars')


# In[ ]:


url='https://space-facts.com/mars/'
tables = pd.read_html(url)
tables


# In[ ]:


df=tables[0]
df


# In[ ]:


Mars_df = df.rename(columns={'0': 'Mars Facts',
                          'Mars': 'Value'})
Mars_df


# In[ ]:


html_table = Mars_df.to_html('table.html')


# # Mars Hemispheres

# In[ ]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'lxml')


# In[ ]:


results = soup.find_all('div', class_='description')


# In[ ]:


titles = []
image_urls = []
hemisphere_image_urls = []

for result in results:
    title = result.find('h3').text
    
    image = result.find('a', class_ ='itemLink product-item')['href']
    image_url = url + image
    
    titles.append(title)
    image_urls.append(image_url)
    hemisphere_image_urls.append({'title':title,
                                  'image_url':image_url})
    print(title)
    print(image_url)
    print('------------------------------------------------------------------')
    


# In[ ]:


hemisphere_image_urls


# In[ ]:


mars_info={"news_title":most_recent_title,
           "news_paragraph":most_recent_paragraph,
           "featuredimage_url":featured_image_url,
           "marsweather":mars_weather,
           "marsfacts":html_table,
           "hemisphereimage_urls":hemisphere_image_urls  
          }
print(mars_info)


# # Store mars_info in MongoDB

# In[ ]:


import pymongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[ ]:


db = client.MarsDB


# In[ ]:


mars = db.mars.find()
for info in mars:
    print(info)


# In[ ]:


db.mars.insert_one(
          {"news_title":most_recent_title,
           "news_paragraph":most_recent_paragraph,
           "featuredimage_url":featured_image_url,
           "marsweather":mars_weather,
           "marsfacts":html_table,
           "hemisphereimage_urls":hemisphere_image_urls
          }
)


# In[ ]:




