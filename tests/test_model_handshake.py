import unittest
import mount_folders
mount_folders.mount() # sets other projectfolders in searchpath
from handshake_message import modelPredict # must be after mount


class test_modelPredict(unittest.TestCase):
    
    def test_return_value(self):
        msg = "Service is a smile. It is an acknowledging wave, a reaching handshake, a friendly wink, and a warm hug. It's these simple acts that matter most, because the greatest service to a human soul has always been the kindness of recognition. [R. Goodrich]"
        self.assertIsNotNone(modelPredict())
        self.assertEqual(modelPredict(), msg) 

if __name__ == "__main__":
    unittest.main()
