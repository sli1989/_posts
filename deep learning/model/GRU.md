---
title: GRU的源码实现
abbrlink: c79f2f90
categories:
  - deep learning
  - model
date: 2018-02-06 19:08:53
---
# GRU的实现源码

## GRU-tensorflow



```python

def call(self, inputs, state):
  """Gated recurrent unit (GRU) with nunits cells."""

  gate_inputs = math_ops.matmul(
      array_ops.concat([inputs, state], 1), self._gate_kernel)
  gate_inputs = nn_ops.bias_add(gate_inputs, self._gate_bias)

  value = math_ops.sigmoid(gate_inputs)
  r, u = array_ops.split(value=value, num_or_size_splits=2, axis=1)

  r_state = r * state

  candidate = math_ops.matmul(
      array_ops.concat([inputs, r_state], 1), self._candidate_kernel)
  candidate = nn_ops.bias_add(candidate, self._candidate_bias)

  c = self._activation(candidate)
  new_h = u * state + (1 - u) * c
  return new_h, new_h
```

## pytorch
