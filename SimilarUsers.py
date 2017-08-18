__author__ = 'anishdalal'
import heapq

def get_difference(vec1, vec2):
    # manhattan distance
    z = zip(vec1, vec2)
    return sum([abs(x - y) for x, y in z])

def get_top_k_similar_users(user_vec, all_users, k):
    heap = []
    for vec in all_users:
        sim = get_difference(user_vec, vec)
        if len(heap) < k:
            heapq.heappush(heap, (sim, vec))
        elif len(heap) == k:
            if sim < heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (sim, vec))
            elif sim < heap[-1]:
                del heap[-1]
                heapq.heapify(heap)
                heapq.heappush(heap, (sim, vec))
    ret = []
    while heap:
        ret.append(heapq.heappop(heap)[1])
    return ret