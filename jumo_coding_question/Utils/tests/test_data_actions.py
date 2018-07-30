from unittest import TestCase

from jumo_coding_question.Utils.data_actions import (
    CreateDictFromCSVData,
    AnalyzeData,
)


class TestCreateDictFromCSVData(TestCase):
    """
    Test cases for parsing read csv file and creating a list of row_dictionaries
    from it.
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

    def test_ListTupleDataToDict(self):
        csv_file_data = ["Name,ID\n", "James,18712\n", "John,209928\n"]
        self.assertListEqual(
            CreateDictFromCSVData.ListTupleDataToDict(csv_file_data),
            [
                {"Name": "James", "ID": "18712"},
                {"Name": "John", "ID": "209928"},
            ],
        )


class TestAnalyzeData(TestCase):
    """
    Test cases for aggregating data.
    """

    def setUp(self):
        self.row_dictionaries = [
            {
                "Product": "M-Banking",
                "Network": "Z-network",
                "Date": "18-Mar-2014",
                "Amount": 1000.00,
            },
            {
                "Product": "M-Banking",
                "Network": "Y-network",
                "Date": "12-Apr-2014",
                "Amount": 1500.00,
            },
            {
                "Product": "M-Banking",
                "Network": "Z-network",
                "Date": "24-Mar-2014",
                "Amount": 2000.00,
            },
        ]
        new_instance = AnalyzeData(self.row_dictionaries)
        self.analysis_list_dictionary = new_instance.analyze()

    def test_analyze(self):
        self.assertListEqual(
            self.analysis_list_dictionary,
            [
                {
                    "Product": "M-Banking",
                    "Network": "Z-network",
                    "Month": "Mar",
                    "Count": 2,
                    "Aggregated Amount": 3000.00,
                },
                {
                    "Product": "M-Banking",
                    "Network": "Y-network",
                    "Month": "Apr",
                    "Count": 1,
                    "Aggregated Amount": 1500.00,
                },
            ],
        )

    def test_get_months(self):
        row_dictionaries = [
            {"Name": "James", "ID": "18712", "Date": "18-Mar-2016"},
            {"Name": "John", "ID": "209928", "Date": "12-Apr-2016"},
        ]
        self.assertTrue(
            "Month" in AnalyzeData.get_months(row_dictionaries)[0].keys()
        )
        self.assertTrue(
            "Month" in AnalyzeData.get_months(row_dictionaries)[1].keys()
        )

    def test_get_all_combinations(self):
        row_dictionaries = [
            {"Product": "M-Banking", "Network": "Z-network", "Month": "Mar"},
            {"Product": "M-Banking", "Network": "Z-network", "Month": "Mar"},
        ]
        self.assertListEqual(
            AnalyzeData.get_all_combinations(row_dictionaries),
            [
                ("M-Banking", "Z-network", "Mar", 0, 0),
                ("M-Banking", "Z-network", "Mar", 0, 0),
            ],
        )

    def test_get_unique_combinations(self):
        combinations = [
            ("M-Banking", "Z-network", "Mar", 0, 0),
            ("M-Banking", "Z-network", "Mar", 0, 0),
        ]
        self.assertListEqual(
            AnalyzeData.get_unique_combinations(combinations),
            [("M-Banking", "Z-network", "Mar", 0, 0)],
        )

    def test_aggregate(self):
        updated_row_dictionaries = [
            {
                "Product": "M-Banking",
                "Network": "Z-network",
                "Month": "Mar",
                "Amount": 1000.00,
            },
            {
                "Product": "M-Banking",
                "Network": "Y-network",
                "Month": "Apr",
                "Amount": 1500.00,
            },
            {
                "Product": "M-Banking",
                "Network": "Z-network",
                "Month": "Mar",
                "Amount": 2000.00,
            },
        ]
        unique_combinations = [
            ("M-Banking", "Z-network", "Mar", 0, 0),
            ("M-Banking", "Y-network", "Apr", 0, 0),
        ]
        self.assertTupleEqual(
            AnalyzeData.aggregate(updated_row_dictionaries, unique_combinations),
            (
                [
                    ("M-Banking", "Z-network", "Mar", 2, 3000),
                    ("M-Banking", "Y-network", "Apr", 1, 1500),
                ],
                ("Product", "Network", "Month", "Count", "Aggregated Amount"),
            ),
        )
