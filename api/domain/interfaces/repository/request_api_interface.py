from abc import ABC, abstractmethod
from typing import List


class RequestAPIInterface(ABC):
    """Interface Consulta API repository"""

    @abstractmethod
    def request_data_price(self, pair: str, from_timestamp: int, to_timestamp: int) -> List:
        """abstractmethod"""
        raise NotImplementedError
