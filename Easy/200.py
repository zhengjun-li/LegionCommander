'''
Count the number of islands in a 2D grid

Iterate through each cell, if it is an island '1', run BFS and mark all connected landmass as None. Increase count by 1

Improvements:
Instead of doing try, catch, we can do some if statements with (i,j) at the beginning to speed up program overhead

'''
class Solution:
    def BFS(self, i, j, tileType, grid):
        #print(f'Running BFS on {i},{j}')
        if i < 0 or j < 0:
            return
        #explore from input node and set everything to null
        if grid[i][j] == tileType:
            grid[i][j] = None
        else:
            return
        try:
            #explore up
            self.BFS(i - 1, j, tileType, grid)
        except Exception as e:
            #print(e)
            pass
        
        try:
            #explore right
            self.BFS(i, j + 1, tileType, grid)
            
        except Exception as e:
            #print(e)
            pass
        
        try:
            #explore down
            self.BFS(i + 1, j, tileType, grid)
        except Exception as e:
            #print(e)
            pass
        
        try:
            #explore left
            self.BFS(i, j - 1, tileType, grid)
        except Exception as e:
            #print(e)
            pass
        
        return
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        print(f'{m} x {n}')
        
        for i in range(0, m):
            for j in range(0, n):
                #print(f'{i},{j} value is {grid[i][j]}')
                #print(type(grid[i][j]))
                if grid[i][j] == '1':
                    print('here')
                    self.BFS(i, j, '1', grid)
                    islands += 1
                elif grid[i][j] == '0':
                    continue
                    print('here2')
                    self.BFS(i, j, '0', grid)
                elif grid[i][j] == None:
                    pass
        return islands