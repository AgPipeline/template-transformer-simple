#!/usr/bin/env python3
"""Tests plotclip.py
"""
import argparse
import os
import re
from subprocess import getstatusoutput

from agpypeline.environment import Environment

from configuration import ConfigurationInfo

# The name of the source file to test and it's path
SOURCE_FILE = 'transformer.py'
SOURCE_PATH = os.path.abspath(os.path.join('.', SOURCE_FILE))

# Path relative to the current folder where the testing data files are
TESTING_JSON_FILE_PATH = './test_data'


def test_exists():
    """Asserts that the source file is available"""
    assert os.path.isfile(SOURCE_PATH)


def test_usage():
    """Program prints a "usage" statement when requested"""
    for flag in ['-h', '--help']:
        ret_val, out = getstatusoutput(f'{SOURCE_PATH} {flag}')
        assert re.match('usage', out, re.IGNORECASE)
        assert ret_val == 0


def test_add_parameters():
    """Checks that the add_parameters function is callable without error"""
    # pylint: disable=import-outside-toplevel
    from transformer import TemplateTransformer as tt

    new_tt = tt()
    arg_parser = argparse.ArgumentParser()
    new_tt.add_parameters(arg_parser)


def test_check_continue():
    """Checks that the check_continue function is callable without error"""
    # pylint: disable=import-outside-toplevel
    from transformer import TemplateTransformer as tt

    new_tt = tt()
    ret_val = new_tt.check_continue(Environment(ConfigurationInfo()),  {}, {}, [])

    assert ret_val == 0


def test_perform_process():
    """Checks that the perform_process function is callable without error"""
    # pylint: disable=import-outside-toplevel
    from transformer import TemplateTransformer as tt

    new_tt = tt()
    ret_val = new_tt.perform_process(Environment(ConfigurationInfo()),  {}, {}, [])

    assert 'code' in ret_val
    assert ret_val['code'] == 0
