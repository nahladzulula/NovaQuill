# test_novaquill.py
"""
Tests for NovaQuill module.
"""

import unittest
from novaquill import NovaQuill

class TestNovaQuill(unittest.TestCase):
    """Test cases for NovaQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaQuill()
        self.assertIsInstance(instance, NovaQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
