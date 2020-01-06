from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.urls = list()

    # Only getting links with certain characteristics
    def handle_starttag(self, tags, attrs):
        if tags == "a":
            for name, value in attrs:
                candidate = value.startswith('/wiki/') \
                            and not value == '/wiki/Main_Page' \
                            and not ':' in value
                if name == "href" and candidate:
                    self.urls.append('http://en.wikipedia.org' + value)



