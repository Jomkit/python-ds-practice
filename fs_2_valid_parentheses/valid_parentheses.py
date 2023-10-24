def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens[0] == ')' or parens[-1] == '(':
        return False
    
    open_parens = 0
    close_parens = 0

    for p in parens:
        if p == '(':
            open_parens += 1
        elif p == ')':
            close_parens += 1
    if open_parens == close_parens:
        return True
    
    return False