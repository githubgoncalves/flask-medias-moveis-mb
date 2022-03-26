from infra.repository.request_data_price_repository import RequestDataPriceRepository
from typing import List, Type, Dict
import pandas as pd


class RequestDataPriceService():
    """Class to define usecase: Register User"""

    def __init__(self, request_api_repository: Type[RequestDataPriceRepository]) -> None:
        self.request_api_repository = request_api_repository

    def request_data_price(self, pair, from_timestamp, to_timestamp) -> List:
        """Request API
        :param - pair: pair crypto
               - from_timestamp: from date timestamp
               - to_timestamp: to date timestamp
               - precision: precision day
        :return - Dictionary with information of the process
        """

        response = None
        validate_entry = isinstance(pair, str) \
                         and isinstance(from_timestamp, int) \
                         and isinstance(to_timestamp, int)


        if validate_entry:
            response = self.request_api_repository.consulta(pair, from_timestamp, to_timestamp)
            df = pd.DataFrame.from_records(response["Data"])
            df_calculete_mm = self.calculate_simple_moving_average(df)
            df_data_insert = df_calculete_mm[['timestamp', 'mms_20', 'mms_50', 'mms_200']]
            df_data_insert.insert(0, 'id', df_data_insert.index + 1)
            df_data_insert.insert(1, 'pair', pair)
            print(df_data_insert)
        return {"Success": validate_entry, "Data": df_data_insert}


    def calculate_simple_moving_average(self, values) -> None:
        values['mms_20'] = values["close"].rolling(20).mean()
        values['mms_50'] = values["close"].rolling(50).mean()
        values['mms_200'] = values["close"].rolling(200).mean()
        return values


