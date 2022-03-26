from pydantic import BaseModel


class MovingAverage200Schema(BaseModel):  # serializer
    timestamp: int
    mms_200: str = None


    class Config:
        orm_mode = True

