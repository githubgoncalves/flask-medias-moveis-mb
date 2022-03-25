from typing import Dict
from abc import ABC, abstractclassmethod
from api.domain.models import MovingAverage


class MovingAverage(ABC):
    """ Interface to RegisterUser use case """

    @abstractclassmethod
    def moving_average(cls, pair: str, from_timestamp: int, to_timestamp: int, precision: str) -> Dict[bool, MovingAverage]:
        """ Case """

        raise Exception("Should implement method: register")