import time
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from typing import Optional

import httpx
import ujson
from django.conf import settings

SECONDS_IN_DAY = 60 * 60 * 24

def timed_lru_cache(seconds: int, maxsize: int = 10240):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)

        # инструментирование декоратора двумя атрибутами,
        # представляющими время жизни кэша lifetime
        # и дату истечения срока его действия expiration
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache

class AvitoClient:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.base_url = "https://api.avito.ru"
        self.token_url = self.base_url + "/token"
        self.reviews_url = self.base_url + "/ratings/v1/reviews"
        data = self._get_api_key()
        if data is not None:
            self.access_token, expires_in = data["api_key"], data["expires_in"]
        else:
            self.access_token = None
            expires_in = None
        if self.access_token is None or not self._is_valid_key(self.access_token, expires_in):
            self.access_token, expires_in = self._update_api_key(client_id, client_secret)
            self._cache_api_key(self.access_token, expires_in)

    def _get(self, url: str, params={}) -> httpx.Response:
        auth_header = {"Authorization": f"Bearer {self.access_token}"}
        return httpx.get(url, headers=auth_header, params=params)
    def _get_api_key(self) -> Optional[dict]:
        try:
            with open("key.json", "r") as rf:
                return ujson.load(rf)
        except:
            return None

    def _update_api_key(self, client_id: str, client_secret: str) -> tuple[str, int]:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        key = httpx.post(
            self.token_url,
            data={"client_id":client_id, "client_secret":client_secret,"grant_type":"client_credentials"},
            headers=headers,
        ).json()
        print(key)
        return (key["access_token"], time.time()+key["expires_in"])

    def _cache_api_key(self, api_key: str, expires_in: int):
        with open("key.json", "w") as wf:
            ujson.dump({"api_key":api_key, "expires_in":expires_in}, wf)

    def _is_valid_key(self, api_key: str, expires_in: int) -> bool:
        if time.time() + 3600 < expires_in:
            return False
        return True

    def get_reviews(self) -> dict:
        offset = 0
        _ret = []
        # while True:
        #     response = self._get(self.reviews_url, params={"offset":offset, "limit":50}).json()
        #     if len(response["reviews"]) == 0:
        #         break
        #     ret += response["reviews"]
        #     offset += 50
        return self._get(self.reviews_url, params={"offset":offset, "limit":50}).json()["reviews"]

    # def optimize_get_reviews(self) -> dict:
    #     return self.get_reviews()

def get_api_instanse():
    client_id = settings.AVITO_CLIENT_ID
    client_secret = settings.AVITO_CLIENT_SECRET
    return AvitoClient(client_id, client_secret)

@timed_lru_cache(SECONDS_IN_DAY)
def avito_get_reviews() -> dict:
    api = get_api_instanse()
    return api.get_reviews()