import logging


logger = logging.getLogger(__name__)


class CreateDictFromCSVData(object):
    """
    Convert csv data which is in list format to python dict.
    """

    @classmethod
    def dictify_column_head_and_columns(cls, head, data):
        return [
            dict(zip(head, row_data))
            for row_data in data
            if len(head) == len(row_data)
        ]

    @classmethod
    def split_columns(cls, csv_lines):
        # get and parse the column headers
        head = (
            csv_lines[0][:-1].replace("'", "").replace("\r", "").replace(
                "\n", ""
            ).replace(
                "\r\n", ""
            ).split(
                ","
            )
        )
        # get and parse the column data
        data = [
            each[:-1].replace("'", "").replace("\r", "").replace(
                "\n", ""
            ).replace(
                "\r\n", ""
            ).split(
                ","
            )
            for each in csv_lines[1:]
        ]

        return head, data

    @classmethod
    def ListTupleDataToDict(cls, list_tuple_data, headers=None):
        if not headers:
            column_heads, row_data = cls.split_columns(list_tuple_data)
            row_dictionaries = cls.dictify_column_head_and_columns(
                column_heads, row_data
            )
        else:
            row_dictionaries = cls.dictify_column_head_and_columns(
                headers, list_tuple_data
            )

        return row_dictionaries


class AnalyzeData(object):

    def __init__(self, row_dictionaries):
        self.row_dictionaries = AnalyzeData.get_months(row_dictionaries)
        self.unique_combinations = AnalyzeData.get_unique_combinations(
            AnalyzeData.get_all_combinations(self.row_dictionaries)
        )

    def analyze(self):
        column_heads, row_data = AnalyzeData.aggregate(
            self.row_dictionaries, self.unique_combinations
        )
        return CreateDictFromCSVData.ListTupleDataToDict(
            column_heads, row_data
        )

    @classmethod
    def get_months(cls, row_dictionaries):
        [
            each.update({"Month": each["Date"].split("-")[1]})
            for each in row_dictionaries
        ]
        return row_dictionaries

    @classmethod
    def get_all_combinations(cls, row_dictionaries):
        combinations = [
            (each["Product"], each["Network"], each["Month"], 0, 0)
            for each in row_dictionaries
        ]
        return combinations

    @classmethod
    def get_unique_combinations(cls, combinations):
        unique_combinations = []
        [
            unique_combinations.append(each)
            for each in combinations
            if each not in unique_combinations
        ]
        return unique_combinations

    @classmethod
    def aggregate(cls, row_dictionaries, unique_combinations):
        list_unique_combinations = [list(each) for each in unique_combinations]
        for unique in range(len(list_unique_combinations)):
            for each in row_dictionaries:
                if (
                    each["Product"] == list_unique_combinations[unique][0]
                    and each["Network"] == list_unique_combinations[unique][1]
                    and each["Month"] == list_unique_combinations[unique][2]
                ):
                    list_unique_combinations[unique][3] = (
                        list_unique_combinations[unique][3] + 1
                    )
                    list_unique_combinations[unique][
                        4
                    ] = list_unique_combinations[
                        unique
                    ][
                        4
                    ] + float(
                        each["Amount"]
                    )
        unique_combinations_updated = [
            tuple(each) for each in list_unique_combinations
        ]
        return (
            unique_combinations_updated,
            ("Product", "Network", "Month", "Count", "Aggregated Amount"),
        )
