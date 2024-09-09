from nagini_contracts.contracts import *

def right__angle__triangle(a : int, b : int, c : int) -> bool:
    # pre-conditions-start
    Ensures((Result()) == ((((((a) * (a)) + ((b) * (b))) == ((c) * (c))) or ((((a) * (a)) + ((c) * (c))) == ((b) * (b)))) or ((((b) * (b)) + ((c) * (c))) == ((a) * (a)))))
    # pre-conditions-end

    # impl-start
    result = False # type : bool
    result = (((((a) * (a)) + ((b) * (b))) == ((c) * (c))) or ((((a) * (a)) + ((c) * (c))) == ((b) * (b)))) or ((((b) * (b)) + ((c) * (c))) == ((a) * (a)))
    return result
    # impl-end
