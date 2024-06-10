"""
Constants for APP setup such as Architectures, launch mode and path for enviroment variables
"""

ARCH_STREAMING_SERVERLESS_FUNCTION = "STREAMING_SERVERLESS_FUNCTION"
ARCH_BLOB = "BLOB"

PROD = "PROD"
DEV = "DEV"
TEST = "TEST"

ARCHITECTURE_ENV_NAME = "ARCH"
DEFAULT_ARCHITECTURE = ARCH_BLOB

SECRET_KEY_SIGN_ENV_NAME = "SECRET_KEY_SIGN"
MONGO_URI_ENV_NAME = "MONGO_URI"
SERVERLESS_FUNCTION_URL_ENV_NAME = "SERVERLESS_FUNCTION_URL"
ENV_VALUE_ENV_NAME = "ENV_VALUE"
