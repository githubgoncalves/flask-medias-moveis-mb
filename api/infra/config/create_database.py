from api.infra.config.db_config import DBConnectionHandler
from sqlalchemy import MetaData, Table, Column, Integer, TIMESTAMP, String


class CreateDataBase():

    def __init__(self):
        self.engine = DBConnectionHandler().get_engine()

        metadata = MetaData()

        moving_average = Table('moving_average', metadata,
                               Column('id', Integer, nullable=False),
                               Column('pair', String, nullable=False),
                               Column('timestamp', TIMESTAMP, nullable=False),
                               Column('mms_20', Integer, nullable=True),
                               Column('mms_50', Integer, nullable=True),
                               Column('mms_200', Integer, nullable=True)

                               )

        metadata.create_all(self.engine, checkfirst=True)
