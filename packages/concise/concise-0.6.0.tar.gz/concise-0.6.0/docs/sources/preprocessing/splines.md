### encodeSplines


```python
encodeSplines(x, n_bases=10, spline_order=3, start=None, end=None)
```


Get B-spline base-function expansion

__Details__

First, the knots for B-spline basis functions are placed
equidistantly on the [start, end] range.
(inferred from the data if None). Next, b_n(x) value is
is computed for each x and each n (spline-index) with
`scipy.interpolate.splev`.

__Arguments__

- __x__: a numpy array of positions with 2 dimensions
n_splines int: Number of splines used for the positional bias.
- __spline_order__: 2 for quadratic, 3 for qubic splines
start, end: range of values. If None, they are inferred from the data
as minimum and maximum value.

__Returns__

`np.ndarray` of shape `(x.shape[0], x.shape[1], n_bases)`
