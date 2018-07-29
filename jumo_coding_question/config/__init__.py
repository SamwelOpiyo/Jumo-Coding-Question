import os


class Config(object):
    LOGS_DIRECTORY = os.environ.get("LOGS_DIRECTORY", "logs/")
    INPUTS_DIRECTORY = os.environ.get("INPUTS_DIRECTORY", "inputs/")
    OUTPUTS_DIRECTORY = os.environ.get("OUTPUTS_DIRECTORY", "outputs/")
