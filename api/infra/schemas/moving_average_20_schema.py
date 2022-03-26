from pydantic import BaseModel


class MovingAverage20Schema(BaseModel):  # serializer
    timestamp: int
    mms_20: str = None


    class Config:
        orm_mode = True

