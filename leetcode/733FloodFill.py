from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    X, Y = len(image), len(image[0])
    col = image[sr][sc]
    visited = {(sr, sc)}
    if col == color:
        return image
    stack = [(sr, sc)]
    image[sr][sc] = color
    while stack:
        r, c = stack.pop()
        l = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
        for i, j in l:
            if i >= 0 and i < X and j >= 0 and j < Y and (i, j) not in visited and image[i][j] == col:
                stack.append((i, j))
                visited.add((i, j))
                image[i][j] = color
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
         