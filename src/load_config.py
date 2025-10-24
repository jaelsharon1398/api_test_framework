import yaml
from pathlib import Path

class Config:
    """Loads and provides access to configuration values from config.yaml."""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            try:
                config_data = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML file {self.config_path}: {e}")

        # Load 'default' section
        self.default = config_data.get("default")
        self.base_url = self.default.get("base_url")
        self.timeout = self.default.get("timeout")
        self.retries = self.default.get("retries")
        self.retry_backoff = self.default.get("retry_backoff")
        self.headers = self.default.get("headers")

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __repr__(self):
        return (
            f"<Config base_url={self.base_url}, timeout={self.timeout}, "
            f"retries={self.retries}, backoff={self.retry_backoff}>"
        )

# Instantiate a global config object for reuse
config = Config()

__all__ = ["config", "Config"]
