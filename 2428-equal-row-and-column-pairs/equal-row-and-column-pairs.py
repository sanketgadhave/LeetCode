class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = [list(row) for row in zip(*grid)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(transposed_grid)):
                if grid[i] == transposed_grid[j]:
                    count += 1
        
        return count
            
