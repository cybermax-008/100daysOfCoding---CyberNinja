class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        num_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.find_island(grid,i,j)
                    num_islands+=1
                    
        return num_islands
    
    def find_island(self,grid,i,j):
        if i<0 or i>=len(grid):
            return
        if j<0 or j>=len(grid[0]):
            return
        if grid[i][j] !='1':
            return
        
        grid[i][j]='0'
        self.find_island(grid,i-1,j)
        self.find_island(grid,i+1,j)
        self.find_island(grid,i,j+1)
        self.find_island(grid,i,j-1)