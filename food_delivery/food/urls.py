from django.conf.urls import url

from . import views
from basescript import init_logger
from kwikapi.django import RequestHandler

from food_delivery.settings import LOG_FILE_PATH

log = init_logger(fpath=LOG_FILE_PATH, fmt="json", level="INFO")

urlpatterns = [
    url(r'api/', RequestHandler(views.api, log=log).handle_request),
]
