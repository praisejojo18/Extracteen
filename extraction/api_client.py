import requests
from requests.exceptions  import HTTPError, RequestException
def get_data(url, params=None, timeout =10):
    try: 
        response = requests.get(url, params=params, headers=None, timeout=timeout)

        print("Request URL:", response.url)
        response.raise_for_status()

        return {
           "success":True,
           "status_code": response.status_code,
           "data": response.json()
        }

    except HTTPError as htt_err:
        status_code = response.status_code

        if status_code  == 404:
            return {"my_cutomer_response":  "opps! the data you are looking for does not exist"
                    }
        
        if status_code == 401:
            return {
                "error": "Authentication failed. Check your API credentials.",
                "status_code": 401
            }

        if status_code == 403:
            return {
                "error": "You are not authorized to access this resource.",
                "status_code": 403
            }

        if status_code == 429:
            return {
                "error": "Rate limit exceeded. Too many requests.",
                "status_code": 429
            }

        return {
            "error": f"HTTP error occurred: {status_code}",
            "status_code": status_code
        }

        

    except RequestException as req_err:
        return {
            "error": f"Request failed: {req_err}"     
       }
        