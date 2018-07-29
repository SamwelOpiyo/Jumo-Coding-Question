import os
import tempfile
from unittest import TestCase

from jumo_coding_question.Utils.file_actions import CSVFileRead


class TestCSVFileRead(TestCase):
    """
    Test cases for reading file.
    """

    tmpfile_ = os.path.join(tempfile.gettempdir(), "tmp-testfile.csv")

    def setUp(self):
        with open(self.tmpfile_, "w") as f:
            f.write("Name, ID")

    def test_setup(self):
        self.assertTrue(os.path.isfile(self.tmpfile_))

    def test_reading_of_non_existent_file(self):
        file_ = "/nslkjew/test.csv"
        self.assertIsNone(CSVFileRead.readfile(file_))

    def test_reading_of_existent_file(self):
        self.assertEqual(CSVFileRead.readfile(self.tmpfile_), ["Name, ID"])

    def tearDown(self):
        if os.path.isfile(self.tmpfile_):
            os.remove(self.tmpfile_)
        else:
            pass
