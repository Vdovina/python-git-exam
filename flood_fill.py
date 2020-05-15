image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2

def floodFill(sr, sc):
    currentColor = image[sr][sc]
    if currentColor == newColor:
        return image
    fill(sr, sc, currentColor)

def fill(r, c, cur):
    if image[r][c] == cur:
        image[r][c] = newColor
        if r < len(image):
            fill(r+1, c, cur)
        if c < len(image[0]):
            fill(r, c+1, cur):
        if r >= 1:
            fill(r-1, c, cur)
        if c >= 1:
            fill(r, c-1, cur)

floodFill(sr, sc)
print(image)