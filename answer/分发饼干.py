def findContentChildren(g, s) -> int:
    g = sorted(g)
    s = sorted(s)
    len_g = len(g)
    len_s = len(s)
    res = 0
    i = 0
    j = 0
    while i < len_g:
        while j < len_s:
            if s[j] >= g[i]:
                j += 1
                res += 1
                break
            else:
                j += 1
                continue
        i += 1
    return res


g = [1, 2, 3]
s = [1, 3, 9]
findContentChildren(g, s)
