# Web to Doc


# Task

In my particular case the task was to create a Word document containing prospectus information 

Create a word document from scraped data from the website.

* Identify a landing page that contains a list of links to records you want to store
* Access the page and convert it to a web scraping object
* Identify elements that contain links to the records you wish to store.
* Using a `for` loop, access each element --incomplete


# External libraries

* Pandoc (https://pandoc.org/)


# Python libs installed 

* BeautifulSoup
* Pypandoc
* Progressbar2


# Steps

1. Collect website data
2. Create a list of categories
3. Go through each category page
4. Get Title
5. Bonus create progress bar
6. Pandoc


# Pandoc install steps on linus

1. Go to https://pandoc.org/installing.html
2. Download Pandoc deb package https://github.com/jgm/pandoc/releases/tag/2.11.2
3. Right-click and install package