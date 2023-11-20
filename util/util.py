
def create_coap_uri(address="localhost", port=5683, resource_path=".well-known/core"):
    return f"coap://{address}:{port}/{resource_path}"
