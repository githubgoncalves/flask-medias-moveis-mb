from typing import Type
from api.domain.services import MovingAverage
from api.application.presenters import HttpRequest, HttpResponse, HttpErrors


class FindMovingAverageController():
    """Class to Define Route to find_moving_average_use_case use case"""

    def __init__(self, find_moving_average_use_case: Type[MovingAverage], pair: str):
        self.find_moving_average_use_case = find_moving_average_use_case
        self.pair = pair

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:
            # if body in htp_request
            body_params = http_request.body.keys()

            if "from_timestamp" in body_params:
                from_timestamp = int(http_request.body["from_timestamp"])
            if "to_timestamp" in body_params:
                to_timestamp = int(http_request.body["to_timestamp"])
            if "range" in body_params:
                range = str(http_request.body["range"]).strip().lower()

            if (from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None
                    and range != '' and range != None):
                response = self.find_moving_average_use_case.get_mms(self.pair, from_timestamp, to_timestamp, range)
        elif http_request.query:
            body_params = http_request.query

            if "from_timestamp" in body_params:
                from_timestamp = int(body_params["from_timestamp"])
            if "to_timestamp" in body_params:
                to_timestamp = int(body_params["to_timestamp"])
            if "range" in body_params:
                range = str(body_params["range"]).strip().lower()

            if (from_timestamp != '' and from_timestamp != None
                    and to_timestamp != '' and to_timestamp != None
                    and range != '' and range != None):
                response = self.find_moving_average_use_case.get_mms(self.pair, from_timestamp, to_timestamp, range)
        else:
            response = {"Success": False, "Data": None}

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )