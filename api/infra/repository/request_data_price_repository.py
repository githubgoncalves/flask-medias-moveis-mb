import requests
import pandas as pd
import json
from typing import List
from enum import Enum
from pathlib import Path
import cloudscraper
from urllib.request import Request, urlopen


class Pair(str, Enum):
    BRLBTC = 'BRLBTC'
    BRLETH = 'BRLETH'


class RequestDataPriceRepository():
    """Class to manage Consulta API"""

    def consulta(self, pair, from_timestamp, to_timestamp, precision) -> List:

        """URL de exemplo utilizada na consulta dos dados"""
        """https://mobile.mercadobitcoin.com.br/v4/BRLBTC/candle?from=1577836800&to=1606565306&precision=1d"""

        url = f"https://mobile.mercadobitcoin.com.br/v4/{pair}/candle?from=" \
              f"{from_timestamp}&to={to_timestamp}&precision={precision}"

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'})
        response = urlopen(req).read()
        response_json = json.loads(response)

        if (response_json['status_code'] == 200 or response_json['status_code'] == 100):
            df = pd.DataFrame.from_records(response_json)
            dados = pd.DataFrame.from_records(df["candles"])
        else:
            filename = Path(__file__).resolve(). \
                           parent.parent / "repository/dataset_example/candle.json"
            with open(filename, 'r') as json_file:
                df = pd.DataFrame.from_records(json.load(json_file))
                dados = pd.DataFrame.from_records(df["candles"])

        return {"Success": True, "Data": dados}
