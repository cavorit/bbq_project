import unittest, requests
from handshake_message import handshake_message

import app # from  app import handshake as handshake


class test_handshake(unittest.TestCase):
    
    url = 'http://127.0.0.1'
    port = 5000

    url += ':'+str(port)

    def test_got_response_from_connection(self, url=url):
        
        response = requests.get(url=url)
        self.assertTrue(response.__nonzero__())

        
    def test_handshake_return(self, url=url):
        
        response = requests.get(url=url)        
        self.assertEqual(response.content.decode(), handshake_message()) 

if __name__ == "__main__":
    unittest.main()



