from pydantic import BaseModel


class MovingAverage50Schema(BaseModel):  # serializer
    timestamp: int
    mms_50: str = None


    class Config:
        orm_mode = True

