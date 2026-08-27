# Fill-Level Detection

A small computer vision project: estimating how full a glass is from a photograph.

Converts source images to grayscale, then works through thresholding and edge behavior
to find the liquid line. `demo.ipynb` walks through the pipeline step by step against
the sample images in the repo; `convert_2_grayscale.py` and `main.py` are the
standalone versions.

Built to get hands-on with OpenCV's preprocessing primitives before moving to
CNN-based approaches.

## Running it

```bash
pip install opencv-python numpy matplotlib
jupyter lab demo.ipynb
```

