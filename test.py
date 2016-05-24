import unittest
from LRU import LRUCache

class CacheValuesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = LRUCache()

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test_empty_cache(self):
        print('Test : Empty Cache')
        self.assertDictEqual(self.fixture.getStore(),{},"Cache is empty")

    def test_cache_oneEntry(self):
        print('Test : Cache with single value')
        self.fixture.find(1)
        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{1:1},"Cache has a single entry")

    def test_cache_repeatedOneEntry(self):
        print('Test : Cache with single value repeatedly')
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)
        self.fixture.find(1)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{1:1},"Cache has a single entry")

    def test_cache_fullSize(self):
        print('Test : Cache full size')
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(4)
        self.fixture.find(5)
        self.fixture.find(6)
        self.fixture.find(7)
        self.fixture.find(8)
        self.fixture.find(9)
        self.fixture.find(0)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9},"Cache has all entries")

    def test_cache_overflow(self):
        print('Test : Cache overflow')
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(4)
        self.fixture.find(5)
        self.fixture.find(6)
        self.fixture.find(7)
        self.fixture.find(8)
        self.fixture.find(9)
        self.fixture.find(0)
        self.fixture.find(16)
        self.fixture.find(27)
        self.fixture.find(38)
        self.fixture.find(49)
        self.fixture.find(50)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{0: 0, 6: 6, 7: 7, 8: 8, 9: 9, 38: 38, 16: 16, 49: 49, 50: 50, 27: 27},"Cache has all entries")

    def test_cache_random(self):
        print('Test : Cache random')
        self.fixture.find(1)
        self.fixture.find(22342)
        self.fixture.find("harry")
        self.fixture.find(-4689)
        self.fixture.find("&&&&")
        self.fixture.find(690040809480)
        self.fixture.find("0090")
        self.fixture.find(8)
        self.fixture.find(0)
        self.fixture.find(0)
        self.fixture.find("16")
        self.fixture.find(27568)
        self.fixture.find(38)
        self.fixture.find(49)
        self.fixture.find(50)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{0: 0, 49: 49, 38: 38, 6272037681056615: '16', 690040809480: 690040809480, -8147289704323569492: '&&&&', 27568: 27568, 8: 8, 50: 50, -3495090546366936577: '0090'},"Cache has all entries")

    def test_cache_alternateValues(self):
        print('Test : Cache alternating Values')
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(2)
        self.fixture.find(1)
        self.fixture.find(3)
        self.fixture.find(1)
        self.fixture.find(3)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(2)
        self.fixture.find(1)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{1: 1, 2: 2, 3: 3},"Cache has all entries")

    def test_cache_alternateHitsandMisses(self):
        print('Test : Cache hits  and misses for repeating values')
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(4)
        self.fixture.find(5)
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(4)
        self.fixture.find(5)
        self.fixture.find(6)
        self.fixture.find(7)
        self.fixture.find(8)
        self.fixture.find(9)
        self.fixture.find(10)
        self.fixture.find(11)
        self.fixture.find(1)
        self.fixture.find(2)
        self.fixture.find(3)
        self.fixture.find(4)
        self.fixture.find(5)

        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11},"Cache has all entries")

    def test_cache_String(self):
        print('Test : Cache with String values')
        self.fixture.find("Harry")
        self.fixture.find("Archer")
        self.fixture.find("Dexter")
        self.fixture.find("Seinfield")
        self.fixture.find("Friends")
        self.fixture.find("Shield")
        self.fixture.find("Vikings")
        self.fixture.find("Grimm")
        self.fixture.find("Google")
        self.fixture.find("Yahoo")
        self.fixture.find("Saleforce")
        self.fixture.find("twitter")
        self.fixture.find("facebook")
        self.fixture.find("capio")
        self.fixture.find("Python")
        self.fixture.find("java")
        self.fixture.find("xml")
        self.fixture.find("html")
        self.fixture.find("random strings to test String Caching")


        print self.fixture.getStore()
        self.assertDictEqual(self.fixture.getStore(),{-5999452984715080672: 'xml', -2338026935110240988: 'java', -1782981222247821945: 'random strings to test String Caching', -2359742753373747800: 'Python', -6598467229008937334: 'twitter', 3021726190866786059: 'Saleforce', -8781860034246656723: 'Yahoo', 7799575877465763251: 'html', 3162525260849330260: 'facebook', -8502831814997350055: 'capio'},"Cache has all entries")

    def test_cache_exception(self):
        print('Test : Cache with single value')
        try:
        	self.fixture.find(x)
        except:
        	pass
        else:
            self.fail('Did not NameError')

if __name__ == '__main__':
    unittest.main()