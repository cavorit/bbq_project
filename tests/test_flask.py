import unittest
import mount_folders 
mount_folders.mount() # sets other projectfolders in searchpath

from app import app # this is the flask test

class HelloWorldTestCase(unittest.TestCase):


    def setUp(self):
        app.testing = True
        self.app = app.test_client()


    def test_models_redirect(self):
        r = self.app.get('/models/handshake')
        assert r.status_code = 200
        assert b'/models folder is now /services' in r.data

    def test_services_req(self):
        r = self.app.get('/services/handshake')
        assert r.status_code = 200
        assert b'msg' in r.data

if __name__ == '__main__':
    unittest.main()

