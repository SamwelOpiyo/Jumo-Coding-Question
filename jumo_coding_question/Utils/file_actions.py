import os.path
import logging


logger = logging.getLogger(__name__)


class CSVFileRead(object):
    """
    Read CSV file into python lists
    """

    def __init__(self, filename):
        self.filename = filename

    def check(self):
        pass

    def read(self):
        return CSVFileRead.readfile(self.filename)

    @classmethod
    def does_file_exist(cls, file_):
        return os.path.isfile(file_)

    @classmethod
    def readfile(cls, file_):
        if CSVFileRead.does_file_exist(file_):
            with open(file_, "r") as csvfile:
                logger.debug("Opened File {}.".format(file_))
                return csvfile.readlines()
        else:
            logger.error("File {} does not exist!".format(file_))
            return None
