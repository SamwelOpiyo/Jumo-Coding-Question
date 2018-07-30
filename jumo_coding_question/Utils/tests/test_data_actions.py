from unittest import TestCase

from jumo_coding_question.Utils.data_actions import CreateDictFromCSVData


class TestCreateDictFromCSVData(TestCase):
    """
    Test cases for parsing read csv file and creating a dictionary from it.
    """

    def test_dictify_column_head_and_columns(self):
        head = ["Name", "ID"]
        data = [["James", "18712"], ["John", "209928"]]
        self.assertListEqual(
            CreateDictFromCSVData.dictify_column_head_and_columns(head, data),
            [
                {head[0]: data[0][0], head[1]: data[0][1]},
                {head[0]: data[1][0], head[1]: data[1][1]},
            ],
        )

    def test_split_columns(self):
        csv_file_data = ["Name,ID\n", "James,18712\n", "John,209928\n"]
        self.assertTupleEqual(
            CreateDictFromCSVData.split_columns(csv_file_data),
            (["Name", "ID"], [["James", "18712"], ["John", "209928"]]),
        )

    def test_CSVDataToDict(self):
        csv_file_data = ["Name,ID\n", "James,18712\n", "John,209928\n"]
        self.assertListEqual(
            CreateDictFromCSVData.CSVDataToDict(csv_file_data),
            [
                {"Name": "James", "ID": "18712"},
                {"Name": "John", "ID": "209928"},
            ],
        )
