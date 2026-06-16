import unittest
from pythonstarterpackage import main

class TestStarterPackage(unittest.TestCase):

    def test_application_execution(self):
        """Test the main entrypoint."""
        try:
            main.main()
        except Exception as e:
            self.fail(f"Error running main: {e}")

if __name__ == "__main__":
    unittest.main()

