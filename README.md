# Web Scraper

## API

This is a web scraper that scrapes a Wikipedia and records which passages need citations.

The web scraper reports the number of citations needed and identifies the cases with the relevant passages (aka the parent element that contains the passage, often a paragraph element).

## Navigation

The module is named scraper.

Function get_citations_needed_count
takes in a url string and returns an integer.

Function get_citations_needed_report
takes in a url string and returns a report string
The returned string is formatted with each citation listed in the order found.


## Resources

See the code for [The Web Scraper](scraper.py) by clicking on the highlighted words!

Worked with Brian Tarte