# coding: utf-8
import testing_path_imports
import unittest
from version.ver import Version, ArgumentError, ArgumentOutOfRangeError, ArgumentNullError

# run test in order
unittest.TestLoader.sortTestMethodsUsing = None


class TestVersion(unittest.TestCase):

    def test_001(self):
        v = Version()
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '0.0')
        self.assertEqual(v.__hash__(), 0)

    def test010_instance_major_int(self):
        v = Version(2)
        self.assertEqual(v.major, 2)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '2.0')
        self.assertEqual(v.__hash__(), 536870912)

    def test011_instance_major_str(self):
        v = Version("2.0")
        self.assertEqual(v.major, 2)
        self.assertEqual(v.minor, 0)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '2.0')
        self.assertEqual(v.__hash__(), 536870912)

    def test012_instance_major_str_short(self):
        self.assertRaises(ArgumentError, Version, "2")

    def test013_instance_major_str_empty(self):
        self.assertRaises(ArgumentNullError, Version, "")

    def test014_instance_major_str_empty_part(self):
        self.assertRaises(ArgumentError, Version, "2..0")

    def test015_instance_major_str_empty_part(self):
        self.assertRaises(ArgumentError, Version, 1, 2, 3, 4, 5)

    def test016_minor_neg(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, 1, 2, -2)

    def test017_rev_neg(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, 1, 2, 2, -1)
        
    def test_018(self):
        self.assertRaises(ArgumentError, Version, "1.a.2")

    def test_019(self):
        self.assertRaises(ArgumentError, Version, 1, 'a',2)
        self.assertRaises(ArgumentError, Version, "1", 'a', 2)
        
    def test020_instance_all_int(self):
        v = Version(1, 2, 3, 4)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 4)
        self.assertEqual(str(v), '1.2.3.4')
        self.assertEqual(v.__hash__(), 270544900)

    def test021_instance_all_single_str(self):
        v = Version("1.2.3.4")
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 4)
        self.assertEqual(str(v), '1.2.3.4')

    def test022_instance_m_m_b(self):
        v = Version("1.2.3")
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '1.2.3')

    def test023_instance_m_m(self):
        v = Version("1.2")
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '1.2')

    def test024_instance_int_m_m_b(self):
        v = Version(1,2,44)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 44)
        self.assertEqual(v.revision, 0)
        self.assertEqual(str(v), '1.2.44')
        self.assertEqual(v.__hash__(), 270712832)

    def test025_instance_int_m_m(self):
        v = Version(24, 29)
        self.assertEqual(v.major, 24)
        self.assertEqual(v.minor, 29)
        self.assertEqual(v.build, 0)
        self.assertEqual(v.revision, 0)
        
    def test030_parse(self):
        v = Version.parse('0.1.0')
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 1)
        self.assertEqual(v.build, 0)

    def test031_parse_all(self):
        v = Version.parse("1.2.3.4")
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.build, 3)
        self.assertEqual(v.revision, 4)

    def test031_parse_too_many(self):
        self.assertRaises(ArgumentError, Version.parse, "1.2.3.4.5")

    def test031_parse_too_few(self):
        self.assertRaises(ArgumentError, Version.parse, "1")

    def test031_parse_missing_part(self):
        self.assertRaises(ArgumentError, Version.parse, "2.1.0.")

    def test032_parse_empty_str(self):
        self.assertRaises(ArgumentNullError, Version.parse, "")

    def test033parse_empty_none(self):
        self.assertRaises(ArgumentError, Version.parse, None)

    def test034parse_neg(self):
        self.assertRaises(ArgumentOutOfRangeError, Version.parse, "1.-2")
    
    def test035parse_empty_str(self):
        self.assertRaises(ArgumentNullError, Version.parse, "")

    def test050_eq(self):
        v1 = Version.parse("1.2.3.4")
        v2 = Version.parse("1.2.3.4")
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == 22)

    def test052_rev_gt_eq(self):
        v1 = Version.parse("1.2.3")
        v2 = Version.parse("1.2.3")
        self.assertTrue(v1 >= v2)
        _type_error = False
        try:
            print(v1 >= 22)
        except TypeError:
            _type_error = True
        self.assertTrue(_type_error)

    def test053_rev_gt_eq(self):
        v1 = Version.parse("1.2.3")
        v2 = Version.parse("1.2.3")
        self.assertTrue(v1 <= v2)
        _type_error = False
        try:
            print(v1 <= 22)
        except TypeError:
            _type_error = True
        self.assertTrue(_type_error)

    def test054_rev_gt(self):
        v1 = Version.parse("1.2.3.2")
        v2 = Version.parse("1.2.3")
        self.assertTrue(v1 > v2)
        _type_error = False
        try:
            print(v1 > 22)
        except TypeError:
            _type_error = True
        self.assertTrue(_type_error)

    def test054_rev_lt(self):
        v1 = Version("1.2.2")
        v2 = Version("1.2.3")
        self.assertTrue(v1 < v2)
        _type_error = False
        try:
            print(v1 < 22)
        except TypeError:
            _type_error = True
        self.assertTrue(_type_error)

    def test055_rev_ne(self):
        v1 = Version("1.2.2")
        v2 = Version("1.2.3")
        self.assertTrue(v1 != v2)
        self.assertTrue(v1 != 22)

    def test056_major_comp(self):
        v1 = Version("2.2.2")
        v2 = Version("1.2.2")
        self.assertTrue(v1 > v2)
        self.assertTrue(v2 < v1)
        
    def test057_minor_comp(self):
        v1 = Version("1.3.2")
        v2 = Version("1.2.2")
        self.assertTrue(v1 > v2)
        self.assertTrue(v2 < v1)
        
    def test058_build_comp(self):
        v1 = Version("1.2.3")
        v2 = Version("1.2.2")
        self.assertTrue(v1 > v2)
        self.assertTrue(v2 < v1)

    def test059_rev_comp(self):
        v1 = Version("1.2.2.2")
        v2 = Version("1.2.2.1")
        self.assertTrue(v1 > v2)
        self.assertTrue(v2 < v1)


    def test060_str_eq(self):
        v1 = Version("1.2.2")
        self.assertEqual(str(v1), "1.2.2")

    def test070_str_neg_major(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, -1, 2)
        
    def test071_str_neg_minor(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, 1, -2)
        
    def test072_str_neg_build(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, "1.2.-3")
    
    def test072_str_neg_rev(self):
        self.assertRaises(ArgumentOutOfRangeError, Version, "1.2.3.-5")
    
    def test080_to_str(self):
        v = Version("1.2.3.4")
        self.assertRaises(ArgumentOutOfRangeError, v.to_str, 5)
        self.assertEqual(v.to_str(1), '1')
        self.assertEqual(v.to_str(2), '1.2')
        self.assertEqual(v.to_str(3), '1.2.3')
        self.assertEqual(v.to_str(4), '1.2.3.4')
    
    def test081_to_str_build_err(self):
        v = Version("1.2")
        self.assertRaises(ArgumentOutOfRangeError, v.to_str, 5)
        self.assertEqual(v.to_str(1), '1')
        self.assertEqual(v.to_str(2), '1.2')
        self.assertRaises(ArgumentError, v.to_str, 3)
    
    def test082_to_str_rev_err(self):
        v = Version("1.2.3")
        self.assertRaises(ArgumentOutOfRangeError, v.to_str, 5)
        self.assertEqual(v.to_str(1), '1')
        self.assertEqual(v.to_str(2), '1.2')
        self.assertEqual(v.to_str(3), '1.2.3')
        self.assertRaises(ArgumentError, v.to_str, 4)

    def test090_rev_hi_lo(self):
        rev = int("ffbbff0b", 16)
        v = Version(1,2,3,rev)
        self.assertEqual(v.major_revision, int("ffbb", 16))
        self.assertEqual(v.minor_revision, int("ff0b", 16))
    def test100_inherit(self):
        class tmp(Version):
            pass
        self.assertRaises(TypeError, tmp, "1.2.-3")

    def test200_try_parse(self):
        v_result = Version.try_parse('0.1.0')
        v = v_result[1]
        self.assertTrue(v_result[0])
        self.assertEqual(v.major, 0)
        self.assertEqual(v.minor, 1)
        self.assertEqual(v.build, 0)
        
    def test201_try_parse_empty_str(self):
        v_result = Version.try_parse('')
        e = v_result[1]
        self.assertFalse(v_result[0])
        self.assertIsInstance(e, ArgumentNullError)
    
    def test202_try_parse_non_str(self):
        v_result = Version.try_parse(2)
        e = v_result[1]
        self.assertFalse(v_result[0])
        self.assertIsInstance(e, ArgumentError)
        
    def test203_try_parse(self):
        v_result = Version.try_parse('0.1.0.2.1')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentError)

    def test204_try_parse(self):
        v_result = Version.try_parse('1')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentError)

    def test205_try_parse_neg_minor(self):
        v_result = Version.try_parse('1.-2')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentOutOfRangeError)

    def test206_try_parse_neg_build(self):
        v_result = Version.try_parse('1.2.-3')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentOutOfRangeError)

    def test207_try_parse_neg_rev(self):
        v_result = Version.try_parse('1.2.3.-5')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentOutOfRangeError)
    
    def test208_try_parse_bad_build(self):
        v_result = Version.try_parse('a.2.3.5')
        e = v_result[1]
        self.assertIsInstance(e, ArgumentError)
    
if __name__ == '__main__':
    unittest.main()
