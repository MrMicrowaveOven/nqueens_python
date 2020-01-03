import sys
sys.path.append("../lib")

import unittest

from space import Space

class SpaceTest(unittest.TestCase):
    def test_space_init(self):
        s = Space()
        assert not s.filled, 'space does not start filled'

    def test_is_filled(self):
        s = Space()
        assert not s.is_filled(), 'space does not start filled'

    def test_fill(self):
        s = Space()
        s.fill()
        assert s.filled, 'fill does not fill'

    def test_empty(self):
        s = Space()
        s.fill()
        assert s.is_filled(), 'fill does not fill'
        s.empty()
        assert not s.is_filled(), 'empty does not empty'
if __name__ == "__main__":
    unittest.main()
