"""Testing files for transformer.py
"""

# Import transformer.py and embedded modules
import argparse
import transformer
import transformer_class

# Setting up some testing classes
TEST_TRANSFORMER = transformer_class.Transformer()
PARSE = argparse.ArgumentParser()

# pylint: disable=assignment-from-no-return
def test_add_parameters():
    """Test for add_parameters function
    """

    # Saving method call to variable
    test_params = transformer.add_parameters(PARSE)

    # Should return None
    assert test_params is None

def test_check_continue():
    """Test for check_continue function
    """

    # Creating testing metadata dict arguments
    test_md = {}
    test_transformer_md = {}
    test_full_md = {}

    # Saving function call to variable
    test_check = transformer.check_continue(TEST_TRANSFORMER, test_md, test_transformer_md, test_full_md)

    # Should return a list type
    assert isinstance(test_check, list)

def test_perform_process():
    """Test for perform_process function
    """

    # Creating testing metadata dict arguments
    test_md = {}
    test_transformer_md = {}
    test_full_md = {}

    # Saving function call to variable
    test_process = transformer.perform_process(TEST_TRANSFORMER, test_md, test_transformer_md, test_full_md)

    # Should return dict type
    assert isinstance(test_process, dict)

