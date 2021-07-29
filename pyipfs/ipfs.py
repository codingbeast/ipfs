import requests
from Error import IPFSConnectionError
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import sys
class connection:
    def __init__(self, server = "127.0.0.1", port = "5001"):
        url = "http://{}:{}/api/v0/version/deps".format(server, port)
        try:
            response = requests.post(url)
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            raise IPFSConnectionError()
            sys.exit(141)
        
        
        
#obj = connection()