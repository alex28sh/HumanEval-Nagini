from typing import cast, List, Dict, Set, Optional, Union, Tuple
from nagini_contracts.contracts import *

def solve(n : int) -> int:
    # pre-conditions-start
    Requires((n) >= (0))
    # pre-conditions-end
    # post-conditions-start
    Ensures(Result() >= 0)
    Ensures((Result()) == (popcount(n)))
    # post-conditions-end

    # impl-start
    r = int(0) # type : int
    d_0_m_ = int(0) # type : int
    d_0_m_ = n
    r = 0
    while (d_0_m_) > (0):
        # invariants-start
        Invariant(((0) <= (d_0_m_)) and ((d_0_m_) <= (n)))
        Invariant(r >= 0)
        Invariant(((r) + (popcount(d_0_m_))) == (popcount(n)))
        # invariants-end
        r = (r) + ((d_0_m_ % 2))
        d_0_m_ = (d_0_m_ // 2)
    return r
    # impl-end

@Pure
def popcount(n : int) -> int :
    # pre-conditions-start
    Requires(n >= 0)
    # pre-conditions-end

    # impl-start
    if n == 0:
        return 0
    else:
        return (n % 2) + popcount(n // 2)
    # impl-end

