""" Repository to User Entity """
from domain.models import MovingAverage
from infra.config import DBConnectionHandler
from infra.schemas import (MovingAverage20Schema,
                           MovingAverage50Schema,
                           MovingAverage200Schema)
from sqlalchemy import text, func, and_
from typing import List
import pandas as pd


class MovingAverageRepository():
    """Class to manage User Repository"""

    def select(cls, pair: str, from_timestamp: int, to_timestamp: int, range: int) -> List[MovingAverage]:
        """Find MMS
        :param - pair: pair crypto
               - from_timestamp: from date timestamp
               - to_timestamp: to date timestamp
        :return - Dictionary with information of the process
        """

        try:
            query_data = None
            if pair and from_timestamp and to_timestamp and range:
                with DBConnectionHandler() as db_connection:
                    if range == 20:
                        data = (
                            db_connection.session.query(MovingAverage).filter(MovingAverage.pair == pair,
                                                                              MovingAverage.mms_20 != None,
                                                                              MovingAverage.timestamp >= from_timestamp,
                                                                              MovingAverage.timestamp <= to_timestamp)
                        )
                        query_data = [MovingAverage20Schema.from_orm(d) for d in data]
                    elif range == 50:
                        data = (
                            db_connection.session.query(MovingAverage).filter(MovingAverage.pair == pair,
                                                                              MovingAverage.mms_50 != None,
                                                                              MovingAverage.timestamp >= from_timestamp,
                                                                              MovingAverage.timestamp <= to_timestamp)
                        )
                        query_data = [MovingAverage50Schema.from_orm(d) for d in data]
                    else:
                        data = (
                            db_connection.session.query(MovingAverage).filter(MovingAverage.pair == pair,
                                                                              MovingAverage.mms_200 != None,
                                                                              MovingAverage.timestamp >= from_timestamp,
                                                                              MovingAverage.timestamp <= to_timestamp)
                        )
                        query_data = [MovingAverage200Schema.from_orm(d) for d in data]

            return query_data

        except:
            raise
        finally:
            db_connection.session.close()

        return None

    def register_mms_from_db_table(self, table_name, data):
        """
        Scrape the column names from a database table to a list
        :param sql_cursor: sqlite cursor
        :param table_name: table name to get the column names from
        :return: a list with table column names
        """

        with DBConnectionHandler() as db_connection:
            table_column_names = 'PRAGMA table_info(' + table_name + ');'
            result = db_connection.get_engine().execute(text(table_column_names))
            column_names = list()
            for row in result:
                column_names.append(row[1])
                print("Coluna:", row[1])

            df = pd.DataFrame.from_records(data)
            df.columns = column_names
            df.to_sql(name=table_name,
                      con=db_connection.get_engine(),
                      index=False,
                      if_exists='append')

        return 'Calculate and insert process finished'
