from api.application.presenters.controllers import FindMovingAverageController
from api.domain.services import MovingAverage
from api.infra.repository.moving_average_repository import MovingAverageRepository


def find_moving_average_composer(pair) -> FindMovingAverageController:
    """Composing Find Search moving average
    :param - None
    :return - Object with Search moving average
    """

    repository = MovingAverageRepository()
    repository_mms = MovingAverage(repository)
    find_mms_route = FindMovingAverageController(repository_mms, pair)

    return find_mms_route