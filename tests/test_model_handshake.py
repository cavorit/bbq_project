import unittest
import mount_folders
mount_folders.mount() # sets other projectfolders in searchpath
from handshake import modelPredict # must be after mount
from handshake import modelTransform 

class test_model_handshake(unittest.TestCase):
    
    def test_modelTransform(self):
        self.assertIsNone(modelTransform(JSONstringREQ='{}'))        

    def test_modelPredict(self):
        msg = "Service is a smile. It is an acknowledging wave, a reaching handshake, a friendly wink, and a warm hug. It's these simple acts that matter most, because the greatest service to a human soul has always been the kindness of recognition. [R. Goodrich]"
        self.assertIsNotNone(modelPredict())
        self.assertEqual(modelPredict(), msg) 

if __name__ == "__main__":
    unittest.main()
