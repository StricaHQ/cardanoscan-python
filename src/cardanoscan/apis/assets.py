from typing import Any, Dict, Optional

def get_asset_details(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/asset", params=params)


def get_assets_by_policy_id(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/asset/list/byPolicyId", params=params)


def get_assets_by_address(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/asset/list/byAddress", params=params)


def get_asset_holders_by_policy_id(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/asset/holders/byPolicyId", params=params)


def get_asset_holders_by_asset_id(self, params: Optional[Dict] = None) -> Any:
    return self._do_request_sync("GET", "/asset/holders/byAssetId", params=params)
