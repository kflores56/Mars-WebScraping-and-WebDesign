# Mission to Mars

This project built a web application to scrape various websites for data related to the Mission to Mars and then displays the information in a single HTML page. The following outlines how this was accomplished.

## Step 1 - Scraping

The initial scraping was conducted using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter and saved in a Juypter Notebook. The following outlines what was scraped and provides original sources.

* **NASA Mars News**

    * The latest news title and paragraph text was scraped from the [Mars News Site](https://redplanetscience.com/).

* **Mars Featured Image**

    * Splinter was used to navigate to and scrape the full size feature image from [Space Images Website](https://spaceimages-mars.com). The full url was saved to use for webpage creation. 

* **Mars Facts**

    * Pandas was used to convert data from the [Mars Facts webpage](https://galaxyfacts-mars.com) into a HTML table string.  

* **Mars Hemispheres**

    * Four high resolution images were scraped from a [Mars Hemisphere Website](https://marshemispheres.com/) by using splinter to click each of link to the hemispheres in order to find the image url to the full resolution image. 

    * The image url string for the full resolution hemisphere image and the image title were both saved and added to a dictionary for web development. 

## Step 2 - MongoDB and Flask Application

MongoDB with Flask was used with the goal of creating a new HTML page that displays all of the information that was scraped from the above websites.

* The Jupyter notebook was converted into a Python script and then updated in [scrape_mars.py](https://github.com/kflores56/web-scraping-challenge/blob/main/scrape_mars.py) to scrape the data.  Python dictionary containing all of the scraped data.

* Next, a route called `/scrape`  was created so the  `scrape_mars.py` script could be imported.

  * The returned data was stored in Mongo as a Python dictionary.

## Step 3 - Web Development

*  A root route `/` was created to query the Mongo database and pass the mars data into an HTML template to display the data.

* A template HTML file called `index.html` was created to take the mars data dictionary and display all of the data in the appropriate HTML elements. The following is the final application: 

*Top half of the application*
<img src="https://github.com/kflores56/web-scraping-challenge/blob/main/images/top_pg.png" width="600"/> 

*Bottom half of the application*
<img src="https://github.com/kflores56/web-scraping-challenge/blob/main/images/bottom_pg.png" width="600"/> 

