import requests
from bs4 import BeautifulSoup


def fetch_webpage(url, timeout=10):
    try:
        response = requests.get(
            url,
            timeout=timeout
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return {
            "success": True,
            "status_code": response.status_code,
            "soup": soup
        }

    except requests.exceptions.HTTPError as http_error:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": f"HTTP error: {http_error}"
        }

    except requests.exceptions.RequestException as request_error:
        return {
            "success": False,
            "status_code": None,
            "error": f"Request failed: {request_error}"
        }