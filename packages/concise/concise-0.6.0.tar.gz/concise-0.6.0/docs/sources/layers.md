<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L207)</span>
### ConvDNA

```python
concise.layers.ConvDNA(filters, kernel_size, strides=1, padding='valid', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None, seq_length=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L261)</span>
### ConvRNA

```python
concise.layers.ConvRNA(filters, kernel_size, strides=1, padding='valid', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None, seq_length=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L270)</span>
### ConvRNAStructure

```python
concise.layers.ConvRNAStructure(filters, kernel_size, strides=1, padding='valid', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None, seq_length=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L266)</span>
### ConvAA

```python
concise.layers.ConvAA(filters, kernel_size, strides=1, padding='valid', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None, seq_length=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L274)</span>
### ConvCodon

```python
concise.layers.ConvCodon(filters, kernel_size, strides=1, padding='valid', dilation_rate=1, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None, seq_length=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L434)</span>
### ConvSplines

```python
concise.layers.ConvSplines(filters, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=<concise.regularizers.GAMRegularizer object at 0x7fed1bd4a400>, bias_regularizer=None, kernel_constraint=None, bias_constraint=None, activity_regularizer=None)
```

Convenience wrapper over `keras.layers.Conv1D` with 2 changes:
- additional argument seq_length specifying input_shape (as in ConvDNA)
- restriction in kernel_regularizer - needs to be of class GAMRegularizer
- hard-coded values:
   - kernel_size=1,
   - strides=1,
   - padding='valid',
   - dilation_rate=1,

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L295)</span>
### GAMSmooth

```python
concise.layers.GAMSmooth(n_bases=10, spline_order=3, share_splines=False, spline_exp=False, l2_smooth=1e-05, l2=1e-05, use_bias=False, bias_initializer='zeros')
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/layers.py#L100)</span>
### GlobalSumPooling1D

```python
keras.layers.pooling.GlobalSumPooling1D()
```

Global average pooling operation for temporal data.
__Input shape__

3D tensor with shape: `(batch_size, steps, features)`.
__Output shape__

2D tensor with shape:
`(batch_size, channels)`

----

### InputDNA


```python
InputDNA(seq_length, name=None)
```


Input placeholder for array returned by `encodeDNA` or `encodeRNA`

Wrapper for: `keras.layers.Input((seq_length, 4), name=name, **kwargs)`

----

### InputDNA


```python
InputDNA(seq_length, name=None)
```


Input placeholder for array returned by `encodeDNA` or `encodeRNA`

Wrapper for: `keras.layers.Input((seq_length, 4), name=name, **kwargs)`

----

### InputRNAStructure


```python
InputRNAStructure(seq_length, name=None)
```


Input placeholder for array returned by `encodeRNAStructure`

Wrapper for: `keras.layers.Input((seq_length, 5), name=name, **kwargs)`

----

### InputCodon


```python
InputCodon(seq_length, ignore_stop_codons=True, name=None)
```


Input placeholder for array returned by `encodeCodon`

- __Note__: The seq_length is divided by 3

Wrapper for: `keras.layers.Input((seq_length / 3, 61 or 61), name=name, **kwargs)`

----

### InputAA


```python
InputAA(seq_length, name=None)
```


Input placeholder for array returned by `encodeAA`

Wrapper for: `keras.layers.Input((seq_length, 22), name=name, **kwargs)`

----

### InputSplines


```python
InputSplines(seq_length, n_bases=10, name=None)
```


Input placeholder for array returned by `encodeSplines`

Wrapper for: `keras.layers.Input((seq_length, n_bases), name=name, **kwargs)`
