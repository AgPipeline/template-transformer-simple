"""My nifty transformer
"""

import argparse
from agpypeline import algorithm, entrypoint
from agpypeline.environment import Environment

from configuration import ConfigurationInfo


# Rename this class to something meaningful for your algorithm
class TemplateTransformer(algorithm.Algorithm):
    """Used  as base for simplified RGB transformers"""

    # Optional function that can be removed if not used
    def add_parameters(self, parser: argparse.ArgumentParser) -> None:
        """Adds parameters
        Arguments:
            parser: instance of argparse.ArgumentParser
        """
        # pylint: disable=unused-argument, no-self-use

    # Optional function that can be removed if not used
    def check_continue(self, environment: Environment, check_md: dict, transformer_md: dict, full_md: list) -> tuple:
        """Checks if conditions are right for continuing processing
        Arguments:
            environment: instance of environment class
            check_md: request specific metadata
            transformer_md: metadata associated with previous runs of the transformer
            full_md: the full set of metadata available to the transformer
        Return:
            Returns a tuple containing the return code for continuing or not, and
            an error message if there's an error
        """
        # pylint: disable=unused-argument, no-self-use

        # Replace the following lines with your code
        print("check_continue(): received arguments: %s" % str(check_md))
        return 0

    def perform_process(self, environment: Environment, check_md: dict, transformer_md: dict, full_md: list) -> dict:
        """Performs the processing of the data
        Arguments:
            environment: instance of environment class
            check_md: request specific metadata
            transformer_md: metadata associated with previous runs of the transformer
            full_md: the full set of metadata available to the transformer
        Return:
            Returns a dictionary with the results of processing
        """
        # pylint: disable=unused-argument, no-self-use

        # Replace the following lines with your implementation
        print("perform_process(): received arguments: %s" % str(check_md))
        return {'code': 0, 'message': "Everything is going swimmingly"}


if __name__ == "__main__":
    CONFIGURATION = ConfigurationInfo()
    entrypoint.entrypoint(CONFIGURATION, TemplateTransformer())
