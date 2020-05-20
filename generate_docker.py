#!/usr/bin/env python3

"""Generated Dockerfile from a template
"""

import argparse
import configuration

# The template file name for Dockerfile
DOCKERFILE_TEMPLATE_FILE_NAMES = ["Dockerfile.template"]

# The default docker image to use
DEFAULT_DOCKER_IMAGE = 'agdrone/drone-base-image:1.2'

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
    if hasattr(configuration, "BASE_DOCKER_IMAGE_OVERRIDE_NAME"):
        static_override = getattr(configuration, "BASE_DOCKER_IMAGE_OVERRIDE_NAME")

    return static_override if static_override else args.base_image

def generate_dockerfile(base_image_name: str) -> None:
    """Generates a Dockerfile file using the configured information
    """
    # pylint: disable=global-statement
    global DOCKERFILE_TEMPLATE_FILE_NAMES

    missing = []
    if not hasattr(configuration, 'TRANSFORMER_NAME') or not configuration.TRANSFORMER_NAME:
        missing.append("Transformer name")
    if not hasattr(configuration, 'AUTHOR_NAME') or not configuration.AUTHOR_NAME:
        missing.append("Author name")
    if not hasattr(configuration, 'AUTHOR_EMAIL') or not configuration.AUTHOR_EMAIL:
        missing.append("Author email")
    if missing:
        raise RuntimeError("One or more configuration fields aren't defined in configuration.py: "
                           + ", ".join(missing))

    new_name = configuration.TRANSFORMER_NAME.strip().replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_')
    extractor_name = new_name.lower()

    for template_name in DOCKERFILE_TEMPLATE_FILE_NAMES:
        template = [line.rstrip('\n') for line in open(template_name, "r")]
        template_len = len('.template')
        dockerfile_name = template_name[:(template_len * -1)]
        with open(dockerfile_name, 'w') as out_file:
            for line in template:
                if line.startswith('LABEL maintainer='):
                    out_file.write("LABEL maintainer=\"{0} <{1}>\"\n".format(configuration.AUTHOR_NAME,
                                                                             configuration.AUTHOR_EMAIL))
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
