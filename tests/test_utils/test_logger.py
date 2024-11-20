import logging
import unittest

from bot.utils.logger import setup_logger


class TestSetupLogger(unittest.TestCase):

    def test_logger_name(self):
        logger_name = "test_logger"
        logger = setup_logger(logger_name)
        self.assertEqual(logger.name, logger_name)

    def test_logger_level(self):
        logger_name = "test_logger"
        logger = setup_logger(logger_name, logging.DEBUG)
        self.assertEqual(logger.level, logging.DEBUG)

    def test_logger_has_stream_handler(self):
        logger_name = "test_logger"
        logger = setup_logger(logger_name)
        has_stream_handler = any(
            isinstance(handler, logging.StreamHandler) for handler in logger.handlers
        )
        self.assertTrue(has_stream_handler)

    def test_logger_formatter(self):
        logger_name = "test_logger"
        logger = setup_logger(logger_name)
        stream_handler = next(
            handler
            for handler in logger.handlers
            if isinstance(handler, logging.StreamHandler)
        )
        formatter = stream_handler.formatter
        self.assertIsInstance(formatter, logging.Formatter)
        self.assertEqual(
            formatter._fmt, "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )


if __name__ == "__main__":
    unittest.main()
