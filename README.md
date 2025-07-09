# BU RISE Data Science Practicum Lab 4 - Geometry Demo

This is a Python lab exploring various geometrical components including different shapes (squares and circles) and their areas. The program also computes the stats for areas of squares and circles, including mean, min, and max. This is done to verify the accuracy and variability in the different area calculations being conducted. The program can be added on to in order to calculate the areas of other shapes, such as rectangles, triangles, trapezoids, etc.

## Installation

1. Clone the repository
```bash
git clone https://github.com/AA2026/lab-4-pkg.git
cd lab-4-pkg/geometry-demo
```

2. Set up the Python environment (using conda):
```bash
conda create -n lab_4 --file environment.txt -y
conda activate lab_4
```

3. Install the package in editable mode:
 ```bash
 pip install -e .
 ```

## Installation
You can run and edit your own copy of the demo.py script to see the package in action:
```bash
 python demo.py
 ```
Sample import for your own code:
```python
from geometry import Square, Circle, area_stats

s = Square(4)
c = Circle(2)

print(s.area())           # 16.0
print(c.area())           # ~12.57
print(area_stats(s, c))   # Summary dictionary (prints number of shapes, total area, mean area, min area, max area)

```


## Contributing

Currently this repository is not open to contributions since it is part of a lab for a university program (Boston University RISE).

