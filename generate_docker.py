#!/usr/bin/env python3

"""Generated Dockerfile from a template
"""

import argparse
from configuration import ConfigurationInfo

# The template file name for Dockerfile
DOCKERFILE_TEMPLATE_FILE_NAMES = ["Dockerfile.template"]

# The default docker image to use
DEFAULT_DOCKER_IMAGE = 'ubuntu:18.04'

def determine_base_image() -> str:
    """Determines the base image to use in the dockerfile
    Return:
        The name of the base image to use
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('base_image', nargs='?', default=DEFAULT_DOCKER_IMAGE,
                        help='the docker image to use as the base for this transformer (can also be set in configuration.py')

    args = parser.parse_args()

    # Check for a configuration override
    static_override = None
    if hasattr(ConfigurationInfo, "base_docker_image_override_name"):
        static_override = getattr(ConfigurationInfo, "base_docker_image_override_name")

    return static_override if static_override else args.base_image

def generate_dockerfile(base_image_name: str) -> None:
    """Generates a Dockerfile file using the configured information
    """
    # pylint: disable=global-statement
    global DOCKERFILE_TEMPLATE_FILE_NAMES

    missing = []
    if not hasattr(ConfigurationInfo, 'transformer_name') or not ConfigurationInfo.transformer_name:
        missing.append("Transformer name")
    if not hasattr(ConfigurationInfo, 'author_name') or not ConfigurationInfo.author_name:
        missing.append("Author name")
    if not hasattr(ConfigurationInfo, 'author_email') or not ConfigurationInfo.author_email:
        missing.append("Author email")
    if missing:
        raise RuntimeError("One or more configuration fields aren't defined in configuration.py: "
                           + ", ".join(missing))

    for template_name in DOCKERFILE_TEMPLATE_FILE_NAMES:
        template = [line.rstrip('\n') for line in open(template_name, "r")]
        template_len = len('.template')
        dockerfile_name = template_name[:(template_len * -1)]
        with open(dockerfile_name, 'w') as out_file:
            for line in template:
                if line.startswith('LABEL maintainer='):
                    out_file.write("LABEL maintainer=\"{0} <{1}>\"\n".format(ConfigurationInfo.author_name,
                                                                             ConfigurationInfo.author_email))
                elif line.startswith('FROM base-image'):
                    out_file.write("FROM {0}\n".format(base_image_name))
                else:
                    out_file.write("{0}\n".format(line))

# Make the call to generate the file
if __name__ == "__main__":
    print('Configuring Dockerfile')
    BASE = determine_base_image()
    print('Using base image "%s"' % BASE)
    generate_dockerfile(BASE)
