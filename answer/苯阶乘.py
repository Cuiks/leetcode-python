# 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

#
# def clumsy(N: int) -> int:
#     res = 0
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     if N == 3:
#         return 6
#     if N > 3:
#         res += N * (N - 1) // (N - 2) + (N - 3)
#         N -= 4
#     while N:
#         if N == 1:
#             res += -1 * N
#             N -= 1
#         elif N == 2:
#             res += -1 * (N * (N - 1))
#             N -= 2
#         elif N == 3:
#             res += -1 * (N * (N - 1) // (N - 2))
#             N -= 3
#         elif N:
#             res += -1 * (N * (N - 1) // (N - 2)) + (N - 3)
#             N -= 4
#     return res
#
#
# print(clumsy(5))


def clumsy(N: int) -> int:
    _list = [N]
    N -= 1
    index = 0
    while N:
        if index % 4 == 0:
            _list.append(_list.pop() * N)
        elif index % 4 == 1:
            _list.append(int(_list.pop() / N))
        elif index % 4 == 2:
            _list.append(N)
        elif index % 4 == 3:
            _list.append(-N)
        index += 1
        N -= 1

    return sum(_list)

print(clumsy(5))