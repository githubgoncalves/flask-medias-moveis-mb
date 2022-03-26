from flask import Blueprint, jsonify, json, request, current_app
from infra.config import create_database
from flask_restx import Resource, Api
from application.presenters.extensions import obj_dict
from datetime import datetime

from main.composer import (
    find_moving_average_composer,
    request_api
)
from main.adapter import flask_adapter


api_routes_bp = Blueprint("api_routes", __name__)
api_routes_sg = Api(api_routes_bp, version="1.0", title="BTC and ETH Moving Averages", description="MERCADO BITCOIN")

"""-----------------"""
name_space_convert_timestamp = api_routes_sg.namespace("v1/convert-date-to-timestamp",
                                                       description="Convert date to timestamp")
name_space_data_base = api_routes_sg.namespace("v1/load-data-base", description="Calc and Load Data Base")
name_space_indicators = api_routes_sg.namespace("v1/indicators", description="BTC and ETH Moving Averages")
"""-----------------"""


convert_timestamp = name_space_convert_timestamp.parser()
convert_timestamp.add_argument('date_to_timestamp', required=True, type=str, location='args',
                               help="Format: 01/03/2020 18:35")
@name_space_convert_timestamp.route('/convert', doc={"descrição":"Calc and Load Data Base"})
class ConvertTimesTamp(Resource):
    @name_space_convert_timestamp.expect(convert_timestamp)
    def get(self):
        """Converter Data em Timestamp"""
        try:
            date = datetime.strptime(str(request.args["date_to_timestamp"]), '%d/%m/%Y %H:%M')
            to_timestamp = datetime.timestamp(date)
            return jsonify({"data": to_timestamp})
        except:
            return jsonify({"status": 422, "data": "Formato Invalido"})


database = name_space_data_base.parser()
database.add_argument('pair', required=True, type=str, location='args', help="BRLBTC ou BRLETH")
database.add_argument('from_timestamp', required=True, type=int, location='args',
                      help="Format timestamp. Exemple: 1641072946")
database.add_argument('to_timestamp', required=False, type=int, location='args',
                      help="(Default: Timestamp now). Format timestamp. Exemple: 1646170546")
@name_space_data_base.route('/', doc={"descrição":"Calc and Load Data Base"})
class LoadDataBase(Resource):
    @name_space_data_base.expect(database)
    def post(self):
        """Calcular e Carregar Dados na Base de Dados"""
        current_app.logger.info("criar base de dados")
        create_database.CreateDataBase()

        message = {}
        response = flask_adapter(request=request, api_route=request_api())

        if response.status_code < 300:
            message = response.body
            return jsonify({"status": response.status_code, "data": message})

        # Handling Errors
        return (
            jsonify(
                {"error": {"status": response.status_code, "title": response.body["error"]}}
            )
        )


indicators = name_space_indicators.parser()
indicators.add_argument('range', required=True, type=int, location='args', help="20, 50 ou 200")
indicators.add_argument('from_timestamp', required=True, type=int, location='args',
                        help="Format timestamp. Exemple: 1641072946")
indicators.add_argument('to_timestamp', required=False, type=int, location='args',
                        help="(Default: Timestamp now). Format timestamp. Exemple: 1646170546  ")
@name_space_indicators.route('/<string:pair>/mms', doc={"descrição":"Search moving average"})
class Indicators(Resource):
    @name_space_indicators.expect(indicators)
    def get(self, pair):
        """ Buscar Medias Moveis MM20, MM50 e MM200 do BRLBTC e BRL ETH """

        current_app.logger.info("query mms " + pair)

        response = flask_adapter(request=request, api_route=find_moving_average_composer(pair))

        if response.status_code < 300:
            message = response.body
            print(len(message))
            return json.dumps(message, default=obj_dict)

        if response.status_code == 422:
            message = response.body
            return jsonify({"status": response.status_code, "data": message})

            # Handling Errors
        return (
            jsonify(
                {"error": {"status": response.status_code, "title": response.body["error"]}}
            )
        )
