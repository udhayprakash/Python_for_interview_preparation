#!/usr/bin/python
"""
Purpose: 
"""
from pprint import pprint


class Solution(object):
    def numOffices(self, grid):
        result = 0
        for x in range(len(grid[0])):
            if grid[0][x] == '1' and grid[0][x - 1] != '1':
                result += 1

        for y in range(1, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == '1' and grid[y][x - 1] != '1' \
                        and grid[y - 1][x] != '1':
                    result += 1
        return result

    def numOffices(self, grid):
        result = 0
        def markIsland(grid, x, y, visited)
            
            if (x < 0 | | x > grid.length - 1 | | y < 0 | | y > grid[x].length - 1)
            
            return
            
            if (visited[x][y] == true) 
            return

            
            visited[x][y] = true
            if (grid[x][y] == '0') 
            return

        
        markIsland(grid, x - 1, y, visited)
        markIsland(grid, x + 1, y, visited)
        markIsland(grid, x, y - 1, visited)
        markIsland(grid, x, y + 1, visited)
        

        visited = []
        for (let i = 0 i < grid.length i++)
        
            visited[i] = []
        
        for (let x = 0 x < grid.length x++) 
        for (let y = 0 y < grid[x].length y++) 
        if (!visited[x][y] & & grid[x][y] == = '1') 
        result++
        markIsland(grid, x, y, visited)
        
        visited[x][y] = true
        
        
        return result

if __name__ == "__main__":
    sol = Solution()
    matrix = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]
    pprint(matrix)
    assert sol.numOffices(matrix) == 3
    print()
    matrix = [['1', '1', '1', '1', '1'],
              ['1', '1', '0', '0', '1'],
              ['1', '0', '0', '0', '0'],
              ['1', '1', '1', '0', '1']]
    pprint(matrix)
    assert sol.numOffices(matrix) == 2
