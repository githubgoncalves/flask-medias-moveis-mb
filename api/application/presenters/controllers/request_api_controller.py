from typing import Type
from domain.services import RequestDataPriceService
from domain.services import MovingAverage
from application.presenters import HttpRequest, HttpResponse, HttpErrors


class RequestAPIController():
    """Class to Define Route to consulta_api use case"""

    def __init__(self, request_api_use_case: Type[RequestDataPriceService],
                 mms_api_use_case: Type[MovingAverage]):
        self.request_api = RequestDataPriceService(request_api_use_case)
        self.moving_average = MovingAverage(mms_api_use_case)

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call consulta_api"""

        response = None

        if http_request.body:
            # if body in htp_request
            body_params = http_request.body.keys()

            if "pair" in body_params:
                pair = str(http_request.body["pair"]).strip().upper()
            if "from_timestamp" in body_params:
                from_timestamp = int(http_request.body["from_timestamp"])
            if "to_timestamp" in body_params:
                to_timestamp = int(http_request.body["to_timestamp"])

            if (pair != '' and pair != None
                    and from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None):
                response = self.request_api.request_data_price(pair, from_timestamp, to_timestamp)
        elif http_request.query:
            body_params = http_request.query

            if "pair" in body_params:
                pair = str(body_params["pair"]).strip().upper()
            if "from_timestamp" in body_params:
                from_timestamp = int(body_params["from_timestamp"])
            if "to_timestamp" in body_params:
                to_timestamp = int(body_params["to_timestamp"])

            if (pair != '' and pair != None
                    and from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None):
                response = self.request_api.request_data_price(pair, from_timestamp, to_timestamp)
        else:
            response = {"Success": False, "Data": None}

        response = self.moving_average.register_mms(response['Data'])

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