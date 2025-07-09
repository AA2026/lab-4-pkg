from geometry import Square, Circle, area_stats

s = Square(156)
c = Circle(463)

print(s.area())
print(c.area())

shapes = [s, c]

print(area_stats(shapes))