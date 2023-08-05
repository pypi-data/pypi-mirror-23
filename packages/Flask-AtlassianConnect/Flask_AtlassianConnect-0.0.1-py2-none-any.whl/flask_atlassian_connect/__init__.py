__version__ = '0.0.1'
__url__ = 'https://github.com/halkeye/flask_atlassian_connect'
__author__ = 'Gavin Mogan'
__email__ = 'opensource@gavinmogan.com'
__all__ = ['base', 'default_client']

from .base import AtlassianConnect  # NOQA: E402, F401, C0413
from .client import AtlassianConnectClient  # NOQA: E402, F401, C0413
