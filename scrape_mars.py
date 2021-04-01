
# Import dependecies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from urllib.request import urlopen



def scrape():

#### NASA Mars News ####

    # browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text


#### JPL Mars Space Images - Featured Image ####

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    browser.links.find_by_partial_text('FULL').click()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    relative_image_path = soup.find('img', class_='fancybox-image')["src"]
    featured_image_url = url + relative_image_path

#### Mars Facts ####

    url = 'https://galaxyfacts-mars.com/'

    table = pd.read_html(url)
    table

    mars_data = table[0]
    mars_data.columns = ['Description', 'Mars', 'Earth']
    mars_data.set_index('Description', inplace=True)
        
    data = mars_data.to_html()

#### Mars Hemisphere Images ####

    url = 'https://marshemispheres.com/'
    browser.visit(url)

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


### Store data in a dictionary ###

    mars_info = { 
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "mars_data": data,
        "image_urls": image_urls
        }

    # Close the browser after scraping
    browser.quit()

    # Return dictionary 
    return mars_info
