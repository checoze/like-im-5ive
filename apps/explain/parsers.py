import urllib
from bs4 import BeautifulSoup

def parse_url(term):
    """ Returns a computer name and url """
    try:
    	url_data = urllib.urlopen(term)
    	url_html = url_data.read()

        try:
            soup = BeautifulSoup(url_html)
            return soup.title.string, term
        except:
            pass
    except Exception, e:
        print e
        return term, term
