# This is the main file to be called from the command line, ex: py crawl.py url.
import argparse     # This is for the command line argument.
import web      # This imports the core web crawler file.

def main():
    parser = argparse.ArgumentParser()              # Parser for command-line options, arguments and sub-commands.
    parser.add_argument('url', help='Crawls a web page for links. Cmd: py crawl.py Site-URL.')
    args = parser.parse_args()
    web.crawl(args)                                 # Function call to crawl() in web.py where the actual web crawling happens.
    
if __name__ == "__main__":
    main()