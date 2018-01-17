from microbit import *

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    
def amap(x, in_min, in_max, out_min, out_max):
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
def constrain(x, lo, hi):
    return max(min(x, hi), lo)

blur_dist = 1/2**0.5

def draw_circle(x, y, r):
   circle_sharpness = r
   r = r - 1
   for px in range(5):
       for py in range(5):
           d = dist(px, py, x, y)
           value = -(9*circle_sharpness*(d-blur_dist-r))/(1+(circle_sharpness*abs(d-blur_dist-r)) ** 2) ** 0.5
           display.set_pixel(px, py, constrain(int(value + 0.5), 0, 9))
    
def draw_rect(x, y, w, h):
    display.clear()
    for px in range(x, x+w):
        for py in range(y, y+h):
            display.set_pixel(px, py, 9)
  
def draw_line(sx, sy, ex, ey, b=9):
    if sx == ex:
        for y in range(sy, ey + [-1, 1][ey > sy], [-1, 1][sy < ey]):
            display.set_pixel(sx, y, b)
        return
    if sx > ex:
        sx, sy, ex, ey = ex, ey, sx, sy
    m = (sy - ey) / (sx - ex)
    c = sy - m * sx
    l = int(dist(sx, sy, ex, ey)) + 1
    for gap in range(l + 1):
        x = int(amap(gap, 0, l, sx, ex) + 0.5)
        y = int(m * x + c + 0.5)
        display.set_pixel(x, y, 9)
        
def draw_polygon(*points):
    for p1, p2 in zip(points, list(points[1:])+[points[0]]):
        draw_line(p1[0], p1[1], p2[0], p2[1])
    sx = int(sum(p[0] for p in points) / len(points) + 0.5)
    sy = int(sum(p[1] for p in points) / len(points) + 0.5)
    queue = [(sx, sy)]
    while queue:
        px, py = queue.pop()
        if display.get_pixel(px, py) == 9:
            continue
        display.set_pixel(px, py, 9)
        for mx, my in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= px + mx < 5 and 0 <= py + my < 5:
                queue.append((px + mx, py + my))
