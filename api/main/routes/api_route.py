from flask import Blueprint, jsonify, Response, json, request,current_app
from api.infra.config import create_database
from flask_restx import Resource, Api
from datetime import datetime
from api.main.composer import (
    find_moving_average_composer,
    request_api
)
from api.main.adapter import flask_adapter


api_routes_bp = Blueprint("api_routes", __name__)
api_routes_sg = Api(api_routes_bp, version="1.0", title="BTC and ETH Moving Averages", description="MERCADO BITCOIN")

"""-----------------"""
name_space_data_base = api_routes_sg.namespace("v1/load-data-base", description="Calc and Load Data Base")
name_space_indicators = api_routes_sg.namespace("v1/indicators", description="BTC and ETH Moving Averages")
"""-----------------"""


database = name_space_data_base.parser()
database.add_argument('pair', required=True, type=str, location='args', help="BRLBTC ou BRLETH")
database.add_argument('from_timestamp', required=True, type=int, location='args', help="Format timestamp")
database.add_argument('to_timestamp', required=False, type=int, location='args', help="Format timestamp")
database.add_argument('precision', required=True, type=str, location='args', help="Examples: 1d, 2d ...")
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
indicators.add_argument('from_timestamp', required=True, type=int, location='args', help="Format timestamp")
indicators.add_argument('to_timestamp', required=False, type=int, location='args', help="Format timestamp")
@name_space_indicators.route('/<string:pair>/mms', doc={"descrição":"Search moving average"})
class Indicators(Resource):
    @name_space_indicators.expect(indicators)
    def get(self, pair):
        """ register user route """

        current_app.logger.info("query mms " + pair)

        message = {}
        response = flask_adapter(request=request, api_route=find_moving_average_composer(pair))

        if response.status_code < 300:
            message = response.body
            return jsonify({"status": response.status_code, "data": message})

            # Handling Errors
        return (
            jsonify(
                {"error": {"status": response.status_code, "title": response.body["error"]}}
            )
        )
