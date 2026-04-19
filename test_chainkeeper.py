# test_chainkeeper.py
"""
Tests for ChainKeeper module.
"""

import unittest
from chainkeeper import ChainKeeper

class TestChainKeeper(unittest.TestCase):
    """Test cases for ChainKeeper class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainKeeper()
        self.assertIsInstance(instance, ChainKeeper)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainKeeper()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
