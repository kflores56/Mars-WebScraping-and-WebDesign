from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find('div', class_='content_title')
    news_p = soup.find('div', class_='article_teaser_body')

    # Store data in a dictionary
    article_data = {
        "news_title": news_title,
        "news_p": news_p,
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return article_data