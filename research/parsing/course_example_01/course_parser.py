from bs4 import SoupStrainer as strainer, BeautifulSoup as soup

class CourseParser:
    def __init__(self):
        self.tag_spec = ''
        self.soup = ''

    def set_parsing_spec(self, tag, attribute, attr_value):
        """Set parsing specifictation, which are obtained
        using the strainer
        """
        self.tag_spec = strainer(tag, 
                                 attrs={attribute: attr_value})
        return self.tag_spec

    def get_table(self, page_content):
        """
        """
        self.soup = soup(page_content, 'html.parser',
                         parse_only=self.tag_spec)
        return self.soup

    def get_rows(self, table):
        self.rows = self.soup.find_all('tr')
        return self.rows

    def get_cols(self, rows):
        pass
