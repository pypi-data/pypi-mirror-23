<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/hyopt.py#L78)</span>
### CMongoTrials

```python
concise.hyopt.CMongoTrials(db_name, exp_name, ip='ouga03', port=1234, kill_timeout=None)
```

----

<span style="float:right;">[[source]](https://github.com/avsecz/concise/blob/master/concise/hyopt.py#L380)</span>
### CompileFN

```python
concise.hyopt.CompileFN(db_name, exp_name, data_fn, model_fn, add_eval_metrics=[], loss_metric='loss', loss_metric_mode='min', valid_split=0.2, cv_n_folds=None, stratified=False, random_state=None, use_tensorboard=False, save_model='best', save_results=True, save_dir='/s/project/deepcis/hyperopt/')
```

----

### test_fn


```python
test_fn(fn, hyper_params, n_train=1000, tmp_dir='/tmp/concise_hyopt_test/')
```


Test the correctness of the function before executing on large scale
1. Run without error
2. Correct save/load model to disk

__Arguments__

- __fn__: CompileFN instance
- __hyper_params__: pyll graph of hyper-parameters - as later provided to `hyperopt.fmin`
- __n_train__: int, number of training points
- __tmp_dir__: Temporary path where to write the trained model.

----

### eval_model


```python
eval_model(model, test, add_eval_metrics={})
```
