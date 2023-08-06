class Article:
    """Represents an article.

    Attributes
    ----------
    url: str
        The URL of the article.
    length: int
        The amount of characters
        in the summary.
    title: str
        The title of the article.
    content: str
        The summary of the article.
    keywords: list
        List of keywords used to summarize the article.
        Returns an empty list if keyword count is 0.
    """


    def __init__(self, data):
        self._length = data.get('sm_api_character_count')
        self._title = data.get('sm_api_title')
        self._content = data.get('sm_api_content')
        self._keywords = data.get('sm_api_keyword_array', [])
        self._article_url = data.get('article_url')

    @property
    def url(self):
        return self._article_url

    @property
    def length(self):
        return int(self._length)

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def keywords(self):
        return self._keywords
