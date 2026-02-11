


def side_effects() -> None:
    raise NotImplementedError('dangerous side-effects')

def err_returning_func() -> tuple[bool, Exception|None]:
    '''This function swallows all errors, and returns them in a result tuple
    instead of raising an exception
    '''
    try:
        side_effects()
    except Exception as err:
        return False, err

    return True, None


def my_func() -> tuple[bool, Exception|None]:
    ok, err = err_returning_func()
    return ok, None if ok else False, err
