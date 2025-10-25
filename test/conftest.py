import sys
import os
import pytest

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.load_config import config
from src.main import APIClient

@pytest.fixture(scope='session')
def cfg():
    return config

@pytest.fixture(scope='session')
def api_client(cfg):
    base = os.getenv('BASE_URL', cfg.get('base_url'))
    return APIClient(base_url=base,
                     timeout=int(cfg.get('timeout', 10)),
                     retries=int(cfg.get('retries', 3)),
                     retry_backoff=float(cfg.get('retry_backoff', 1)))
