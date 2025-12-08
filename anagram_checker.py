def is_anagram(first, second):
    """Function to test if two strings are anagrams."""
    # remove whitespaces
    first = first.replace(" ", "")
    second = second.replace(" ", "")
    # change strings to lowercase
    first = first.lower()
    second = second.lower()

    if len(first) != len(second):
        return False
    for char in first:
        if char not in second:
            return False
    for char in second:
        if char not in first:
            return False
    return True
