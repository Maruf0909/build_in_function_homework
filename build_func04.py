def main(n):
    """A integer type variable 'n' is given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_fun
    Args:
        n (int): integer
        
    Returns:
        float: the value of the expression
    """
    value = pow((2+n)/3,2)
    return value

print(main(4))