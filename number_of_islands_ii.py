class Solution:
    def numIslands2(self, m, n, positions):
        parent = list(range(m * n))
        rank = [0] * (m * n)
        land = set()
        count = 0
        result = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            if rank[ra] < rank[rb]:
                ra, rb = rb, ra

            parent[rb] = ra

            if rank[ra] == rank[rb]:
                rank[ra] += 1

            return True

        for r, c in positions:
            cell = r * n + c

            if cell in land:
                result.append(count)
                continue

            land.add(cell)
            count += 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    neighbor = nr * n + nc

                    if neighbor in land and union(cell, neighbor):
                        count -= 1

            result.append(count)

        return result
