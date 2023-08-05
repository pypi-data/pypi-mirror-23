from __future__ import absolute_import

import sys
import yaml

import cucco.logging as logging

from cucco.errors import ConfigError

DEFAULT_NORMALIZATIONS = [
    'replace_punctuation',
    'remove_extra_white_spaces',
    'replace_symbols',
    'remove_stop_words'
]
STR_TYPE = str if sys.version_info[0] > 2 else (str, unicode)


class Config(object):
    """Class to manage cucco configuration.

    This class allows to handle all cucco configuration and is
    used by the different modules.

    Attributes:
        debug: Whether to show debug messages or not.
        language: Language to be used for the normalizations.
        normalizations: List or path to config file.
        verbose: Level of output verbosity.
    """

    normalizations = DEFAULT_NORMALIZATIONS

    def	__init__(self,
                 normalizations=None,
                 language='en',
                 logger=None,
                 debug=False,
                 verbose=False):
        """Inits Config class."""
        self.debug = debug
        self.language = language
        self.logger = logger or logging.initialize_logger(debug)
        self.verbose = verbose or debug

        if normalizations:
            if isinstance(normalizations, STR_TYPE):
                normalizations = self._load_from_file(normalizations)

            self.normalizations = self._parse_normalizations(normalizations)

    @staticmethod
    def _load_from_file(path):
        """Load a config file from the given path.

        Load all normalizations from the config file received as
        argument. It expects to find a YAML file with a list of
        normalizations and arguments under the key 'normalizations'.

        Args:
            path: Path to YAML file.
        """
        config = []

        try:
            with open(path, 'r') as config_file:
                config = yaml.load(config_file)['normalizations']
        except EnvironmentError as e:
            raise ConfigError('Problem while loading file: %s' %
                              e.args[1] if len(e.args) > 1 else e)
        except (TypeError, KeyError) as e:
            raise ConfigError('Config file has an unexpected structure: %s' % e)
        except yaml.YAMLError:
            raise ConfigError('Invalid YAML file syntax')

        return config

    @staticmethod
    def _parse_normalization(normalization):
        """Parse a normalization item.

        Transform dicts into a tuple containing the normalization
        options. If a string is found, the actual value is used.

        Args:
            normalization: Normalization to parse.

        Returns:
            Tuple or string containing the parsed normalization.
        """
        parsed_normalization = None

        if isinstance(normalization, dict):
            if len(normalization.keys()) == 1:
                items = list(normalization.items())[0]
                if len(items) == 2: # Two elements tuple
                    # Convert to string if no normalization options
                    if items[1] and isinstance(items[1], dict):
                        parsed_normalization = items
                    else:
                        parsed_normalization = items[0]
        elif isinstance(normalization, STR_TYPE):
            parsed_normalization = normalization

        return parsed_normalization

    def _parse_normalizations(self, normalizations):
        """Returns a list of parsed normalizations.

        Iterates over a list of normalizations, removing those
        not correctly defined. It also transform complex items
        to have a common format (list of tuples and strings).

        Args:
            normalizations: List of normalizations to parse.

        Returns:
            A list of normalizations after being parsed and curated.
        """
        parsed_normalizations = []

        if isinstance(normalizations, list):
            for item in normalizations:
                normalization = self._parse_normalization(item)
                if normalization:
                    parsed_normalizations.append(normalization)
        else:
            raise ConfigError('List expected. Found %s' % type(normalizations))

        return parsed_normalizations
