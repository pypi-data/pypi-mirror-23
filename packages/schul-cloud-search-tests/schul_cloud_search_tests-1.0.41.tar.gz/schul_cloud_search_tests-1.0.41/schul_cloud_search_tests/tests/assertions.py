"""
This module contains the assertions and error definitions.

Please see the specification for the errors.
- https://github.com/schul-cloud/schul_cloud_search_tests/blob/master/README.rst#specification
"""
from schul_cloud_resources_server_tests.tests.assertions import assertIsError
from schul_cloud_resources_api_v1.schema import get_schemas

ERROR_CLIENT_REQUEST = 400 # https://httpstatuses.com/400
Q = "Q" # The query string
ERROR_SERVER_RESPONSE = 409 # https://httpstatuses.com/409

ERROR = get_schemas()["error"].get_valid_examples()[0]
