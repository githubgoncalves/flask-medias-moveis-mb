from typing import Type
from domain.services import MovingAverage
from application.presenters import HttpRequest, HttpResponse, HttpErrors
from datetime import datetime


class FindMovingAverageController():
    """Class to Define Route to find_moving_average_use_case use case"""

    def __init__(self, find_moving_average_use_case: Type[MovingAverage], pair: str):
        self.find_moving_average_use_case = find_moving_average_use_case
        self.pair = pair.strip().upper()

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call find_moving_average_use_case"""

        response = None

        if http_request.body:
            # if body in htp_request
            body_params = http_request.body.keys()

            if "from_timestamp" in body_params:
                from_timestamp, to_timestamp = self.check_timestamp(body_params)

            if "range" in body_params:
                range = int(http_request.body["range"])

            if (from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None
                    and range != '' and range != None):
                response = self.find_moving_average_use_case.get_mms(self.pair, from_timestamp, to_timestamp, range)
        elif http_request.query:
            body_params = http_request.query

            if "from_timestamp" in body_params:
                from_timestamp, to_timestamp = self.check_timestamp(body_params)

                if from_timestamp is None and to_timestamp is None:
                    response = {"Success": False, "Data": "O valor entre as datas não pode ser maior que 365 dias!"}
                    return HttpResponse(status_code=422, body=response["Data"])

            if "range" in body_params:
                range = int(body_params["range"])

            if (from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None
                    and range != '' and range != None):
                response = self.find_moving_average_use_case.get_mms(self.pair, from_timestamp, to_timestamp, range)
        else:
            response = {"Success": False, "Data": None}

        if response["Success"] is False:
            https_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=https_error["status_code"], body=https_error["body"]
            )

        return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )


    def check_timestamp(self, body_params):
        dt_now = datetime.now()

        from_timestamp = int(body_params["from_timestamp"])

        if "to_timestamp" in body_params:
            to_timestamp = int(body_params["to_timestamp"])
        else:
            to_timestamp = datetime.timestamp(dt_now)

        dt_from_timestamp = datetime.fromtimestamp(from_timestamp)
        dt_to_timestamp = datetime.fromtimestamp(to_timestamp)
        quantidade_dias = abs((dt_from_timestamp - dt_to_timestamp).days)

        if quantidade_dias > 365:
            return None, None

        return from_timestamp, int(to_timestamp)
