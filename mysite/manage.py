#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import logging
#
#
# def setup_logging():
#     file_handler = logging.FileHandler('/home/alex/Documents/Projects/battleShip/env1/debug.log')
#     formatted = logging.Formatter("[%(asctime)s] - %(levelname)s - %(message)s")
#     file_handler.setFormatter(fmt=formatted)
#     file_handler.setLevel(level=logging.DEBUG)
#
#     root_handler = logging.getLogger()
#     root_handler.addHandler(hdlr=file_handler)
#     root_handler.setLevel(level=logging.DEBUG)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # setup_logging()
    main()
