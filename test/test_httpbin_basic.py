import pytest
from src.unique_data_generation import random_query_params


def test_get_ip(api_client):
    resp = api_client.get('/ip')
    j = resp.json()
    assert 'origin' in j

def test_get_headers_inspection(api_client):
    headers = {'X-Test-Header': 'pytest-header'}
    resp = api_client.get('/headers', headers=headers)
    j = resp.json()
    # httpbin returns header keys capitalized, verify contains header
    assert j['headers'].get('X-Test-Header') == 'pytest-header'

def test_response_formats_json(api_client):
    params = random_query_params(2)
    resp = api_client.get('/get', params=params)
    j = resp.json()
    assert 'args' in j
    assert set(j['args'].keys()) == set(params.keys())
