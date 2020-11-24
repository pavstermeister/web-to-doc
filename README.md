# Web to Doc

A python script that scrapes content from a web page, converts it to a Markdown string and outputs a Word document.

Using Python 3.6.12.

**Steps**

1. Collect data from index page
2. Scrape a list of links to all film category pages
3. Visit each category page and scrape a list of films in that category
4. Visit each film in each category and scrape relevant data for that film
5. Format collected data into a markdown string
6. Store collected data as a Word document

Check out the associated article on Dev.to -- https://dev.to/pavstermeister/from-web-to-word-using-python-4gd9


# Dependencies

## External dependencies

* [Pandoc document converter](https://pandoc.org/)


## External Python libraries used

* [BeautifulSoup 3.2.2](https://pypi.org/project/BeautifulSoup/)
* [pypandoc 1.5](https://pypi.org/project/pypandoc/)
* [pandoc-docx-pagebreak 0.0.2](https://pypi.org/project/pandoc-docx-pagebreak/)
* [progressbar2 3.53.1](https://pypi.org/project/progressbar2/)
