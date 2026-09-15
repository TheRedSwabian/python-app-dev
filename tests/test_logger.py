from pathlib import Path

import pytest

from py_app_dev.core.docs_utils import validates
from py_app_dev.core.logging import create_log_format, log_to_file, logger, setup_logger, time_it


@pytest.fixture
def console_capture(capsys):
    """Capture the console log output and detach the sink afterwards, so that later tests do not write into a closed stream."""
    yield capsys
    logger.remove()


@pytest.mark.parametrize("show_code_location", [True, False])
@validates("REQ-LOGGING_CODE_LOCATION-0.0.1")
def test_create_log_format(show_code_location):
    log_format = create_log_format(show_code_location)
    assert ("{name}" in log_format) is show_code_location
    assert ("{function}" in log_format) is show_code_location
    assert ("{line}" in log_format) is show_code_location
    assert "{message}" in log_format


@pytest.mark.parametrize("show_code_location", [True, False])
@validates("REQ-LOGGING_CODE_LOCATION-0.0.1")
def test_setup_logger_code_location(console_capture, show_code_location):
    setup_logger(show_code_location=show_code_location)
    logger.info("Detecting C compiler ABI info")
    console_output = console_capture.readouterr().out
    assert "Detecting C compiler ABI info" in console_output
    assert (":test_setup_logger_code_location:" in console_output) is show_code_location


@validates("REQ-LOGGING_CODE_LOCATION-0.0.1")
def test_setup_logger_hides_code_location_by_default(console_capture):
    setup_logger()
    logger.info("Detecting C compiler ABI info")
    console_output = console_capture.readouterr().out
    assert "Detecting C compiler ABI info" in console_output
    assert ":test_setup_logger_hides_code_location_by_default:" not in console_output


@validates("REQ-LOGGING_FILE-0.0.1")
def test_setup_logger(tmp_path):
    log_file = tmp_path / "test.log"
    setup_logger(log_file, clear=True)
    logger.debug("Test")
    assert log_file.exists()


@time_it("My cool function")
def _some_func() -> None:
    logger.debug("I am some_func")


@validates("REQ-LOGGING_TIME_IT-0.0.1")
def test_time_it(tmp_path):
    log_file = tmp_path / "test.log"
    setup_logger(log_file, clear=True)
    _some_func()
    log_text = log_file.read_text()
    assert "Starting My cool function" in log_text
    assert "I am some_func" in log_text


@time_it()
def _some_other_func(my_arg: str) -> None:
    logger.debug(f"Input arg is {my_arg}")


@validates("REQ-LOGGING_TIME_IT-0.0.1")
def test_time_it_without_arguments(tmp_path):
    log_file = tmp_path / "test.log"
    setup_logger(log_file, clear=True)
    _some_other_func("123")
    log_text = log_file.read_text()
    assert "tests.test_logger._some_other_func" in log_text


class MyClass:
    def __init__(self, log_file: Path):
        self.logger = logger.bind()
        self.log_file = log_file

    @time_it()
    def run(self):
        with log_to_file(self.log_file, self.logger):
            self.logger.debug("I am in the log file")
        self.logger.debug("Not in the log file")


def test_log_with_file(tmp_path):
    log_file = tmp_path / "test.log"
    MyClass(log_file).run()
    log_text = log_file.read_text()
    assert "I am in the log file" in log_text
    assert "Not in the log file" not in log_text


def test_log_with_file_default_logger(tmp_path):
    log_file = tmp_path / "test.log"
    with log_to_file(log_file) as new_logger:
        new_logger.debug("I am in the log file")
    log_text = log_file.read_text()
    assert "I am in the log file" in log_text
