from unittest import TestCase

from jumo_coding_question.config import Config


class TestConfigAttributes(TestCase):
    def setUp(self):
        self.configurations = Config()

    def tearDown(self):
        self.configurations = None

    def test_config_has_values(self):
        configurations = Config()
        self.assertTrue(hasattr(configurations, "LOGS_DIRECTORY"))
        self.assertTrue(hasattr(configurations, "INPUTS_DIRECTORY"))
        self.assertTrue(hasattr(configurations, "OUTPUTS_DIRECTORY"))
        self.assertIsNotNone(configurations.LOGS_DIRECTORY)
        self.assertIsNotNone(configurations.INPUTS_DIRECTORY)
        self.assertIsNotNone(configurations.OUTPUTS_DIRECTORY)
