from typing import Dict, List
from abc import ABC, abstractclassmethod


class RequestAPI(ABC):
    """ Interface to Request API Externa use case """

    @abstractclassmethod
    def request_api(cls, pair: str, from_timestamp: int, to_timestamp: int, precision: str) -> List:
        """ Case """

        raise Exception("Should implement method: register")