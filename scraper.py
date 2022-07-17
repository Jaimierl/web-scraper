import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Plant"

page = requests.get(URL)

#print(page.content)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="mw-body-content mw-content-ltr")

# print(results.prettify())

citation = "citation needed"
    # 'citation needed' is the text we are looking for

all_citations = soup.find_all(text=citation)
    # soup.findAll
    # This will find things with the citation

# print(all_citations)

def get_citations_needed_count(url_string):
    """Takes in a url string and returns an integer."""
    count_citations = len(all_citations)
    print(count_citations)
    return count_citations


def get_citations_needed_report(url_string):
    """Takes in a url string and returns a report string formatted with each citation listed in the order found in paragraphs."""
    report_string = ""

    for found_citation in all_citations:
        parent_text = found_citation.find_parent('p')
        # This finds the parent tag of the full paragraph the citation needed is connected to
        text_only = parent_text.get_text()
        # This should be taking out the text formatting from the paragraphs but is causing an error.
        print (text_only)

        # report_string += paragraph.parent.text

    # return report_string


if __name__ == "__main__":
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)
