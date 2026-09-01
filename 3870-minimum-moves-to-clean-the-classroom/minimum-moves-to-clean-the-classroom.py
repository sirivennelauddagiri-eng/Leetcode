from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an ID to every litter
        litter_id = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_id[(i, j)] = count
                    count += 1

        # All litter collected
        all_mask = (1 << count) - 1

        # BFS state:
        # (row, col, remaining_energy, mask)
        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            # All litter collected
            if mask == all_mask:
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Wall
                if classroom[nr][nc] == 'X':
                    continue

                # Cannot move without energy
                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                # Recharge
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Collect litter
                if classroom[nr][nc] == 'L':
                    new_mask |= 1 << litter_id[(nr, nc)]

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append((
                        nr,
                        nc,
                        new_energy,
                        new_mask,
                        moves + 1
                    ))

        return -1