import connexion
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_hello_world():
    """
    returns a hello world json
    A simple hello world json here

    :rtype: InlineResponse200
    """
    my_dict = {'value': 'Hello World!'}
    return my_dict
