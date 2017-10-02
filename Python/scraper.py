# Simple webscraper that grabs the links from a page.

import requests

def grab_page(url):
    '''Function that grabs a web-page and its content.'''
    page = requests.get(url)
    content = page.text
    return content
 
def grab_next_link(page):
    '''Function to find next link'''
    start_link = page.find('a href=')
    if start_link == -1:
        return None, 0        
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
 
def grab_all_links(page):
    '''Gets all the links from a page and returns them in a list.'''
    links = []
    while True:
        url, endpos = grab_next_link(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
 
links = grab_all_links(grab_page("https://www.amazon.com/"))
 
print(links)