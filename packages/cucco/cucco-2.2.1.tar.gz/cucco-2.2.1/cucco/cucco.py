from __future__ import absolute_import, unicode_literals

import codecs
import os
import re
import string
import sys
import unicodedata

import cucco.regex as regex

from cucco.config import Config

PATH = os.path.dirname(__file__)


class Cucco(object):
    """This class offers methods for text normalization.

    Attributes:
        config: Config to use.
        lazy_load: Whether or not to lazy load files.
    """
    __punctuation = set(string.punctuation)

    def __init__(
            self,
            config=None,
            lazy_load=False):
        self._config = config if config else Config()

        self._characters_regexes = dict()
        self._logger = self._config.logger
        self.__stop_words = dict()

        # Load stop words
        self._load_stop_words(self._config.language if lazy_load else None)

    def _load_stop_words(self, language=None):
        """Load stop words into __stop_words set.

        Stop words will be loaded according to the language code
        received during instantiation.

        Args:
            language: Language code.

        Returns:
            A boolean indicating whether a file was loaded.
        """
        self._logger.debug('Loading stop words')

        loaded = False

        if language:
            file_path = 'data/stop-' + language
            loaded = self._parse_stop_words_file(os.path.join(PATH, file_path))
        else:
            for file in os.listdir(os.path.join(PATH, 'data')):
                loaded = self._parse_stop_words_file(os.path.join(PATH, 'data', file)) or loaded

        return loaded

    @staticmethod
    def _parse_normalizations(normalizations):
        """Parse and yield normalizations.

        Parse normalizations parameter that yield all normalizations and
        arguments found on it.

        Args:
            normalizations: List of normalizations.

        Yields:
            A tuple with a parsed normalization. The first item will
            contain the normalization name and the second will be a dict
            with the arguments to be used for the normalization.
        """
        str_type = str if sys.version_info[0] > 2 else (str, unicode)

        for normalization in normalizations:
            yield (normalization, {}) if isinstance(normalization, str_type) else normalization

    def _parse_stop_words_file(self, path):
        """Load stop words from the given path.

        Parse the stop words file, saving each word found in it in a set
        for the language of the file. This language is obtained from
        the file name. If the file doesn't exist, the method will have
        no effect.

        Args:
            path: Path to the stop words file.

        Returns:
            A boolean indicating whether the file was loaded.
        """
        language = None
        loaded = False

        if os.path.isfile(path):
            self._logger.debug('Loading stop words in %s', path)

            language = path.split('-')[-1]

            if not language in self.__stop_words:
                self.__stop_words[language] = set()

            with codecs.open(path, 'r', 'UTF-8') as file:
                loaded = True
                for word in file:
                    self.__stop_words[language].add(word.strip())

        return loaded

    def normalize(self, text, normalizations=None):
        """Normalize a given text applying all normalizations.

        Normalizations to apply can be specified through a list of
        parameters and will be executed in that order.

        Args:
            text: The text to be processed.
            normalizations: List of normalizations to apply.

        Returns:
            The text normalized.
        """
        for normalization, kwargs in self._parse_normalizations(
                normalizations or self._config.normalizations):
            try:
                text = getattr(self, normalization)(text, **kwargs)
            except AttributeError as e:
                self._logger.debug('Invalid normalization: %s', e)


        return text

    @staticmethod
    def remove_accent_marks(text, excluded=None):
        """Remove accent marks from input text.

        This function removes accent marks in the text, but leaves
        unicode characters defined in the 'excluded' parameter.

        Args:
            text: The text to be processed.
            excluded: Set of unicode characters to exclude.

        Returns:
            The text without accent marks.
        """
        if excluded is None:
            excluded = set()

        return unicodedata.normalize(
            'NFKC', ''.join(
                c for c in unicodedata.normalize(
                    'NFKD', text) if unicodedata.category(c) != 'Mn' or c in excluded))

    @staticmethod
    def remove_extra_white_spaces(text):
        """Remove extra white spaces from input text.

        This function removes white spaces from the beginning and
        the end of the string, but also duplicates white spaces
        between words.

        Args:
            text: The text to be processed.

        Returns:
            The text without extra white spaces.
        """
        return ' '.join(text.split())

    def remove_stop_words(self, text, ignore_case=True, language=None):
        """Remove stop words.

        Stop words are loaded on class instantiation according
        to the specified language.

        Args:
            text: The text to be processed.
            ignore_case: Whether or not to ignore case.
            language: Code of the language to use (defaults to 'en').

        Returns:
            The text without stop words.
        """
        if not language:
            language = self._config.language

        if language not in self.__stop_words:
            if not self._load_stop_words(language):
                self._logger.error('No stop words file for the given language')
                return text

        return ' '.join(word for word in text.split(' ') if (
            word.lower() if ignore_case else word) not in self.__stop_words[language])

    def replace_characters(self, text, characters, replacement=''):
        """Remove characters from text.

        Removes custom characters from input text or replaces them
        with a string if specified.

        Args:
            text: The text to be processed.
            characters: Characters that will be replaced.
            replacement: New text that will replace the custom characters.

        Returns:
            The text without the given characters.
        """
        if not characters:
            return text

        characters = ''.join(sorted(characters))
        if characters in self._characters_regexes:
            characters_regex = self._characters_regexes[characters]
        else:
            characters_regex = re.compile("[%s]" % re.escape(characters))
            self._characters_regexes[characters] = characters_regex

        return characters_regex.sub(replacement, text)

    @staticmethod
    def replace_emails(text, replacement=''):
        """Remove emails address from text.

        Removes email addresses from input text or replaces them
        with a string if specified.

        Args:
            text: The text to be processed.
            replacement: New text that will replace email addresses.

        Returns:
            The text without email addresses.
        """
        return re.sub(regex.EMAIL_REGEX, replacement, text)

    @staticmethod
    def replace_emojis(text, replacement=''):
        """Remove emojis from text.

        Removes emojis from input text or replaces them with a
        string if specified.

        Args:
            text: The text to be processed.
            replacement: New text that will replace emojis.

        Returns:
            The text without emojis.
        """
        return regex.EMOJI_REGEX.sub(replacement, text)

    @staticmethod
    def replace_hyphens(text, replacement=' '):
        """Replace hyphens in text.

        Replaces hyphens from input text with a whitespace or a
        string if specified.

        Args:
            text: The text to be processed.
            replacement: New text that will replace the hyphens.

        Returns:
            The text without hyphens.
        """
        return text.replace('-', replacement)

    def replace_punctuation(self, text, excluded=None, replacement=''):
        """Replace punctuation symbols in text.

        Removes punctuation from input text or replaces them with a
        string if specified. Characters replaced will be those
        in string.punctuation.

        Args:
            text: The text to be processed.
            excluded: Set of characters to exclude.
            replacement: New text that will replace punctuation.

        Returns:
            The text without punctuation.
        """
        if excluded is None:
            excluded = set()
        elif not isinstance(excluded, set):
            excluded = set(excluded)
        punct = ''.join(self.__punctuation.difference(excluded))

        return self.replace_characters(
            text, characters=punct, replacement=replacement)

    @staticmethod
    def replace_symbols(
            text,
            form='NFKD',
            excluded=None,
            replacement=''):
        """Replace symbols in text.

        Removes symbols from input text or replaces them with a
        string if specified.

        Args:
            text: The text to be processed.
            form: Unicode form.
            excluded: Set of unicode characters to exclude.
            replacement: New text that will replace symbols.

        Returns:
            The text without symbols.
        """
        if excluded is None:
            excluded = set()

        categories = set(['Mn', 'Sc', 'Sk', 'Sm', 'So'])

        return ''.join(c if unicodedata.category(c) not in categories or c in excluded
                       else replacement for c in unicodedata.normalize(form, text))

    @staticmethod
    def replace_urls(text, replacement=''):
        """Replace URLs in text.

        Removes URLs from input text or replaces them with a
        string if specified.

        Args:
            text: The text to be processed.
            replacement: New text that will replace URLs.

        Returns:
            The text without URLs.
        """
        return re.sub(regex.URL_REGEX, replacement, text)
