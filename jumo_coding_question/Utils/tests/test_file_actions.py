import os
import tempfile
from unittest import TestCase

from jumo_coding_question.Utils.file_actions import CSVFileRead, CSVFileWrite


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

    def test_does_file_exist(self):
        self.assertTrue(CSVFileRead.does_file_exist(self.tmpfile_))

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


class TestCSVFileWrite(TestCase):
    """
    Test cases for writing dict data to a file.
    """

    tempfile_ = os.path.join(tempfile.gettempdir(), "tmp-testfile.csv")

    def setUp(self):
        with open(self.tempfile_, "w") as f:
            f.write("")

    def test_setup(self):
        self.assertTrue(os.path.isfile(self.tempfile_))

    def test_data_written(self):
        dict_data = [{1: 233, 3: 23432}, {1: 23432, 3: 21332123}]
        is_written = CSVFileWrite.writefile(self.tempfile_, dict_data)

        with open(self.tempfile_, "r") as f:
            written_data = f.readlines()
        self.assertTrue(is_written)
        self.assertListEqual(
            written_data, ["1,3\n", "233,23432\n", "23432,21332123\n"]
        )

    def test_setup(self):
        self.assertTrue(os.path.isfile(self.tempfile_))

    def test_writing_of_non_existent_file(self):
        file_ = os.path.join(tempfile.gettempdir(), "/nslkjew/test.txt")
        self.assertTrue(CSVFileWrite.writefile(file_, "Hello World!"))

    def tearDown(self):
        file_ = os.path.join(tempfile.gettempdir(), "/nslkjew/test.csv")
        if os.path.isfile(self.tempfile_):
            os.remove(self.tempfile_)
        if os.path.isfile(file_):
            os.remove(file_)
        else:
            pass
