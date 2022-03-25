from infra.config import Base
from sqlalchemy import String, Integer, Column


class MovingAverage(Base):
    """Model MovingAverage"""

    __tablename__ = 'moving_average'

    id = Column(Integer, primary_key=True)
    pair = Column(String, nullable=False)
    timestamp = Column(Integer, nullable=False, unique=False)
    mms_20 = Column(Integer, nullable=False, unique=False)
    mms_50 = Column(Integer, nullable=False, unique=False)
    mms_200 = Column(Integer, nullable=False, unique=False)

    def __rep__(self):
        return f"Model Moving Averag [name={self.pair}]"

    def __eq__(self, other):
        if (
                self.id == other.id
                and self.pair == other.pair
                and self.timestamp == other.timestamp
                and self.mms_20 == other.mms_20
                and self.mms_50 == other.mms_50
                and self.mms_200 == other.mms_200
        ):
            return True
        return False


