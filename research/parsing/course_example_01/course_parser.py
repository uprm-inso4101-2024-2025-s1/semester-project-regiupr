from bs4 import SoupStrainer as strainer, BeautifulSoup as soup

class CourseParser:
    """Parser for course."""

    def __init__(self):
        self.tag_spec = ''
        self.soup = ''

    def strainer(self, tag, attribute, attr_value):
        """Set parsing specifictation, which are obtained
        using the strainer
        """
        self.tag_spec = strainer(tag, 
                                 attrs={attribute: attr_value})
        return self.tag_spec

    def get_table_from(self, page_content):
        """Parse the provided page content with BeautifulSoup.
        'parse_only' parameter taken directly from itself.
        """
        self.soup = soup(page_content, 'html.parser',
                         parse_only=self.tag_spec)
        return self.soup

    def get_rows_from(self, table):
        self.rows = self.soup.find_all('tr')
        return self.rows

    def get_cols_from(self, rows):
        self.cols = []
        self.data = {}
#        for row in rows:
            #            for col in row:
                
