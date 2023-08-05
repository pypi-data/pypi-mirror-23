from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow.python.ops import control_flow_ops


def dot(x, y):
  """Compute dot product between a 2-D tensor and a 1-D tensor.

  If x is a ``[M x N]`` matrix, then y is a ``M``-vector.

  If x is a ``M``-vector, then y is a ``[M x N]`` matrix.

  Parameters
  ----------
  x : tf.Tensor
    A 1-D or 2-D tensor (see above).
  y : tf.Tensor
    A 1-D or 2-D tensor (see above).

  Returns
  -------
  tf.Tensor
    A 1-D tensor of length ``N``.

  Raises
  ------
  InvalidArgumentError
    If the inputs have Inf or NaN values.
  """
  x = tf.convert_to_tensor(x)
  y = tf.convert_to_tensor(y)
  dependencies = [tf.verify_tensor_all_finite(x, msg=''),
                  tf.verify_tensor_all_finite(y, msg='')]
  x = control_flow_ops.with_dependencies(dependencies, x)
  y = control_flow_ops.with_dependencies(dependencies, y)

  if len(x.shape) == 1:
    vec = x
    mat = y
    return tf.reshape(tf.matmul(tf.expand_dims(vec, 0), mat), [-1])
  else:
    mat = x
    vec = y
    return tf.reshape(tf.matmul(mat, tf.expand_dims(vec, 1)), [-1])


def logit(x):
  """Evaluate :math:`\log(x / (1 - x))` elementwise.

  Parameters
  ----------
  x : tf.Tensor
    A n-D tensor.

  Returns
  -------
  tf.Tensor
    A tensor of same shape as input.

  Raises
  ------
  InvalidArgumentError
    If the input is not between :math:`(0,1)` elementwise.
  """
  x = tf.convert_to_tensor(x)
  dependencies = [tf.assert_positive(x),
                  tf.assert_less(x, 1.0)]
  x = control_flow_ops.with_dependencies(dependencies, x)

  return tf.log(x) - tf.log(1.0 - x)


def rbf(X, X2=None, lengthscale=1.0, variance=1.0):
  """Radial basis function kernel, also known as the squared
  exponential or exponentiated quadratic. It is defined as

  .. math::

    k(x, x') = \\sigma^2 \exp\Big(
        -\frac{1}{2} \sum_{d=1}^D \frac{1}{\\ell_d^2} (x_d - x'_d)^2 \Big)

  for output variance :math:`\\sigma^2` and lengthscale :math:`\\ell^2`.

  The kernel is evaluated over all pairs of rows, ``k(X[i, ], X2[j, ])``.
  If ``X2`` is not specified, then it evaluates over all pairs
  of rows in ``X``, ``k(X[i, ], X[j, ])``. The output is a matrix
  where each entry (i, j) is the kernel over the ith and jth rows.

  Parameters
  ----------
  X : tf.Tensor
    N x D matrix of N data points each with D features.
  X2 : tf.Tensor, optional
    N x D matrix of N data points each with D features.
  lengthscale : tf.Tensor, optional
    Lengthscale parameter, a positive scalar or D-dimensional vector.
  variance : tf.Tensor, optional
    Output variance parameter, a positive scalar.

  Examples
  --------
  >>> X = tf.random_normal([100, 5])
  >>> K = ed.rbf(X)
  >>> assert K.shape == (100, 100)
  """
  lengthscale = tf.convert_to_tensor(lengthscale)
  variance = tf.convert_to_tensor(variance)
  dependencies = [tf.assert_positive(lengthscale),
                  tf.assert_positive(variance)]
  lengthscale = control_flow_ops.with_dependencies(dependencies, lengthscale)
  variance = control_flow_ops.with_dependencies(dependencies, variance)

  X = tf.convert_to_tensor(X)
  X = X / lengthscale
  Xs = tf.reduce_sum(tf.square(X), 1)
  if X2 is None:
    X2 = X
    X2s = Xs
  else:
    X2 = tf.convert_to_tensor(X2)
    X2 = X2 / lengthscale
    X2s = tf.reduce_sum(tf.square(X2), 1)

  square = tf.reshape(Xs, [-1, 1]) + tf.reshape(X2s, [1, -1]) - \
      2 * tf.matmul(X, X2, transpose_b=True)
  output = variance * tf.exp(-square / 2)
  return output


