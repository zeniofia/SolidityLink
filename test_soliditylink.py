# test_soliditylink.py
"""
Tests for SolidityLink module.
"""

import unittest
from soliditylink import SolidityLink

class TestSolidityLink(unittest.TestCase):
    """Test cases for SolidityLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityLink()
        self.assertIsInstance(instance, SolidityLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
