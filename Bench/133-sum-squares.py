from typing import cast, List, Dict, Set, Optional, Union
from nagini_contracts.contracts import *

@Pure
def psum(i : int, j : int, s : List[int]) -> int :
    # pre-conditions-start
    Requires(Acc(list_pred(s)))
    Requires(0 <= i and i <= j and j <= len(s))
    # pre-conditions-end

    # impl-start
    if i == j:
        return 0
    else:
        return (s)[j - 1] * (s)[j - 1] + (psum(i, j - 1, s))
    # impl-end

def sum__squares(lst : List[int]) -> int:
    # pre-conditions-start
    Requires(Acc(list_pred(lst)))
    # pre-conditions-end
    # post-conditions-start
    Ensures(Acc(list_pred(lst)))
    Ensures((Result()) == (psum(0, len(lst), lst)))
    # post-conditions-end

    # impl-start
    r = int(0) # type : int
    r = 0
    d_2_k_ = int(0) # type : int
    d_2_k_ = 0
    while (d_2_k_) < (len(lst)):
        # invariants-start
        Invariant(Acc(list_pred(lst)))
        Invariant(((0) <= (d_2_k_)) and ((d_2_k_) <= (len(lst))))
        Invariant((r) == (psum(0, d_2_k_, lst)))
        Invariant(Forall(int, lambda d_2_i_: (not (((0) <= (d_2_i_)) and ((d_2_i_) < (len(lst)))) or ((psum(0, d_2_i_ + 1, lst)) == (psum(0, d_2_i_, lst) + lst[d_2_i_] * lst[d_2_i_])), [[psum(0, d_2_i_ + 1, lst)]])))
        # invariants-end
        r = (r) + ((lst)[d_2_k_]) * ((lst)[d_2_k_])
        d_2_k_ = (d_2_k_) + (1)
    return r
    # impl-end
