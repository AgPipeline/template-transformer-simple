"""Contains transformer configuration information
"""
from agpypeline.configuration import Configuration


class ConfigurationInfo(Configuration):
    """Configuration information"""
    # pylint: disable=too-few-public-methods
    # The version number of the transformer
    transformer_version = '1.0'

    # The transformer description
    transformer_description = ''

    # Short name of the transformer
    transformer_name = ''

    # The sensor associated with the transformer
    transformer_sensor = ''

    # The transformer type (eg: 'rgbmask', 'plotclipper')
    transformer_type = ''

    # The name of the author of the extractor
    author_name = ''

    # The email of the author of the extractor
    author_email = ''

    # Contributors to this transformer
    contributors = []

    # Repository URI of where the source code lives
    repository = ''

    # Hard-coded override of base docker image (used when Dockerfile is generated)
    # If a name is entered here it will be used to populate the "FROM" field of the Dockerfile
    base_docker_image_override_name = ''
