import unittest
import mount_folders 
mount_folders.mount() # sets other projectfolders in searchpath

from app import app # this is the flask test

class Flask_Test(unittest.TestCase):


    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_models_redirect(self):
        r = self.app.get('/models/handshake')
        assert r.status_code == 301
        #assert b'/models folder is now /services' in r.data

    def test_services(self):
        r = self.app.get('/services/handshake')
        assert r.status_code == 200
        assert b"Service is a smile. It is an acknowledging wave, a reaching handshake, a friendly wink, and a warm hug. It's these simple acts that matter most, because the greatest service to a human soul has always been the kindness of recognition. [R. Goodrich]" in r.data

if __name__ == '__main__':
    unittest.main()