def reduce_logmeanexp(input_tensor, axis=None, keep_dims=False):
  """Computes log(mean(exp(elements across dimensions of a tensor))).

  Parameters
  ----------
  input_tensor : tf.Tensor
    The tensor to reduce. Should have numeric type.
  axis : int or list of int, optional
    The dimensions to reduce. If `None` (the default), reduces all
    dimensions.
  keep_dims : bool, optional
    If true, retains reduced dimensions with length 1.

  Returns
  -------
  tf.Tensor
    The reduced tensor.
  """
  logsumexp = tf.reduce_logsumexp(input_tensor, axis, keep_dims)
  input_tensor = tf.convert_to_tensor(input_tensor)
  n = input_tensor.shape.as_list()
  if axis is None:
    n = tf.cast(tf.reduce_prod(n), logsumexp.dtype)
  else:
    n = tf.cast(tf.reduce_prod(n[axis]), logsumexp.dtype)

  return -tf.log(n) + logsumexp


def to_simplex(x):
  """Transform real vector of length ``(K-1)`` to a simplex of dimension ``K``
  using a backward stick breaking construction.

  Parameters
  ----------
  x : tf.Tensor
    A 1-D or 2-D tensor.

  Returns
  -------
  tf.Tensor
    A tensor of same shape as input but with last dimension of
    size ``K``.

  Raises
  ------
  InvalidArgumentError
    If the input has Inf or NaN values.

  Notes
  -----
  x as a 3-D or higher tensor is not guaranteed to be supported.
  """
  x = tf.cast(x, dtype=tf.float32)
  dependencies = [tf.verify_tensor_all_finite(x, msg='')]
  x = control_flow_ops.with_dependencies(dependencies, x)

  if isinstance(x, (tf.Tensor, tf.Variable)):
    shape = x.get_shape().as_list()
  else:
    shape = x.shape

  if len(shape) == 1:
    K_minus_one = shape[0]
    eq = -tf.log(tf.cast(K_minus_one - tf.range(K_minus_one), dtype=tf.float32))
    z = tf.sigmoid(eq + x)
    pil = tf.concat([z, tf.constant([1.0])], 0)
    piu = tf.concat([tf.constant([1.0]), 1.0 - z], 0)
    S = tf.cumprod(piu)
    return S * pil
  else:
    n_rows = shape[0]
    K_minus_one = shape[1]
    eq = -tf.log(tf.cast(K_minus_one - tf.range(K_minus_one), dtype=tf.float32))
    z = tf.sigmoid(eq + x)
    pil = tf.concat([z, tf.ones([n_rows, 1])], 1)
    piu = tf.concat([tf.ones([n_rows, 1]), 1.0 - z], 1)
    S = tf.cumprod(piu, axis=1)
    return S * pil


def get_control_variate_coef(f, h):
  """Returns scalar used by control variates method for variance reduction in
  MCMC methods.

  If we have a statistic :math:`m` unbiased estimator of :math:`\mu` and
  and another statistic :math:`t` which is an unbiased estimator of
  :math:`\tau` then :math:`m^* = m + c(t - \tau)` is also an unbiased
  estimator of :math:`\mu' for any coefficient :math:`c`.

  This function calculates the optimal coefficient
  .. math::

    \c^* = \frac{Cov(m,t)}{Var(t)}

  for minimizing the variance of :math:`m^*`.

  Parameters
  ----------
  f : tf.Tensor
    A 1-D tensor.
  h : tf.Tensor
    A 1-D tensor.

  Returns
  -------
  tf.Tensor
    A 0 rank tensor
  """
  f_mu = tf.reduce_mean(f)
  h_mu = tf.reduce_mean(h)

  n = f.shape[0].value

  cov_fh = tf.reduce_sum((f - f_mu) * (h - h_mu)) / (n - 1)
  var_h = tf.reduce_sum(tf.square(h - h_mu)) / (n - 1)

  a = cov_fh / var_h

  return a
