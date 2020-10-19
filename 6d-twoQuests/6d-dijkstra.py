from heapq import heappush, heappop
import math


def solution(a, b):
    def skip_intermediates(q):
        result = [q[0]]
        for i in range(1, len(q)-1):
            if not (result[-1] <= q[i] <= q[i + 1] or result[-1] >= q[i] >= q[i + 1]):
                result.append(q[i])

        result.append(q[-1])
        return result

    # Life is easier if the quests have addition nodes at zero, to simplify indexing
    a, b = [[0] + skip_intermediates(x) for x in (a, b)]

    # The quest lengths get used a lot as bounds checks, so better to avoid that function call
    len_a = len(a)
    len_b = len(b)

    # visited[0][i] = j means we have visited (0,i,j)
    # visited[1][j] = i means we have visited (1,i,j)
    visited = [[-1 for i in range(len(q))] for q in (a,b)]

    tentative_heap = []
    tentative_dict = {}

    def Neighbours(s, i, j):
        if s == 0:
            pos = a[i]
        else:
            pos = b[j]

        a_idx = i + 1
        b_idx = j + 1
        a_val = a[a_idx] if a_idx < len_a else None
        b_val = b[b_idx] if b_idx < len_b else None
        neighbour_a = neighbour_b = None
        if a_val is not None and (b_val is None or not (pos <= b_val < a_val or a_val < b_val <= pos)):
            neighbour_a = (abs(pos - a_val), (0, a_idx, j))

        if b_val is not None and (a_val is None or not (pos <= a_val < b_val or b_val < a_val <= pos)):
            neighbour_b = (abs(pos - b_val), (1, i, b_idx))

        if neighbour_a is None:
            if neighbour_b is None:
                return ()
            else:
                return (neighbour_b,)
        else:
            if neighbour_b is None:
                return (neighbour_a,)
            else:
                return (neighbour_a, neighbour_b,)

    def Visit(s, i, j, d):
        if s == 0:
            idx_0 = i
            idx_1 = j
        else:
            idx_0 = j
            idx_1 = i

        if visited[s][idx_0] >= idx_1:
            return
        else:
            visited[s][idx_0] = idx_1

            for nd, neighbour in Neighbours(s, i, j):
                new_entry = [d + nd, neighbour, True]
                add_entry = True
                if neighbour in tentative_dict:
                    if tentative_dict[neighbour][0] > new_entry[0]:
                        tentative_dict[neighbour][-1] = False
                    else:
                        add_entry = False

                if add_entry:
                    tentative_dict[neighbour] = new_entry
                    heappush(tentative_heap, new_entry)

    #Get the ball rolling...
    Visit(0,0,0,0)

    while len(tentative_heap) > 0:
        d, point, valid = heappop(tentative_heap)
        if point in tentative_dict:
            del tentative_dict[point]

        if valid:
            s, i, j = point
            if i == len_a - 1 and j == len_b - 1:
                return d
            Visit(s, i, j, d)

a = [5,3,10,6]
b = [9,7,12]
print(solution(a,b))