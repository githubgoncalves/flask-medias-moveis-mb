from abc import ABC, abstractmethod
from typing import List
from domain.models import MovingAverage


class UserRepositoryInterface(ABC):
    """Interface user repostory"""

    @abstractmethod
    def insert(self, pair: str, from_timestamp: int, to_timestamp: int, range: str) -> MovingAverage:
        """abstractmethod"""
        raise NotImplementedError

    @abstractmethod
    def select(self, pair: str, from_timestamp: int, to_timestamp: int, range: str) -> List[MovingAverage]:
        """abstractmethod"""
        raise NotImplementedError