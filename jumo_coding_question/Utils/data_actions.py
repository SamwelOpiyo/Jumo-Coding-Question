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
        head = csv_lines[0][:-1].split(",")
        # get and parse the column data
        data = [
            each[:-1].replace("'", "").split(",") for each in csv_lines[1:]
        ]

        return head, data

    @classmethod
    def CSVDataToDict(cls, csv_lines):
        column_heads, row_data = cls.split_columns(csv_lines)
        dictionary = cls.dictify_column_head_and_columns(
            column_heads, row_data
        )

        return dictionary
