import requests
from urllib.parse import urljoin
from src.load_config import config
from src.logger import get_logger
from src.retry_api import retry

logger = get_logger(__name__)

class APIClient:
    def __init__(self, base_url=None, timeout=None, headers=None, retries=None, retry_backoff=None):
        self.base_url = config.get('base_url')
        self.timeout = int(config.get('timeout', 10))
        self.session = requests.Session()
        self.session.headers.update(config.get('headers', {}))
        self.retries = int(config.get('retries', 3))
        self.retry_backoff = float(config.get('retry_backoff', 1))

    def _full_url(self, path: str):
        return urljoin(self.base_url, path)

    @retry(max_attempts=int(config.get('retries', 3)), backoff=float(config.get('retry_backoff', 1)))
    def request(self, method: str, path: str, **kwargs):
        url = self._full_url(path)
        try:
            logger.debug(f"{method} {url} | kwargs={{{', '.join(k+':'+str(v) for k,v in kwargs.items())}}}")
        except Exception:
            logger.debug(f"{method} {url} | kwargs (unprintable)")
        resp = self.session.request(method, url, timeout=self.timeout, **kwargs)

        # Detailed logging of request/response for inspection
        logger.info(f"Request: {method} {resp.url}")
        logger.debug(f"Request headers: {dict(resp.request.headers)}")
        if resp.request.body:
            try:
                logger.debug(f"Request body: {resp.request.body}")
            except Exception:
                logger.debug("Request body (binary or unreadable)")
        logger.info(f"Response: status={resp.status_code} len={len(resp.content)}")
        logger.debug(f"Response headers: {dict(resp.headers)}")
        try:
            json_body = resp.json()
            logger.debug(f"Response json: {json_body}")
        except Exception:
            logger.debug("Response not JSON parseable")
        resp.raise_for_status()
        return resp

    def get(self, path: str, **kwargs):
        return self.request('GET', path, **kwargs)

    def post(self, path: str, **kwargs):
        return self.request('POST', path, **kwargs)

# convenience
client = APIClient()

def main():
    """Entry point for execution."""
    logger.info("=== Starting Thinkplam APIClient test run ===")

    try:
        # Example: make a test GET request (replace with your real endpoint)
        response = client.get("/")
        logger.info(f"Response status: {response.status_code}")
        logger.info("=== APIClient test completed successfully ===")

    except Exception as e:
        logger.exception(f"❌ Error during APIClient run: {e}")


if __name__ == "__main__":
    main()
