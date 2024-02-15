# This is the web crawler file, This is a helper file to crawl.py.
import urllib.request               # Extensible library for opening URLs.
from html.parser import HTMLParser          # Simple HTML and XHTML parser.

def crawl(url):                     # This is the web crawler function. it inherits the command-line argument from web.py.
    mod = str(url)                  # Argparse returns a namespace object, mod converts to str object.
    f = urllib.request.urlopen(mod[15:-2])              # This opens the url into a file object using urllib.request.
    contents = f.read()                 # This stores the contents of the read file which is returned as a bytes-object.
    byt_two_str = str(contents)         # bytes object gets converted to string.
    parser = MyHTMLParser()             # Initialized html parser class.
    parser.feed(byt_two_str)            # use feed method to parse url.

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):

        flies = []                      # A container to store filtered objects for further manipulation.

        if tag == 'a':                  # This searches for the <A> hyperlink tags of a web site.
            if len(attrs) > 1:
                flies.append(attrs)
                
                for i in flies:         # This is the outer loop of the flies list used- 
                                        # for prepping the data for output.
                    for i in i:             # This is the inner loop used to turn the data into a string-
                        e = str(i)          # to strip unnecessary data output.
                        if 'href' in e:
                            print(e[10:-2])

if __name__ == '__main__':
    pass                            