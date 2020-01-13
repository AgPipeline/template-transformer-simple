"""My nifty transformer
"""

import argparse
import transformer_class

# pylint: disable=unused-argument
def add_parameters(parser: argparse.ArgumentParser) -> None:
    """Adds parameters
    Arguments:
        parser: instance of argparse.ArgumentParser
    """

def check_continue(transformer: transformer_class.Transformer, check_md: dict, transformer_md: list, full_md: list) -> tuple:
    """Checks if conditions are right for continuing processing
    Arguments:
        transformer: instance of transformer class
        check_md: request specific metadata
        transformer_md: metadata associated with previous runs of the transformer
        full_md: the full set of metadata available to the transformer
    Return:
        Returns a tuple containing the return code for continuing or not, and
        an error message if there's an error
    """
    print("check_continue(): received arguments: %s" % str(check_md))
    return 0

def perform_process(transformer: transformer_class.Transformer, check_md: dict, transformer_md: list, full_md: list) -> dict:
    """Performs the processing of the data
    Arguments:
        transformer: instance of transformer class
        check_md: request specific metadata
        transformer_md: metadata associated with previous runs of the transformer
        full_md: the full set of metadata available to the transformer
    Return:
        Returns a dictionary with the results of processing
    """
    print("perform_process(): received arguments: %s" % str(check_md))
    return {'code': 0, 'message': "Everything is going swimmingly"}
