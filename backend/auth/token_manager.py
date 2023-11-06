import time

class TokenManager:
    def __init__(self, credential, api_type, token_url):
        self.credential = credential
        self.api_type = api_type
        self.token_url = token_url
        self.token_info = {
            "token": "",
            "expires_on": 0
        }

    def check_token(self):
        if self.api_type != "azure_ad":
            return

        if self.token_info["expires_on"] < time.time() + 60:
            new_token = self.credential.get_token(self.token_url)
            self.token_info = {
                "token": new_token.token,
                "expires_on": new_token.expires_on
            }

        return self.token_info["token"]
