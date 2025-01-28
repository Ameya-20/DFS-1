# TC , SC - O(rows*cols), O(N) -> q + dist_mat + directions
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist_mat = [[-1 for _ in range(cols)] for _ in range(rows)]  # Initialize distances
        queue = []
        
        # Step 1: Add all 0s to the q and set their distance to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist_mat[r][c] = 0
                    queue.append((r, c))  # Add all 0 cells as sources
        
        # Step 2: Perform BFS to calculate distances
        while queue:
            curr_r, curr_c = queue.pop(0)
            
            for mv_r, mv_c in directions:
                nr, nc = curr_r + mv_r, curr_c + mv_c
                # If the neighbor is valid and hasn't been visited
                if 0 <= nr < rows and 0 <= nc < cols and dist_mat[nr][nc] == -1:
                    dist_mat[nr][nc] = dist_mat[curr_r][curr_c] + 1  # Update distance
                    queue.append((nr, nc))
        
        return dist_mat
