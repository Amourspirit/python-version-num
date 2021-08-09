if __name__ == '__main__':
    import path_imports

import unittest
from verr import Version, ArgumentError, ArgumentOutOfRangeError, ArgumentNullError
import json

# run test in order
unittest.TestLoader.sortTestMethodsUsing = None


class TestVersionJson(unittest.TestCase):
    def test_001(self):
        v = Version()
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '0.0')
        self.assertEqual(v.__hash__(), 0)

    def test_010_json_m_m_b_r(self):
        v = Version("1.2.3.4")
        j = json.dumps(v)
        self.assertEqual(
            j, '{"major": 1, "minor": 2, "build": 3, "revision": 4}')
        v_j = Version(json.loads(j))
        self.assertEqual(v_j.major, 1)
        self.assertEqual(v_j.minor, 2)
        self.assertEqual(v_j.build, 3)
        self.assertEqual(v_j.revision, 4)
        self.assertEqual(v_j.__str__(), '1.2.3.4')
        self.assertEqual(v_j.__repr__(), '<Version(1, 2, 3, 4)>')

    def test_011_json_m_m_b(self):
        v = Version("1.2.3")
        j = json.dumps(v)
        self.assertEqual(j, '{"major": 1, "minor": 2, "build": 3}')
        v_j = Version(json.loads(j))
        self.assertEqual(v_j.major, 1)
        self.assertEqual(v_j.minor, 2)
        self.assertEqual(v_j.build, 3)
        self.assertEqual(v_j.revision, 0)

    def test_012_json_m_m(self):
        v = Version.parse("1.2")
        j = json.dumps(v)
        self.assertEqual(j, '{"major": 1, "minor": 2}')
        v_j = Version(json.loads(j))
        self.assertEqual(v_j.major, 1)
        self.assertEqual(v_j.minor, 2)
        self.assertEqual(v_j.build, 0)
        self.assertEqual(v_j.revision, 0)

    def test_013_json_m_errro(self):
        j = '{"major": 1}'
        d = json.loads(j)
        self.assertRaises(ArgumentNullError, Version, d)

    def test_014_json_m_m_b_r_more(self):
        j = '{"major": 1, "minor": 2, "build": 3, "revision": 4, "year": 2021}'
        v_j = Version(json.loads(j))
        self.assertEqual(v_j.major, 1)
        self.assertEqual(v_j.minor, 2)
        self.assertEqual(v_j.build, 3)
        self.assertEqual(v_j.revision, 4)
        self.assertEqual(v_j.__str__(), '1.2.3.4')
        self.assertEqual(v_j.__repr__(), '<Version(1, 2, 3, 4)>')

    def test_015_json_m_m_b_repeat(self):
        v = Version("1.2.3")
        j = json.dumps(v)
        self.assertEqual(j, '{"major": 1, "minor": 2, "build": 3}')
        v_j = Version(json.loads(j))
        self.assertEqual(v_j.major, 1)
        self.assertEqual(v_j.minor, 2)
        self.assertEqual(v_j.build, 3)
        self.assertEqual(v_j.revision, 0)
        self.assertTrue(v == v_j)
        self.assertEqual(v.__hash__(), v_j.__hash__())

        j = json.dumps(v_j)
        v = Version(json.loads(j))
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 0)
        self.assertTrue(v == v_j)
        self.assertEqual(v.__hash__(), v_j.__hash__())

    def test_020_json_missing_major(self):
        j = '{"minor": 2, "build": 3, "revision": 4}'
        d = json.loads(j)
        self.assertRaises(ArgumentNullError, Version, d)

    def test_021_json_missing_minor(self):
        j = '{"major": 2, "build": 3, "revision": 4}'
        d = json.loads(j)
        self.assertRaises(ArgumentNullError, Version, d)

    def test_022_json_neg_major(self):
        j = '{"major": -1, "minor": 2, "build": 3, "revision": 4}'
        d = json.loads(j)
        self.assertRaises(ArgumentOutOfRangeError, Version, d)

    def test_023_json_neg_minor(self):
        j = '{"major": 1, "minor": -2, "build": 3, "revision": 4}'
        d = json.loads(j)
        self.assertRaises(ArgumentOutOfRangeError, Version, d)

    def test_024_json_neg_build(self):
        j = '{"major": 1, "minor": 2, "build": -3, "revision": 4}'
        d = json.loads(j)
        self.assertRaises(ArgumentOutOfRangeError, Version, d)

    def test_025_json_neg_revision(self):
        j = '{"major": 1, "minor": 2, "build": 3, "revision": -4}'
        d = json.loads(j)
        self.assertRaises(ArgumentOutOfRangeError, Version, d)

    def test_030_json_str_values(self):
        j = '{"major": "1", "minor": "2", "build": "3", "revision": "4"}'
        v = Version(json.loads(j))
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 4)
        k = '{"major": 1, "minor": 2, "build": 3, "revision": 4}'
        v_dump = json.dumps(v)
        self.assertEqual(k, v_dump)

    def test_031_json_str_bad_val(self):
        j = '{"major": "1", "minor": "b", "build": "3", "revision": "4"}'
        d = json.loads(j)
        self.assertRaises(ArgumentError, Version, d)

    def test_032_json_str_empty_val(self):
        j = '{"major": "1", "minor": "3", "build": "", "revision": "4"}'
        d = json.loads(j)
        self.assertRaises(ArgumentError, Version, d)

if __name__ == '__main__':
    unittest.main()
