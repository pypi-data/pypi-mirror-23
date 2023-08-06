import aiohttp
import asyncio

from .article import Article
from .errors import *

class SMMRPY:
    """Represents a connection that connects to SMMRY.
    This class is used to interact with the SMMRY API.

    Only one parameter is needed to be passed when instantiating the class.

    Parameters
    ----------
    api_key : Required[str]
        Your personal SMMRY API key. Without this key,
        this wrapper will not function.
    """

    def __init__(self, api_key):
        self.api_key = api_key

        self.url = r'http://api.smmry.com/'

    async def get_smmry(self, url : str, **kwargs):
        """Returns an :class:`Article` object.

        Parameters
        ----------
        length : Optional[int]
            How long the summary should be in
            number of sentences.
        keywords : Optional[int]
            The amount of keywords should be
            included in the response.
        quotes : Optional[bool]
            Whether the summary should contain
            quotes or not.
        breaks : Optional[bool]
            Put `[BREAK]` in between each sentence.


        Raises
        ------
        InternalServerError
            Internal server problem which isn't
            your fault.
        IncorrectSubmissionVariables
            Incorrect submission variables were
            passed.
        IntentialRestriction
            Intential restriction. Could be
            low credits, disabled key, or banned key.
        SummarizationError
            There was an issue summarizing the
            article URL passed.
        """

        length = kwargs.get('length', 7)
        keywords = kwargs.get('keyword_count', 5)
        quotes = kwargs.get('quotes', True)
        breaks = kwargs.get('breaks', False)

        params = {
            'SM_API_KEY' : self.api_key,
            'SM_LENGTH' : length,
            'SM_KEYWORD_COUNT' : keywords,
            'SM_QUOTE_AVOID' : str(not quotes).lower(),
            'SM_WITH_BREAK' : str(breaks).lower(),
            'SM_URL' : url
        }

        async with aiohttp.ClientSession() as cs:
            async with cs.get(self.url, params=params) as rawdata:
                data = await rawdata.json()

        error_code = data.get('sm_api_error')
        message = data.get('sm_api_message')

        if error_code:
            if error_code == 0:
                raise InternalServerError(message)
            elif error_code == 1:
                raise IncorrectSubmissionVariables(message)
            elif error_code == 2:
                raise IntentialRestriction(message)
            elif error_code == 3:
                raise SummarizationError(message)
            else:
                raise GenericError('We failed and don\'t know why :(')

        data['article_url'] = url

        return(Article(data))
