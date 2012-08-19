import urllib
from bs4 import BeautifulSoup

def parse_url(term):
    """ Returns a computer name and url """
    try:
    	url_data = urllib.urlopen(term)
    	url_html = url_data.read()

        soup = BeautifulSoup(url_html)
        
        #Try Getting the meta title
        """
        try:
            tag = soup.find('meta[name="title"]')
            return tag['content'], term
        except Exception, foo:
            print foo
            pass
        """
        
        #Add LOTS of parsing methods
        #Even parse title in a site-specific way

        #Try Getting the title
        try:
            return soup.title.string, term
        except:
            pass
    except Exception, e:
        print e
        return term, term
