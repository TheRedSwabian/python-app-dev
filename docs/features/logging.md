# Logging != print()

Logging records the flow of a program, including its errors and exceptions, to the console and to a file at once. It is more than printing.

## Usage

Call `setup_logger` once at startup, then use the shared `logger` everywhere. The `time_it` decorator logs how long a function takes:

```python
from pathlib import Path

from py_app_dev.core.logging import logger, setup_logger, time_it


@time_it()
def build() -> None:
    logger.info("building ...")


setup_logger(Path("build.log"))  # console + file
build()
```

### Code location in the console

By default a console log line carries only the timestamp, the level and the message:

```text
2026-03-24 11:18:16.429 | INFO     | building ...
```

Pass `show_code_location=True` to prefix every line with the module, the function and the line number that logged it. This helps while debugging and is noise in a build log:

```python
setup_logger(show_code_location=True)
```

```text
2026-03-24 11:18:16.429 | INFO     | my_app.builder:build:12 - building ...
```

The log file is not affected by this option. A log file is read for debugging, so it always keeps the code location.

## Requirements

```{item} REQ-LOGGING_FILE-0.0.1 Print to file

   Print the log messages both to the console and to a file.
   The user **shall** be able to specify the log file path.
```

```{item} REQ-LOGGING_CODE_LOCATION-0.0.1 Configurable code location

   Print the code location (module, function and line number) in the console log only on request.
   The user **shall** be able to enable or disable it. It **shall** be disabled by default.
```

```{item} REQ-LOGGING-2.0.0 Easy Setup and Use

   Be easy to set up and use across all modules.
```

```{item} REQ-LOGGING-3.0.0 Handle Custom Exceptions

   Be capable of handling and logging custom exceptions.
```

```{item} REQ-LOGGING-4.0.0 Console Error Visibility

   Ensure error messages are clearly visible in the console, for instance, by printing them in red.
```

```{item} REQ-LOGGING-5.0.0 Special Error Log File

   Maintain a special log file specifically for error messages.
```

```{item} REQ-LOGGING-6.0.0 Log File Rotation

   Rotate log files, preserving the last two or three files before discarding older ones.
```

```{item} REQ-LOGGING_TIME_IT-0.0.1 Timing Methods

   Support special methods for timing and logging the execution of code blocks.

```

:::{note}
This module is built on the [loguru](https://github.com/Delgan/loguru) logging library.
:::

## Current Status

```{eval-rst}
.. item-matrix:: Traceability matrix
    :source: REQ-LOGGING
    :target: IMPL [IU]TEST
    :sourcetitle: Requirement
    :targettitle: Implementation, Test Cases
    :stats:
```
