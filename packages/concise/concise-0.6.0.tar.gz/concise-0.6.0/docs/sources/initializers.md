<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/initializers.py#L55)</span>
### PSSMBiasInitializer

```python
concise.initializers.PSSMBiasInitializer(pwm_list=[], kernel_size=None, mean_max_scale=0.0, background_probs={'A': 0.25, 'T': 0.25, 'C': 0.25, 'G': 0.25})
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/initializers.py#L112)</span>
### PSSMKernelInitializer

```python
concise.initializers.PSSMKernelInitializer(pwm_list=[], stddev=0.05, seed=None, background_probs={'A': 0.25, 'T': 0.25, 'C': 0.25, 'G': 0.25}, add_noise_before_Pwm2Pssm=True)
```

truncated normal distribution shifted by a PSSM

__Arguments__

- __pwm_list__: a list of PWM's or motifs
- __stddev__: a python scalar or a scalar tensor. Standard deviation of the
  random values to generate.
- __seed__: A Python integer. Used to seed the random generator.
- __background_probs__: A dictionary of background probabilities.
	  - __Default__: `{'A': .25, 'C': .25, 'G': .25, 'T': .25}`

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/initializers.py#L172)</span>
### PWMBiasInitializer

```python
concise.initializers.PWMBiasInitializer(pwm_list=[], kernel_size=None, mean_max_scale=0.0)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/initializers.py#L222)</span>
### PWMKernelInitializer

```python
concise.initializers.PWMKernelInitializer(pwm_list=[], stddev=0.05, seed=None)
```

truncated normal distribution shifted by a PWM

__Arguments__

- __pwm_list__: a list of PWM's or motifs
- __stddev__: a python scalar or a scalar tensor. Standard deviation of the
  random values to generate.
- __seed__: A Python integer. Used to seed the random generator.
