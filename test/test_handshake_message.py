import unittest
from handshake_message import handshake_message

class test_handshake_message(unittest.TestCase):
    
    def test_return_value(self):
        msg = "Service is a smile. It is an acknowledging wave, a reaching handshake, a friendly wink, and a warm hug. It's these simple acts that matter most, because the greatest service to a human soul has always been the kindness of recognition. [R. Goodrich]"
        self.assertIsNotNone(handshake_message)
        self.assertEqual(handshake_message(), msg) 

if __name__ == "__main__":
    unittest.main()
