# Transformer Unit Tests
This folder holds the unit tests [TravisCI](https://travis-ci.org/) will run in it's build. These are basic functional unit tests, checks for output formatting and typing. All tests are written in and utilizing [pytest](https://docs.pytest.org/en/latest/). In addition to this, [pylint](https://www.pylint.org/) will also be deployed.

### Running the tests
Upon submitting a pull request Travis will build and run the testing modules automatically and should return a report with all passing or failing code. 

### Running the tests before submitting a pull request
Should you wish to test your code before submitting a pull request follow these steps
1) Clone, pull, copy or otherwise aquire the pylintrc file located [here](https://github.com/AgPipeline/Organization-info)
2) From the command line run the following commands (from test-transformer-simple) as current directory) \
    ```pylint --rcfile=<path-to-pylint.rc> base-image/*py``` \
    ```pylint --rcfile=<path-to-pylint.rc> base-image/**/*py```
3) Once the previous commands have executed there should be a list of changes that should be made to bring any code up to standard
4) From the command line run the following command while the current working directory is still test-transformer-simple \
    ```python -m pytest -v``` \
    or \
    ```python3 -m pytest -v```

### Requirements 
There are no additional requirements or dependancies if not running these tests locally, if however these are to be run before deploying travis the following are required. 

python 3 \
pylint \
pytest

All three may be installed using pip or conda.