"""Testing files for transformer.py
"""

#Import transformer.py and imbedded modules
import transformer
import argparse
import transformer_class

#Setting up some testing classes
test_transformer = transformer_class.Transformer()
test_parse = argparse.ArgumentParser

def test_add_parameters():
    """Test for add_parameters function
    """

    #Saving method call to variable
    test_params = transformer.add_parameters(test_parse)

    #Should return None
    assert test_params == None

def test_check_continue():
    """Test for check continue
    """

    #Creating testing metadata dict arguments
    test_md = {}
    test_transformer_md = {}
    test_full_md = {}

    #Saving function call to variable
    test_check = transformer.check_continue(test_transformer,test_md,\
        test_transformer_md, test_full_md)

    #Should return a list type
    assert isinstance(test_check,list)

def test_perform_process():
    """Test for perform_process function
    """

    #Creating testing metadata dict arguments
    test_md = {}
    test_transformer_md = {}
    test_full_md = {}

    #Saving function call to variable
    test_process = transformer.perform_process(test_transformer, test_md, test_transformer_md, test_full_md)

    #Should return dict type
    assert isinstance(test_process, dict)
    