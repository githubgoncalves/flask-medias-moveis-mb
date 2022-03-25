from api.domain.models import MovingAverage
from api.infra.repository.moving_average_repository import MovingAverageRepository
from typing import Type, Dict


class MovingAverage():
    """Class to define usecase: Register User"""

    def __init__(self, user_repository: Type[MovingAverageRepository]) -> None:
        self.moving_average_repository = MovingAverageRepository()

    def register_mms(self, data) -> None:
        """Register MMS
        :param - pair: pair crypto
               - from_timestamp: from date timestamp
               - to_timestamp: to date timestamp
        :return - Dictionary with information of the process
        """

        response = None
        #validate_entry = isinstance(name, str) and isinstance(password, str)
        validate_entry = True

        if validate_entry:
            response = self.moving_average_repository.register_mms_from_db_table('moving_average', data)
        return {"Success": validate_entry, "Data": response}



    def get_mms(self, pair: str, from_timestamp: int, to_timestamp: int, range: str) -> Dict[bool, MovingAverage]:
        """Find MMS
        :param - pair: pair crypto
               - from_timestamp: from date timestamp
               - to_timestamp: to date timestamp
        :return - Dictionary with information of the process
        """

        response = None
        #validate_entry = isinstance(name, str) and isinstance(password, str)
        validate_entry = True

        if validate_entry:
            response = self.moving_average_repository.select(pair, from_timestamp, to_timestamp, range)
        return {"Success": validate_entry, "Data": response}