import requests
from pyipfs.Errors import IPFSConnectionError
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import sys
from pyipfs.Constants import ADDFILE_ENDPINT
class connection:
    def __init__(self, server = "127.0.0.1", port = "5001"):
        url = "http://{}:{}/api/v0/version/deps".format(server, port)
        try:
            response = requests.post(url)
            print("connected.")
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            raise IPFSConnectionError()
            sys.exit(141)
        
        
        
#obj = connection()