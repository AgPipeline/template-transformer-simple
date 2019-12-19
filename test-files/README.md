# Transformer Unit Tests
This folder holds the unit tests [TravisCI](https://travis-ci.org/) will run in it's build. 
These are basic functional unit tests, checks for output formatting and typing. 
All tests are written in and utilizing [pytest](https://docs.pytest.org/en/latest/). 
In addition to this, [pylint](https://www.pylint.org/) will also be deployed. 
Look into our organization's repository for our [pylint protocols](https://github.com/AgPipeline/Organization-info).

### Running the tests
Upon submitting a pull request Travis will build and run the testing modules automatically and return a report with passing and failing code. 

### Running the tests before submitting a pull request
Should you wish to test your code before submitting a pull request follow these steps:
1) Clone, pull, copy or otherwise aquire the pylintrc file located at this [repo](https://github.com/AgPipeline/Organization-info)
2) From the command line run the following commands (from test-transformer-simple) as current directory)
    ```sh
    pylint --rcfile=<path-to-pylint.rc> *py
    pylint --rcfile=<path-to-pylint.rc> /**/*.py
    ```
3) Once the previous commands have executed there will be a list of changes that should be made to bring any code up to standard
4) From the command line run the following command while the current working directory is still test-transformer-simple
    ```sh
    python -m pytest -v
    ```
    or
    ```sh
    python3 -m pytest -v
    ```

### Requirements 
These are the requirements needed when ruinning the tests locally. 

python 3 \
pylint \
pytest

All three may be installed using pip, conda, or another preferred method.
