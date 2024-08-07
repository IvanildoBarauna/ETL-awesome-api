import os
import logging
import pytest

from etl.common.utils.logs import CustomLogger
from etl.common.utils.common import default_output_log_folder


@pytest.fixture
def setup_logger():
    return CustomLogger("test")


def test_custom_logger_contructor(setup_logger):  # pylint: disable=redefined-outer-name
    new_logger = setup_logger
    assert new_logger.module == "test"


def test_custom_logger(setup_logger):  # pylint: disable=redefined-outer-name
    new_logger = setup_logger
    logger = new_logger.logger()
    assert isinstance(logger, logging.Logger)


def test_make_file_log(setup_logger):  # pylint: disable=redefined-outer-name
    default_folder = default_output_log_folder()
    expected_file_log = "test.log"
    expected_path = f"{default_folder}{expected_file_log}"

    new_logger = setup_logger
    result_path = new_logger.make_file_log()

    assert result_path == expected_path
    assert os.path.isfile(expected_path)


def test_log_info(setup_logger):  # pylint: disable=redefined-outer-name
    new_logger = setup_logger

    assert new_logger.info("This test message.")


def test_log_error(setup_logger):  # pylint: disable=redefined-outer-name
    new_logger = setup_logger

    assert new_logger.error("This test message.")


def test_log_warning(setup_logger):  # pylint: disable=redefined-outer-name
    new_logger = setup_logger

    assert new_logger.warning("This test message.")
