def area_stats(shapes):
    if len(shapes) == 0:
        raise ValueError("At least one Shape is required")
    
    areas = [shape.area() for shape in shapes]
    areas.sort()

    return {
        "n": len(areas),
        "total": sum(areas),
        "mean": sum(areas)/len(areas),
        "min": areas[0],
        "max": areas[len(areas) - 1],
    }