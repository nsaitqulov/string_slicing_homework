def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    w=s[n:]
    return w
print(main("apple", 1))