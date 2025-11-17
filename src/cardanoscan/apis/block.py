from typing import Any, Dict, Optional

def get_block_details(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/block", params=params)

def get_latest_block_details(self) -> Any:
    return self._do_request_sync("GET", "/block/latest")
