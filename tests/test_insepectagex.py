import re
import tempfile
import os
import pytest
from inspectagex.regex_utils import (
    find_numbers_in_file,
    is_date_full_match,
    find_string_in_file,
    find_words_in_file,
    find_match_at_beginning,
    print_unique_characters,
    split_text_by_pattern,
    replace_pattern_in_file,
)


class TestInspectagex:
    """
    A class containing tests for inspectagex functions.
    """

    @classmethod
    def setup_class(cls):
        """
        Set up the test class by creating a temporary test file and writing content.

        This method is run once before all the test methods.
        """
        cls.file_content = "This is a test file.\n123 is a number.\nDate: 2023-06-09"
        cls.file_path = tempfile.mkstemp()[1]
        with open(cls.file_path, "w") as file:
            file.write(cls.file_content)

    @classmethod
    def teardown_class(cls):
        """
        Tear down the test class by removing the temporary test file.

        This method is run once after all the test methods.
        """
        os.remove(cls.file_path)

    def test_find_numbers_in_file(self):
        """
        Test the find_numbers_in_file function.

        This method tests the find_numbers_in_file function by asserting that the returned list of numbers matches the
        expected numbers in the test file.
        """
        expected_numbers = ["123"]
        numbers = find_numbers_in_file(self.file_path)
        assert numbers == expected_numbers

    def test_is_date_full_match(self):
        """
        Test the is_date_full_match function.

        This method tests the is_date_full_match function by asserting that it correctly detects a full date match in
        the test file.
        """
        date_pattern = r"\d{4}-\d{2}-\d{2}"
        assert is_date_full_match(self.file_path, date_pattern)

    def test_find_string_in_file(self):
        """
        Test the find_string_in_file function.

        This method tests the find_string_in_file function by asserting that it correctly detects the presence or absence
        of a given search string in the test file.
        """
        assert find_string_in_file(self.file_path, "test file")
        assert not find_string_in_file(self.file_path, "example")

    def test_find_words_in_file(self):
        """
        Test the find_words_in_file function.

        This method tests the find_words_in_file function by asserting that the returned list of words matches the
        expected words in the test file.
        """
        expected_words = ["This", "is", "a", "test", "file",
                          "123", "is", "a", "number", "Date", "2023", "06", "09"]
        words = find_words_in_file(self.file_path)
        assert words == expected_words

    def test_find_match_at_beginning(self):
        """
        Test the find_match_at_beginning function.

        This method tests the find_match_at_beginning function by asserting that it correctly detects a pattern match at
        the beginning of a line in the test file.
        """
        pattern = r"This"
        assert find_match_at_beginning(self.file_path, pattern)
        assert not find_match_at_beginning(self.file_path, "is")

    def test_replace_pattern_in_file(self):
        """
        Test the replace_pattern_in_file function.

        This method tests the replace_pattern_in_file function by replacing a pattern with a replacement string in the
        test file and asserting that the content of the file is as expected.
        """
        pattern = r"\d{4}-\d{2}-\d{2}"
        replacement = "YYYY-MM-DD"
        expected_content = "This is a test file.\n123 is a number.\nDate: YYYY-MM-DD"
        replace_pattern_in_file(self.file_path, pattern, replacement)
        with open(self.file_path, "r") as file:
            new_content = file.read()
        assert new_content.strip() == expected_content

