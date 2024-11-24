class UserInputError(Exception):
    pass


def try_parse_int(string):
    try:
        return int(string)
    except:
        return None
