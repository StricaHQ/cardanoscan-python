from typing import Any

def get_network_details(self) -> Any:
    return self._do_request_sync("GET", "/network/state")

def get_network_protocol_details(self) -> Any:
    return self._do_request_sync("GET", "/network/protocolParams")
