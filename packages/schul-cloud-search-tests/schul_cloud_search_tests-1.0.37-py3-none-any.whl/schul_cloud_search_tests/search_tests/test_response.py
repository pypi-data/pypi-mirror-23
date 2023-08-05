"""
Each test function here covers a part of the specification.
They are run when the server returns a request.
If they fail, the client gets feedback.

About the test functions:
Please provide
- A short description of what is tested
- Links to the specification, where this is specified.

"""
from pytest import mark
from schul_cloud_resources_api_v1.schema import get_schemas


def test_result_is_json(result):
    """Make sure the result is a json object.
    
    See
    - http://jsonapi.org/"""
    try:
        json = result.json()
    except:
        assert False, "The result must be a valid json object, not {}".format(result.content)
    else:
        assert isinstance(json, dict), "The result must be a json object, not {}".format(json)


def test_response_schema(search_response):
    """If the request was successful, it must match the search-response schema.
    
    Schema:
    - https://github.com/schul-cloud/resources-api-v1/tree/master/schemas/search-response
    
    The response is successful of a status code 200 is returned.
    """
    schema = get_schemas()["search-response"]
    schema.validate(search_response)
    

@mark.skip(reason="TODO")
def test_400_and_500_status_codes_have_the_jsonapi_design(error):
    """If the status code is 4XX, it contains a list of errors.

    Schema:
    - https://github.com/schul-cloud/resources-api-v1/tree/master/schemas/error
    """


def test_the_content_type_is_from_the_jsonapi(result):
    """Make sure the returned content type is specified and expected.
    
    See here:
    - http://jsonapi.org/format/#content-negotiation-clients
    """
    assert result.headers.get("Content-Type", "") == "application/vnd.api+json", "The content type of the server reply must be application/vnd.api+json."
