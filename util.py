def strip_spaces_and_hyphens(input_string):
    """
    This utility function removes spaces and hyphens from the given string.

    Parameters:
    input_string (str): The string to process.

    Returns:
    str: The processed string with spaces and hyphens removed.
    """
    return input_string.replace(" ", "").replace("-", "")
