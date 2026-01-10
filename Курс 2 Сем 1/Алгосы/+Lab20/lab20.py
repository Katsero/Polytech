def held_karp_tsp(dist):

    n = len(dist)
    if n == 0:
        return 0, []
    if n == 1:
        return 0, [0]

    for i in range(n):
        if dist[i][i] != 0:
            raise ValueError(f"dist[{i}][{i}] must be 0")

    total_masks = 1 << n
    dp = [[None] * n for _ in range(total_masks)]
    parent = [[-1] * n for _ in range(total_masks)]

    dp[1][0] = 0

    for mask in range(1, total_masks):
        for u in range(n):
            if dp[mask][u] is None:
                continue
            if not (mask & (1 << u)):
                continue  

            for v in range(n):
                if mask & (1 << v):
                    continue 

                if dist[u][v] is None:
                    continue

                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]

                if dp[new_mask][v] is None or new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    parent[new_mask][v] = u

    full_mask = total_masks - 1
    best_cost = None
    best_last = -1

    for v in range(1, n):
        if dp[full_mask][v] is None:
            continue
        if dist[v][0] is None:
            continue
        total = dp[full_mask][v] + dist[v][0]
        if best_cost is None or total < best_cost:
            best_cost = total
            best_last = v

    if best_cost is None:
        return None, [] 

    path = []
    cur = best_last
    mask = full_mask

    while cur != -1:
        path.append(cur)
        prev = parent[mask][cur]
        mask ^= (1 << cur)
        cur = prev

    path.reverse()
    path.append(0)

    return best_cost, path


dist_matrix = [
    [0,   10,  15,  None,20,  None],
    [10,  0,   35,  25,  None,30 ],
    [15,  35,  0,   30,  10,  None], 
    [None,25,  30,  0,   15,  20 ],
    [20,  None,10,  15,  0,   25 ],  
    [None,30,  None,20,  25,  0  ]  
]

min_cost, tour = held_karp_tsp(dist_matrix)

if min_cost is None:
    print("Гамильтонов цикл не существует.")
else:
    print("Минимальная стоимость:", min_cost)
    print("Маршрут:", tour)