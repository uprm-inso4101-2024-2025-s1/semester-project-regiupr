import requests

class CourseWebScraper:
    """Web scrapper for courses.
    At the moment downloads from a single url
    """

    def __init__(self):
        self.url = ''
        self.page = ''
        self.content = ''

#   def set_url_to_scrap(self, url):
#        """Set the url to be scraped."""
#        self.url = url

    def download_page_from(self, url):
        """Download the webpage from the url that was set before.
        Returns a Response object of the webpage.
        """
        self.url = url
        self.page = requests.get(self.url)
        if self.page.status_code == 200:
            print(self.page.status_code, '==> Success: page downloaded')
            return self.page
        else:
            print('Failed to read url')

    def page_content(self):
        """Get the content of the page from the Response object.
        Returns the content.
        """
        self.content = self.page.content
        return self.content
