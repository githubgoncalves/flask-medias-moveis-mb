"""Design Pattern """
from application.presenters.controllers import RequestAPIController
from infra.repository import RequestDataPriceRepository
from infra.repository import MovingAverageRepository


def request_api():
    """Composing Register Consulta API Route
    :param - None
    :return - Object with  Consulta API Route
    """

    repository_request = RequestDataPriceRepository()
    repository_mms = MovingAverageRepository()
    register_user_route = RequestAPIController(repository_request, repository_mms)

    return register_user_route