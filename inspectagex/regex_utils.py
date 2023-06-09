import re


def find_numbers_in_file(file_path):
    """
    Find all numbers in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        list: List of numbers found in the file.
    """
    numbers = []

    with open(file_path, "r") as file:
        for line in file:
            matches = re.findall(r"\d+", line)
            numbers.extend(matches)

    return numbers


def is_date_full_match(file_path, date_pattern):
    """
    Check if any line in the file matches the full date pattern.

    Args:
        file_path (str): Path to the file.
        date_pattern (str): Regular expression pattern for the full date.

    Returns:
        bool: True if a full date match is found, False otherwise.
    """
    with open(file_path, "r") as file:
        for line in file:
            match = re.fullmatch(date_pattern, line.strip())
            if match:
                return True

    return False


def find_string_in_file(file_path, search_string):
    """
    Check if the search string is found in the file.

    Args:
        file_path (str): Path to the file.
        search_string (str): String to search for.

    Returns:
        bool: True if the search string is found, False otherwise.
    """
    with open(file_path, "r") as file:
        for line in file:
            if search_string in line:
                return True

    return False


def find_words_in_file(file_path):
    """
    Find all words in a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        list: List of words found in the file.
    """
    words = []

    with open(file_path, "r") as file:
        for line in file:
            matches = re.finditer(r"\w+", line)
            words.extend(match.group() for match in matches)

    return words


def find_match_at_beginning(file_path, pattern):
    """
    Check if any line in the file matches the pattern at the beginning.

    Args:
        file_path (str): Path to the file.
        pattern (str): Regular expression pattern to match.

    Returns:
        bool: True if a match is found at the beginning of a line, False otherwise.
    """
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                return True

    return False


def print_unique_characters(file_path):
    """
    Print all unique characters in the file.

    Args:
        file_path (str): Path to the file.
    """
    unique_chars = set()

    with open(file_path, "r") as file:
        for line in file:
            unique_chars.update(line.strip())

    print("Unique characters in the file:")
    for char in sorted(unique_chars):
        print(char)


def split_text_by_pattern(file_path, pattern):
    """
    Split the text in the file by a pattern.

    Args:
        file_path (str): Path to the file.
        pattern (str): Regular expression pattern to split the text.

    Returns:
        list: List of parts after splitting the text by the pattern.
    """
    split_text = []

    with open(file_path, "r") as file:
        for line in file:
            parts = re.split(pattern, line)
            split_text.extend(parts)

    return split_text


def replace_pattern_in_file(file_path, pattern, replacement):
    """
    Replace a pattern with a replacement string in the file.

    Args:
        file_path (str): Path to the file.
        pattern (str): Regular expression pattern to replace.
        replacement (str): String to replace the pattern with.
    """
    new_content = []

    with open(file_path, "r") as file:
        for line in file:
            new_line = re.sub(pattern, replacement, line)
            new_content.append(new_line)

    with open(file_path, "w") as file:
        file.writelines(new_content)

