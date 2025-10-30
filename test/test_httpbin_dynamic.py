from src.unique_data_generation import random_user, random_uuid

def test_post_echo(api_client):
    user = random_user()
    resp = api_client.post('/post', json=user)
    j = resp.json()
    assert j['json']['email'] == user['email']

def test_dynamic_path_and_uuid(api_client):
    uuid = random_uuid()
    resp = api_client.get(f'/anything/{uuid}')
    j = resp.json()
    assert j['url'].endswith(uuid)
