from typing import cast, List, Dict, Set, Optional, Union
from nagini_contracts.contracts import *

def is__equal__to__sum__even(n : int) -> bool:
    # pre-conditions-start
    Ensures((Result()) == ((((n % 2)) == (0)) and ((n) >= (8))))
    # pre-conditions-end

    # impl-start
    b = False # type : bool
    b = (((n % 2)) == (0)) and ((n) >= (8))
    return b
    # impl-end
