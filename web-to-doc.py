import progressbar
import pypandoc
from urllib.request import urlopen
from bs4 import BeautifulSoup



def collect_website_data(url):
    """
    Takes url string parameter, returns BeautifulSoup object with website content
    """
    index_page = urlopen(url) # HTTP Response
    scrape_data = BeautifulSoup(index_page, "html.parser") # BeatifulSoup Object
    return scrape_data


def get_list_of_category_urls(bs_object, base_url):
    """
    Takes a BeautifulSoup object as parameter, returns a list of urls
    """
    category_a_elements = bs_object.find("div", {"class": "side_categories"}).li.ul.find_all("a")
    category_links = []

    for item in category_a_elements:
        href = base_url + item.get("href")
        category_links.append(href)

    return category_links


def get_category_titles_from_each_page(list_of_urls):
    """
    Takes a list of urls, returns category titles from each visited page
    """
    titles = []

    print('Retrieving data for each category:')
    with progressbar.ProgressBar(max_value=len(list_of_urls)) as bar:
        for counter, url in enumerate(list_of_urls):
            category_page = urlopen(url)
            scrape_data = BeautifulSoup(
                category_page, "html.parser")  # BeatifulSoup Object
            title = scrape_data.h1.text
            titles.append(title)
            bar.update(counter)
    return titles


def apply_markdown_formatting(list_of_records):
    """
    Takes an iterable, returns markdown formatted string
    """
    markdown_string = ""

    for item in list_of_records:
        line = "#" + " " + item + "\n\n"
        markdown_string += line

    print(markdown_string)
    return markdown_string


def get_info_for_each_film(list_of_urls, base_url):
    """
    Takes a list of urls, returns markdown formatted string
    """
    markdown_string = ""

    print('Retrieving film data for each category:')
    with progressbar.ProgressBar(max_value=len(list_of_urls)) as bar:
        for counter, url in enumerate(list_of_urls):
            category_page = urlopen(url)
            scrape_data = BeautifulSoup(
                category_page, "html.parser")
            category = scrape_data.h1.text
            category_md = "#" + " " + category + "\n\n"
            markdown_string += category_md
            links_to_films = scrape_data.find_all("h3")
            links_to_films = [base_url + "catalogue/" +
                              i.a.get("href")[9:] for i in links_to_films]
            for film_link in links_to_films:
                film_page = urlopen(film_link)
                scrape_data = BeautifulSoup(
                    film_page, "html.parser")
                film_title = scrape_data.h1.text
                film_title_md = "##" + " " + film_title + "\n\n"
                markdown_string += film_title_md
                try:
                    description = scrape_data.find(
                        "div", {"id": "product_description"}).next_sibling.next_sibling.text
                    description_md = description + "\n\n"
                    markdown_string += description_md
                except AttributeError as e:
                    markdown_string += '\n\n'
            markdown_string += '\\newpage'
            bar.update(counter)
    return markdown_string


def convert_markdown_to_docx(markdown_string):
    """
    Takes a markdown string, converts it to docx
    """
    filters = ['pandoc-docx-pagebreakpy']
    output = pypandoc.convert_text(
        markdown_string, 'docx', format='md', outputfile="output.docx", filters=filters)
    pass


if __name__ == "__main__":
    BASE_URL = "http://books.toscrape.com/"
    page_data = collect_website_data(BASE_URL)
    links_to_categories = get_list_of_category_urls(page_data, BASE_URL)
    # titles = get_category_titles_from_each_page(links_to_categories)
    # apply_markdown_formatting(titles)
    film_data = get_info_for_each_film(links_to_categories, BASE_URL)
    convert_markdown_to_docx(film_data)
