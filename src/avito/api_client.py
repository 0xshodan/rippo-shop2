from typing import Optional
import time
import httpx

class AvitoClient:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.base_url = "https://api.avito.ru"
        self.token_url = self.base_url + "/token/"
        api_key = self.get_api_key()
        if api_key is None or not self.check_valid(api_key):
            api_key = self.update_api_key(client_id, client_secret)

    def get_api_key(self) -> Optional[str]:
        try:
            with open("key", "r") as rf:
                return rf.read()
        except:
            return None
    
    def update_api_key(self, client_id: str, client_secret: str) -> str:
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        key = httpx.post(self.token_url, 
                         data={"client_id":client_id, 
                               "client_secret":client_secret, 
                               "grand_type":'"client_credentials"'},
                               headers=headers)
        print(key.json())
        print(key.url)

    def cache_api_key(self, key: str):
        pass

    def is_valid_key(self, api_key):
        pass

# x = AvitoClient("t7ivBRaOzMEhvubvwa4U", "1xLUhklG6-FgIDWD0Zqb0YAt3tOXQgoEDZwR1YY_")
x = AvitoClient("Gg8JeLsNn-kUxOJb_RFJ", "xa38qzAD50vgORrO2Ljd0YmkW-uHHA9hZGQXYvhK")