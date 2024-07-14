import requests

class API:
    def __init__(self):
        self.baseApiURL = "https://api.openbrewerydb.org/v1/breweries"

    def get_breweries_list(self):
        return requests.get(self.baseApiURL)    
    
    def get_single_brewery(self, id):
        url = f"{self.baseApiURL}/{id}"
        return requests.get(url)