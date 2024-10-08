from typing import cast, List, Dict, Set, Optional, Union, Tuple
from nagini_contracts.contracts import *

# @Pure
# def getVal(mx: Optional[int]) -> int:
#     Requires(mx is not None)
#     return mx  

# def longest(strings : List[List[int]]) -> Optional[int]:
#     Requires(Acc(list_pred(strings)))
#     Requires(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
#     Ensures(Acc(list_pred(strings)))
#     Ensures(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
#     Ensures(((Result()) is (None)) == ((len(strings)) == (0)))
#     Ensures(Implies(Result() is not None, getVal(Result()) >= 0 and getVal(Result()) < len(strings)))
#     Ensures(not ((Result()) is not (None)) or (Forall(int, lambda d_1_s_:
#         not ((d_1_s_) >= 0 and d_1_s_ < len(strings)) or ((len(strings[getVal(Result())])) >= (len(strings[d_1_s_]))))))
#     Ensures(not (Result() is not None) or (Exists(int, lambda d_1_s_:
#         ((d_1_s_) >= 0 and d_1_s_ < len(strings)) and ((len(strings[getVal(Result())])) == (len(strings[d_1_s_]))))))
#     Ensures(not ((Result()) is not (None)) or (Forall(int, lambda d_4_j_:
#         (not (((0) <= (d_4_j_)) and ((d_4_j_) < (Result()))) or ((len((strings)[d_4_j_])) < (len(strings[getVal(Result())])))))))
#     result : Optional[int] = None
#     if (len(strings)) != (0):
#         d_5_i_ = int(0) # type : int
#         d_5_i_ = 0
#         d_6_mx_ = int(0) # type : int
#         d_6_mx_ = -1
#         while (d_5_i_) < (len(strings)):
#             Invariant(Acc(list_pred(strings)))
#             Invariant(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
#             Invariant(((d_5_i_) >= (0)) and ((d_5_i_) <= (len(strings))))
#             Invariant(((d_6_mx_) == (-1)) == ((result) is (None)))
#             Invariant(not ((d_5_i_) == (0)) or ((d_6_mx_) == (-1)))
#             Invariant(Implies(result is not None, getVal(result) >= 0 and getVal(result) < d_5_i_))
#             Invariant(Implies(result is not None, len(strings[getVal(result)]) == d_6_mx_))
#             Invariant(not ((d_5_i_) > (0)) or (result is not None))
#             Invariant(not ((d_5_i_) > (0)) or ((d_6_mx_) == (len(strings[getVal(result)]))))
#             Invariant(not (result is not None) or (Forall(int, lambda d_1_s_:
#                 not ((d_1_s_) >= 0 and d_1_s_ < d_5_i_) or ((len(strings[getVal(result)])) >= (len(strings[d_1_s_]))))))
#             Invariant(not (result is not None) or (Exists(int, lambda d_1_s_:
#                 ((d_1_s_) >= 0 and d_1_s_ < d_5_i_) and ((len(strings[getVal(result)])) == (len(strings[d_1_s_]))))))
#             Invariant(not ((result) is not (None)) or (Forall(int, lambda d_4_j_:
#                     (not (((0) <= (d_4_j_)) and ((d_4_j_) < (result))) or ((len((strings)[d_4_j_])) < (len(strings[getVal(result)]))), [[((strings)[d_4_j_])]]))))
#             if result is None or (len((strings)[d_5_i_])) > (len(strings[getVal(result)])):
#                 d_6_mx_ = len((strings)[d_5_i_])
#                 result = d_5_i_
#                 Assert(Forall(int, lambda x: Implies(x >= 0 and x < result, len(strings[result]) > len(strings[x]))))
#             d_5_i_ = (d_5_i_) + (1)
#     return result

def longest(strings : List[List[int]]) -> Optional[List[int]]:
    Requires(Acc(list_pred(strings)))
    Requires(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
    Ensures(Acc(list_pred(strings)))
    Ensures(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
    Ensures(((Result()) == (None)) == ((len(strings)) == (0)))
    Ensures(Implies((Result()) != (None), Acc(list_pred((Result())))))
    # Ensures(not ((Result()) != (None)) or (Forall(int, lambda d_1_s_:
    #     not ((d_1_s_) >= 0 and d_1_s_ < len(strings)) or ((len((Result()))) >= (len(strings[d_1_s_]))))))
    # Ensures(not ((Result()) != (None)) or (Exists(List[int], lambda d_2_s_:
    #     ((d_2_s_) in (strings)) and ((len(d_2_s_)) == (len((Result())))))))
    # Ensures(not ((Result()) != (None)) or (Exists(int, lambda d_3_i_:
    #     ((((0) <= (d_3_i_)) and ((d_3_i_) < (len(strings)))) and (((strings)[d_3_i_]) == ((Result())))) and (Forall(int, lambda d_4_j_:
    #         not (((0) <= (d_4_j_)) and ((d_4_j_) < (d_3_i_))) or ((len((strings)[d_4_j_])) < (len((Result())))))))))
    result : Optional[List[int]] = list([int(0)] * 0)
    result = None
    if (len(strings)) != (0):
        d_5_i_ = int(0) # type : int
        d_5_i_ = 0
        d_6_mx_ = int(0) # type : int
        d_6_mx_ = -1
        while (d_5_i_) < (len(strings)):
            Invariant(Acc(list_pred(strings)))
            Invariant(Forall(strings, lambda d_0_s_: Acc(list_pred(d_0_s_))))
            Invariant(Implies(result is not None, Acc(list_pred(result))))
            Invariant(((d_5_i_) >= (0)) and ((d_5_i_) <= (len(strings))))
            Invariant(((d_6_mx_) == (-1)) == ((result) == (None)))
            Invariant(not ((d_5_i_) == (0)) or ((d_6_mx_) == (-1)))
            Invariant(not ((d_5_i_) > (0)) or (result is not None))
            Invariant(Acc(list_pred((result))))
            Invariant(Implies((d_5_i_) > (0), Acc(list_pred((result)))))
            Invariant(not ((d_5_i_) > (0)) or ((d_6_mx_) == (len((result)))))
            # Invariant(not ((d_5_i_) > (0)) or (Forall(int, lambda d_7_s_:
            #     not ((d_7_s_) >= 0 and d_7_s_ < d_5_i_) or ((d_6_mx_) >= (len(strings[d_7_s_]))))))
            # Invariant(not ((d_5_i_) > (0)) or (Exists(List[int], lambda d_8_s_:
            #     ((d_8_s_) in (strings)) and ((d_6_mx_) == (len(d_8_s_))))))
            # Invariant(not ((result) != (None)) or (Exists(int, lambda d_9_i_:
            #     ((((0) <= (d_9_i_)) and ((d_9_i_) < (len(strings)))) and (((strings)[d_9_i_]) == ((result)))) and (Forall(int, lambda d_10_j_:
            #         not (((0) <= (d_10_j_)) and ((d_10_j_) < (d_9_i_))) or ((len((strings)[d_10_j_])) < (len((result)))))))))
            if (len((strings)[d_5_i_])) > (d_6_mx_):
                d_6_mx_ = len((strings)[d_5_i_])
                result = list((strings)[d_5_i_])
                Assert(Acc(list_pred(result)))
            Assert(d_6_mx_ >= 0)
            Assert(result is not None)
            Assert(Acc(list_pred(result)))
            d_5_i_ = (d_5_i_) + (1)
    return result
