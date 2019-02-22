
# coding: utf-8
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests


executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=True)

url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = bs(html, "html.parser")


# # mars headlines
def title():

    return soup.title.text


def headlines():
# # mars headlines

    names = soup.find_all('a')
    # A blank list to hold the headlines
    headlines = []
    for a in names:
        # If td element has an anchor...
        if (a.a):
            # And the anchor has non-blank text...
            if (a.a.text):
                # Append the td to the list
                headlines.append(names)

    return headlines



def Latest_title_text():
    #two variables created storing the latest title and the text for the latest title
    Latest_titles = soup.find("div", class_="content_title").text
    print(Latest_titles)

    Latest_titles_text = soup.body.find(class_='rollover_description_inner').text.strip()
    return Latest_titles_text




'''def boomerang1(browser):
    # # splinter - pull jpg image
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    browser.click_link_by_id('full_image')
    pic_url = browser.html
    soup2 = bs(pic_url, "html.parser")
    boomerang = soup2.find(class_="fancybox-image")
    boomerang1 = boomerang.attrs['src']

    return boomerang1'''


def weath_tweet(browser):
    # # pull twitter weather data
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html3 = browser.html
    soup3 = bs(html3, "html.parser")
    tweet_attrs = {'class':'tweet', 'data-name':'Mars Weather' }
    weath_tweet = soup3.body.find(attrs=tweet_attrs).text.replace('\n', '')

    return weath_tweet



def facts(browser):
    # # mars facts
    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)
    html4 = browser.visit(url4)
    html4 = browser.html
    soup4 = bs(html4, 'html.parser')

    facts = soup4.body.find(id='tablepress-mars').text.replace('\n', '')

    return facts



# # hemispheres
# visit the page
url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)
html5 = browser.visit(url5)
html5 = browser.html
soup5 = bs(html5, 'html.parser')


def hemi1a(browser):
    url5 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)

    browser.click_link_by_partial_text('Cerberus')
    pic_url5 = browser.html
    soup_pic = bs(pic_url5, "html.parser")
    hemi1 = soup_pic.find('div', class_ = 'downloads')
    hemi1a = hemi1.find('a').attrs['href']

    return hemi1a



def hemi2a(browser):
    # #hemi2
    browser.click_link_by_partial_text('Schiaparelli')
    pic_url5b = browser.html
    soup_picB = bs(pic_url5b, "html.parser")
    hemi2 = soup_picB.find('div', class_ = 'downloads')
    hemi2a = hemi2.find('a').attrs['href']

    return hemi2a



def hemi3a(browser):
    # #hemi3
    browser.click_link_by_partial_text('Syrtis')
    pic_url5c = browser.html
    soup_picC = bs(pic_url5c, 'html.parser')
    hemi3 = soup_picC.find('div', class_ = 'downloads')
    hemi3a = hemi3.find('a').attrs['href']

    return hemi3a



def hemi4a(browser):
    # #hemi4
    browser.click_link_by_partial_text('Valles')
    pic_url5d = browser.html
    soup_picd = bs(pic_url5d, 'html.parser')
    hemi4 = soup_picd.find('div', class_ = 'downloads')
    hemi4a = hemi4.find('a').attrs['href']

    return hemi4a



def scrape():

    browser = Browser("chrome", **executable_path, headless=True)

    scrape_dict = {
        "news_title": title(),
        "headline_description": Latest_title_text(),
        #"feature_image":  boomerang1(browser),
        "weather":  weath_tweet(browser),
        "fact_key": facts(browser),
        "hemiA": hemi1a(browser),
        "hemiB": hemi2a(browser),
        "hemiC": hemi3a(browser),
        "hemiD": hemi4a(browser)
}

    return scrape_dict

mars_dict = scrape()
