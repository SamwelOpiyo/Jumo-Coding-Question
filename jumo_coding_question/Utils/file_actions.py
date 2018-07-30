import os.path
import logging


logger = logging.getLogger(__name__)


class CSVFileRead(object):
    """
    Read CSV file into python lists
    """

    def __init__(self, file_):
        self.filename = file_

    def check(self):
        pass

    def read(self):
        return CSVFileRead.readfile(self.file_)

    @classmethod
    def does_file_exist(cls, file_):
        return os.path.isfile(file_)

    @classmethod
    def readfile(cls, file_):
        if CSVFileRead.does_file_exist(file_):
            try:
                with open(file_, "r") as csvfile:
                    logger.debug("Opened File {}.".format(file_))
                    return csvfile.readlines()
            except Exception as err:
                logger.exception(err)
                return None
        else:
            logger.error("File {} does not exist!".format(file_))
            return None


class CSVFileWrite(object):
    """
    Write python dict data to CSV file.
    """

    def __init__(self, file_, dict_data):
        self.file_ = file_
        self.dict_data = dict_data

    def check(self):
        pass

    def write(self):
        return CSVFileRead.writefile(self.file_, self.dict_data)

    @classmethod
    def writefile(cls, file_, dict_data):
        try:
            with open(file_, "a") as csvfile:
                logger.debug("Writing to File {}.".format(file_))
                csvfile.write(",".join(map(str, dict_data[0].keys())) + "\n")
                csvfile.writelines(
                    [
                        ",".join(map(str, each.values())) + "\n"
                        for each in dict_data
                    ]
                )
            logger.debug("Data written to File {} successfully.".format(file_))
        except Exception as err:
            logger.exception(err)

        return True
