
class identify(object):

    def __init__(self, provider):
        self.provider = provider
        if self.provider == 'aws':
            self.credentials = {"key": "", "secret": ""}
        elif self.provider == "digitalocean":
            self.credentials = {"key": "", "secret": ""}
        else:
            return "Invalid provider"


    def getKey(self):
        return self.credentials['key']

    def getSecret(self):
        return self.credentials['secret']

