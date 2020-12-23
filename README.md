![license](https://img.shields.io/badge/license-BSD%203-green?logo=Open-Source-Initiative)

![testing](https://github.com/AgPipeline/template-transformer-simple/workflows/Enforcing%20testing%20checks/badge.svg)

# Transformer Template

This repository is a template for creating Transformer which perform work on one or more files at a time.
Transformers using this template may be used as an integral part of a workflow containing other Transformers and processes.
Transformers are intended to be compatible with workflows on a single system or distributed.

This template is for general purpose use and isn't tied to a particular sensor or file type.
It can be used to process RGB images, Lidar data, perform ML tasks, call out to other applications, etc.

This templated Transformer allows developers to focus on their algorithm by isolating the processing logic from the infrastructure needed for a workflow. 

## Quick Start

To use this template:
1. Clone this template into a new repository
2. Fill out the `configuration.py` file with your information. Feel free to add additional variables.
3. Add your code to the `transformer.py` file, filling in the *add_parameters* (optional), *check_continue* (also optional), and *perform_process* functions. The optional functions can be deleted from the file
4. Run the `generate-docker.py` script to generate your Dockerfile for building images
5. Modify the Dockerfile as needed and build a Docker image for your transformer

You can fill in the BASE_DOCKER_IMAGE_OVERRIDE_NAME variable in `configuration.py` to specify an alternative base Docker image to use for your Transformer.

For your transformer to be accepted, be sure to have test cases and continuous integration (CI) setup.
To assist in this task, this repository provides a basic [PyTest](https://docs.pytest.org/en/stable/) test file and [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions) YAML file which run [PyLint](https://www.pylint.org/) and PyTest as part of CI.

Please be sure to understand how to contribute by reading the documents in our [main repository](https://github.com/AgPipeline/Organization-info).

## Example

In this example we're going to develop a Transformer that returns the sum of two integers.

This example assumes the `agpypeline` library has been installed.
The following command can be used install the latest version of the library for Python3.7 or later:
```shell script
python -m pip install -U agpypeline
```

#### Step 1 - Clone the repository

This can be done in a variety of ways.
We recommend using the GitHub method as defined in their [documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).

#### Step 2 - Update configuration file

Open `configuration.py` in your favorite editor, fill in the values, and save your changes.

Below is an example of what the edited file might look like.
The variables should be assigned meaningful values for your Transformer.
```python
"""Contains transformer configuration information
"""
from agpypeline.configuration import Configuration

class ConfigurationInfo(Configuration):
    """Configuration information"""
    # pylint: disable=too-few-public-methods
    # The version number of the transformer
    transformer_version = '1.0'

    # The transformer description
    transformer_description = 'Adds two numbers'

    # Short name of the transformer
    transformer_name = 'adder'

    # The sensor associated with the transformer
    transformer_sensor = 'None'

    # The transformer type (eg: 'rgbmask', 'plotclipper')
    transformer_type = 'addition'

    # The name of the author of the extractor
    author_name = 'Jo Programmer'

    # The email of the author of the extractor
    author_email = 'jo.programmer@somewhere.edu'

    # Contributors to this transformer
    contributors = []

    # Repository URI of where the source code lives
    repository = 'https://github.com/joprogrammer/adder'

    # Hard-coded override of base docker image (used when Dockerfile is generated)
    # If a name is entered here it will be used to populate the "FROM" field of the Dockerfile
    base_docker_image_override_name = ''

```

#### Step 3 - Rename the class

Open `transformer.py` in your favorite editor and make the changes you need.

We will rename the class to something meaningful.
```python
class Adder(algorithm.Algorithm):
```

#### Step 4 - Add the parameters we need

Continuing our modifications to `transformer.py`, we'll add our two parameters in the *add_parameters* function by adding [argparse](https://docs.python.org/3/library/argparse.html) parameters.
A benefit of using argparse is that it will check the parameter types for us ensuring we're getting two integers.

```python
class Adder(algorithm.Algorithm):

    def add_parameters(self, parser: argparse.ArgumentParser) -> None:
        """Adds parameters
        Arguments:
            parser: instance of argparse.ArgumentParser
        """
        # pylint: disable=unused-argument, no-self-use
        parser.add_argument('first_number', type=int, help='First number to add')
        parser.add_argument('second_number', type=int, help='Second number to add')
```

#### Step 5 - Add our algorithm

We finish up editing `transformer.py` by adding our algorithm to the *perform_process* function.
We will be returning the sum as part of our return JSON.

```python
class Adder(algorithm.Algorithm):
    # add_parameters() code folded so we can't see it

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

        # Add the two numbers and print and return the sum
        sum_value = environment.args.first_number + environment.args.second_number
        return {'code': 0,
                'sum': sum_value,
                'message': "Everything is going swimmingly"}
```

Be sure to save all your changes.

#### Step 6 - Test the script

In this step we will run our script passing it two integers.
We are going to use python to run the script although it's possible to run the script directly from the command line.
You may also be able to run the script from your editor.

```shell script
python3 transformer.py --result print 1 2
```

This will display the result of the addition as output:
```json
{
  "code": 0,
  "sum": 3,
  "message": "Everything is going swimmingly"
}
```
The parameter `--result print` specifies the the result JSON should be printed and not stored in a file.

The displayed JSON contains the key 'sum' and its associated value that's the result of the addition.

#### Step 7 - Create Docker image

We don't need to create a Docker image to use our Transformer we're going to create one anyway to show how it's done.

Generate the Dockerfile file by running `generate_docker.py`.
We're going to use two different ways of running this script.

From the command line run:
```shell script
# Run the script directly, first making sure it's execute bit is set
chmod +x generate_docker.py && ./generate_docker.py
```
or 
```shell script
# Run the script using python
python generate_docker.py
```

There is now a file named `Dockerfile` in the folder.
We can use this to build the Docker image with our algorithm.
Refer to the [Docker build](https://docs.docker.com/engine/reference/commandline/build/) documentation for more information.

The following command creates a Docker image named __adder:latest__.
```shell script
docker build -t adder ./
```

To test the Docker image we can run it with the following command.
Refer to the [Docker run](https://docs.docker.com/engine/reference/commandline/run/) documentation for more information.

The following command will run the Docker image we just built:
```shell script
docker run --rm adder --result print 4 4
```

The following JSON will be printed:
```json
{
  "code": 0,
  "sum": 8,
  "message": "Everything is going swimmingly"
}
```

The parameter `--result print` causes the resulting JSON to be printed (and not stored in a file).

The displayed JSON contains the key 'sum' and its associated value that's the result of the addition.

#### Step 8 - Finishing up

Be sure to save your changes to your source control repository. 

## Extending the Template

This section assumes familiarity with our [Template concepts](https://agpipeline.github.io/).

There are situations where this template won't be sufficient as a transformer for an environment.
In these cases it's recommended that instead of forking this repo and making modifications, a new template repo is created with the expectation that the processing code will be a submodule to it.
Scripts and/or instructions can then be provided on cloning this repo, specifying the submodule, and how to create a working transformer for the environment.

The benefit of this approach is that the processing code can be updated in its original repo, and a clear update path is available to create an updated transformer for the environment.
Another benefit is the clean separation of the processing logic and the environment via separate repos.

A drawback is that there may be a proliferation of repos.
