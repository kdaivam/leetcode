
# FloodFill Algorithm

img = [
[1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 2, 0],
[1, 0, 0, 1, 0, 2, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 0, 1, 0],
[1, 1, 1, 2, 2, 2, 2, 0],
[1, 1, 1, 1, 1, 2, 1, 1],
[2, 2, 1, 1, 1, 2, 2, 1],
]

nr = len(img)
nc = len(img[0])
visited = []

def find_neighbors(r,c):
    return [[r+1, c], [r, c+1], [r-1, c], [r, c-1],
            [r+1, c+1], [r+1, c-1], [r-1, c-1], [r-1, c+1]]

def flood_fill(r, c, oc, new_color):
    if r < 0 or r >= nr:
        return
    if c < 0 or c >= nc:
        return
    
    if img[r][c] != oc:
        return
    
    img[r][c] = new_color
    
    visited.append([r,c])
    neighbors = find_neighbors(r,c)
    
    for cp in neighbors:
        if cp not in visited:
            flood_fill(cp[0],cp[1],oc, new_color)



def flood_img():
    print("Input image ")
    for i in img:   print(i)
    replace_point = (4,4)
    old_color = 2
    new_color = 3
    flood_fill(*replace_point, old_color, new_color)
    print("Output Image")
    for i in img:   print(i)
    

flood_img()