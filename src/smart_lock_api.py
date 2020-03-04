from august.api import Api 
from august.authenticator import Authenticator, AuthenticationState

class SmartLock:

    def __init__(self):
        self.api = Api(timeout=20)
        self.authenticator = Authenticator(self.api, "phone|email", "YourPhoneNumber", "YourPassword",
                                access_token_cache_file="access_token_cache_file.txt")
        self.id='EBE57CE9D7624D78A5A0BE44340E0DFE'
        self.authentication = self.authenticator.authenticate()
        self.access_token = self.authentication.access_token

    def get_smartlock_status(self):
        self.api.get_lock_status(self.access_token, self.id)

    def unlock(self):
        unlock_response = self.api.unlock(self.access_token, self.id)
        print(unlock_response)
def main():
    smart_lock_instance = SmartLock()
    smart_lock_instance.unlock()

if __name__ == "__main__":
    main()
