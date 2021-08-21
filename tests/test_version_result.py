if __name__ == '__main__':
    import path_imports

import unittest
from verr import FormatError, Version, ArgumentError, ArgumentOutOfRangeError, ArgumentNullError



class TestVersionResult(unittest.TestCase):

    # region Set up Methods
    @classmethod
    def setUpClass(cls):
        cls.ParseFailureKind = Version.ParseFailureKind
        cls.VersionResult = Version.VersionResult
        

    # endregion Set up Methods

    # region Tear Down Methods
    @classmethod
    def tearDownClass(cls):
        pass
    # endregion Tear Down Methods
    def test_argument_null_error(self):
        pf = self.ParseFailureKind.ARGUMENT_NULL_ERR
        vr = self.VersionResult()
        vr.init('input', True)
        self.assertRaises(ArgumentNullError, vr.set_failure, failure=pf, argument='minor')

        vr = self.VersionResult()
        vr.init('input', False)
        vr.set_failure(failure=pf, argument='minor')
        fail = vr.get_version_parse_exception()
        self.assertIsInstance(fail, ArgumentNullError)

    def test_argument_error(self):
        pf = self.ParseFailureKind.ARGUMENT_ERR
        vr = self.VersionResult()
        vr.init('input', True)
        self.assertRaises(ArgumentError, vr.set_failure, failure=pf, argument='minor')

        vr = self.VersionResult()
        vr.init('input', False)
        vr.set_failure(failure=pf, argument='minor')
        fail = vr.get_version_parse_exception()
        self.assertIsInstance(fail, ArgumentError)
    
    def test_general_argument_error(self):
        self.assertRaises(ArgumentError, Version.parse, input=".1.2.3.4")
        pf = self.ParseFailureKind.NONE
        vr = self.VersionResult()
        vr.init('input', True)
        self.assertRaises(ArgumentError, vr.set_failure, failure=pf, argument='minor')

        vr = self.VersionResult()
        vr.init('input', False)
        vr.set_failure(failure=pf, argument='minor')
        fail = vr.get_version_parse_exception()
        self.assertIsInstance(fail, ArgumentError)
    
    def test_argument_out_or_range_error(self):
        pf = self.ParseFailureKind.ARGUMENT_OUT_OF_RANGE_ERR
        vr = self.VersionResult()
        vr.init('input', True)
        self.assertRaises(ArgumentOutOfRangeError, vr.set_failure, failure=pf, argument='minor')

        vr = self.VersionResult()
        vr.init('input', False)
        vr.set_failure(failure=pf, argument='minor')
        fail = vr.get_version_parse_exception()
        self.assertIsInstance(fail, ArgumentOutOfRangeError)
        
    def test_format_error(self):
        pf = self.ParseFailureKind.FORMAT_ERR
        vr = self.VersionResult()
        vr.init('input', True)
        self.assertRaises(ArgumentError, vr.set_failure, failure=pf, argument='not a number')
        self.assertRaises(FormatError, vr.set_failure, failure=pf, argument=self)

        vr = self.VersionResult()
        vr.init('input', False)
        vr.set_failure(failure=pf, argument='not a number')
        fail = vr.get_version_parse_exception()
        self.assertIsInstance(fail, ArgumentError)
    
    def test_property_parsed_version(self):
        v = Version.parse("1.2.3.4")
        vr = self.VersionResult()
        vr.parsed_version = v
        self.assertEqual(vr.parsed_version, v)

if __name__ == '__main__':
    unittest.main()