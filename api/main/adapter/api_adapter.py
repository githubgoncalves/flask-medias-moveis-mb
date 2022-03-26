from typing import Type
from sqlalchemy.exc import IntegrityError
from main.interface import RouteInterface as Route
from application.presenters.helpers import HttpRequest, HttpResponse
from application.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask
    :param - Flask Request
    :api_route: Composite Routes
    """

    try:
        query_string_params = request.args.to_dict()
    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(
        header=request.headers, body=request.json, query=query_string_params
    )

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response