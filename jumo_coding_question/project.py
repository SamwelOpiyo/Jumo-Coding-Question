import logging.config
import sys

from jumo_coding_question.configurations import Config
from jumo_coding_question.configurations.logging_config import (
    get_logging_configuration
)
from jumo_coding_question.Utils import file_actions, data_actions


def run(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

    config_instance = Config()
    logging.config.dictConfig(get_logging_configuration(config_instance))

    file_contents = file_actions.CSVFileRead.readfile(
        config_instance.INPUTS_DIRECTORY + "Loans.csv"
    )

    if file_contents is None:
        logging.debug("Could not read file!")
        quit()

    data_items = data_actions.CreateDictFromCSVData.ListTupleDataToDict(
        file_contents
    )
    logging.debug(data_items)
    analysis_instance = data_actions.AnalyzeData(data_items)
    analysis_results = analysis_instance.analyze()
    logging.debug(data_items)
    if file_actions.CSVFileWrite.writefile(
        config_instance.OUTPUTS_DIRECTORY + "Output.csv", analysis_results
    ):
        logging.debug("Job finished successfully")
    else:
        logging.debug("Could not write to file!")


if __name__ == "__main__":
    run()
