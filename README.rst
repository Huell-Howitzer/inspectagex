Inspectagex
===========

Inspectagex is a Python library for file inspection and text manipulation using regular expressions. It provides several functions that allow you to perform common tasks such as finding numbers, dates, strings, words, and patterns in files, as well as manipulating file content based on regular expression patterns.

Installation
------------

You can install Inspectagex using pip::

    pip install inspectagex

Usage
-----

Here are some examples of how to use Inspectagex:

Find Numbers in a File
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import find_numbers_in_file

    file_path = "/path/to/file.txt"
    numbers = find_numbers_in_file(file_path)
    print("Numbers found:", numbers)

Check for Full Date Match
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import is_date_full_match

    file_path = "/path/to/file.txt"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    if is_date_full_match(file_path, date_pattern):
        print("Full date match found!")
    else:
        print("No full date match.")

Find String in a File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import find_string_in_file

    file_path = "/path/to/file.txt"
    search_string = "example"
    if find_string_in_file(file_path, search_string):
        print(f"The search string '{search_string}' is found in the file.")
    else:
        print(f"The search string '{search_string}' is not found in the file.")

Find Words in a File
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import find_words_in_file

    file_path = "/path/to/file.txt"
    words = find_words_in_file(file_path)
    print("Words found:", words)

Find Match at Beginning
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import find_match_at_beginning

    file_path = "/path/to/file.txt"
    pattern = r"Hello"
    if find_match_at_beginning(file_path, pattern):
        print("Match found at the beginning of a line!")
    else:
        print("No match at the beginning of a line.")

Print Unique Characters in a File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import print_unique_characters

    file_path = "/path/to/file.txt"
    print_unique_characters(file_path)

Split Text by Pattern
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import split_text_by_pattern

    file_path = "/path/to/file.txt"
    pattern = r"\s+"
    parts = split_text_by_pattern(file_path, pattern)
    print("Text split by pattern:", parts)

Replace Pattern in a File
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from inspectagex import replace_pattern_in_file

    file_path = "/path/to/file.txt"
    pattern = r"apple"
    replacement = "banana"
    replace_pattern_in_file(file_path, pattern, replacement)

Contributing
------------

Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for details.

