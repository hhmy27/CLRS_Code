import pandas as pd
import numpy as np

# import pandas
# import numpy

def MATRIX_CHAIN_ORDER(p):
    inf = 0xffff
    # i start at 1,end at n, so let n = p.length, not p.length-1
    n = len(p)
    m = [[0 for i in range(n)] for i in range(n)]
    s = [[0 for i in range(n)] for i in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = inf
            for k in range(i, j):
                print(i, j, k)
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
                    # print(i, j)
                    # print(pd.DataFrame(m))
                    # print("=" * 10)
    return m, s


def PRINT_OPTIMAL_PARENS(s, i, j):
    pass


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = MATRIX_CHAIN_ORDER(p)
    pm = pd.DataFrame(m)
    ps = pd.DataFrame(s)

    print(pm)
    print(ps)
