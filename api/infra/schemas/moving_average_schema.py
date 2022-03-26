from pydantic import BaseModel


class MovingAverageSchema(BaseModel):  # serializer
    id: int
    pair: str = None
    timestamp: int
    mms_20: str = None
    mms_50: str = None
    mms_200: str = None


    class Config:
        orm_mode = True

