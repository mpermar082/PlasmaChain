# test_plasmachain.py
"""
Tests for PlasmaChain module.
"""

import unittest
from plasmachain import PlasmaChain

class TestPlasmaChain(unittest.TestCase):
    """Test cases for PlasmaChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        # Create an instance of PlasmaChain and verify it's of the correct type
        instance = PlasmaChain()
        self.assertIsInstance(instance, PlasmaChain)
        
    def test_run_method(self):
        """Test the run method."""
        # Create an instance of PlasmaChain and verify the run method returns True
        instance = PlasmaChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()