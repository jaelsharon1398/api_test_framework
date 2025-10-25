# HTTPBin API Test Framework (pytest)

This is a ready-to-run pytest-based API testing framework targeting https://httpbin.org.
It includes:
- Configuration via config.yaml
- Custom retry decorator with detailed logging
- Faker-based dynamic test data generation
- Allure and pytest-html reporting support
- GitHub Actions CI workflow that uploads reports as artifacts

## Setup
```bash
git clone https://github.com/jaelsharon1398/api_test_framework.git
cd api_test_framework
pip install -r requirements.txt
