from os.path import abspath, dirname
from restclients_core.dao import DAO
import os


class CoDa_DAO(DAO):
    def service_name(self):
        return 'coda'

    def service_mock_paths(self):
        return [abspath(os.path.join(dirname(__file__), "resources"))]