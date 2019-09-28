import urllib
import sys
from MyHTMLParser import MyHTMLParser
import urllib.request as req
import time


class Crawler:

    # Construct a crawler
    def __init__(self, seedURL, numPages):
        self.seedURL = seedURL
        self.numPages = int(numPages)
        self.maxdepth = 5
        self.maxreach = 0
        self.sumsize = 0
        self.crawledlist = set()
        self.maxsize = 0
        self.minsize = 999999999

    # Start the crawling
    def startCrawl(self):

        # start crawling
        self.crawl(1, [self.seedURL])

        # finish crawling and print to text file
        # first record the size of crawling
        self.writestats()

        # record all the urls that have been crawled
        self.recordURL()

    # record all the stats when crawling is done
    def writestats(self):
        stats = open(r"stats.txt", "w+")
        avgsize = 0 if len(self.crawledlist) == 0 else self.sumsize / len(self.crawledlist)
        maxstr = "Maximum size: " + str(self.maxsize) + " bytes\n"
        minstr = "Minimum size: " + str(self.minsize) + " bytes\n"
        avgstr = "Average size: " + str(avgsize) + " bytes\n"
        reachstr = "Maximum depth reach: " + str(self.maxreach) + "\n"
        line = [maxstr, minstr, avgstr, reachstr]
        stats.writelines(line)
        stats.close()

    # record the URLs that have been crawled
    def recordURL(self):
        urlfile = open("URLsCrawled.txt", "w+")
        urlfile.writelines(self.crawledlist)
        urlfile.close()

    # write every html to a single file
    def create_web_file(self, data, num):
        prefix = self.count_digits(num)
        urlfile = open("./HTML_files/" + prefix + str(num) + ".txt", "w+")
        urlfile.write(data)
        urlfile.close()

    # Count the digits
    def count_digits(self, num):
        prefix = "000"
        if len(str(abs(num))) == 4:
            prefix = ""
        elif len(str(abs(num))) == 3:
            prefix = "0"
        elif len(str(abs(num))) == 2:
            prefix = "00"
        elif len(str(abs(num))) == 1:
            prefix = "000"
        return prefix

    # record values like max size and min size every time during crawling
    def record(self, url, depth):
        if (urllib.request.urlopen(url).info()['content-length'] != None):
            self.crawledlist.add(url + "\n")
            size = int(urllib.request.urlopen(url).info()['content-length'])
            self.sumsize += size
            self.maxreach = max(self.maxreach, depth)
            self.maxsize = max(self.maxsize, size)
            self.minsize = min(self.minsize, size)
            return True
        else:
            return False

    # crawler to crawl the web
    def crawl(self, depth, frontier):
        if depth > self.maxdepth:
            return

        nextLevelFrontier = list()
        for url in frontier:
            # only parse when the number of crawled pages are not exceeding maximum
            if len(self.crawledlist) < self.numPages and url not in self.crawledlist:
                # pass in the URL and create the request
                request = req.Request(url, headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
                })
                try:
                    time.sleep(1)
                    # send the request to the url and get the response
                    data = req.urlopen(request).read().decode("utf-8")
                    parser = MyHTMLParser()
                    parser.feed(data)
                    # Handling Nonetype
                    if self.record(url, depth):
                        self.create_web_file(data, len(self.crawledlist))
                        print(url)
                        print("Finished:", len(self.crawledlist),"files")
                        print("current depth: ", depth)
                        nextLevelFrontier += parser.urls
                # try to catch errors when encounter
                except urllib.error.HTTPError as err:
                    # handling page not found error
                    if err.code == 404:
                        continue
                    else:
                        raise
        self.crawl(depth + 1, nextLevelFrontier)


def main(argv):
    crawler = Crawler(argv[1], argv[2])
    crawler.startCrawl()

if __name__== "__main__":
    main(sys.argv)