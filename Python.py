import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):
    
    def test_website_availability(self):
        """
        Test that the ATG World website is available and loads properly.
        """
        url = 'https://atg.world'
        
        try:
            response = requests.get(url)
            # Print statements to log activity
            print(f"Attempting to connect to {url}")
            
            # The website is considered up if the status code is 200
            self.assertEqual(response.status_code, 200)
            print("Connection successful. Website is up.")
            
        except requests.RequestException as e:
            # If any exception occurs during the request, the test fails
            self.fail(f"Website could not be reached. Error: {e}")
            print("Connection failed. Website is down.")

# This allows the test to be run from the command line
if __name__ == '__main__':
    unittest.main()
