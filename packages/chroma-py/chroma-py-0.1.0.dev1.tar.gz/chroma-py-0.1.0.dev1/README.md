# Chroma

## Installation

```
pip install chroma-py
```

## Usage

```python
from chroma import Color, Scale

yellow = Color([255, 255, 0]) # yellow
navy = Color([0, 0, 128]) # navy

rgb_scale = Scale(yellow, navy)
print(rgb_scale(0.5))

lab_scale = Scale(yellow.to_lab(), navy.to_lab())
print(lab_scale(0.5))
```
