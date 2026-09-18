def create_api_key_headers(api_key):
    return{
        "X-API-Key": "value"
    }

def create_bearer_headers(token):
    return{
        "Authorization":f"bearer{token}"
    }