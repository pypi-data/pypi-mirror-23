from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

try:
  from tensorflow.python.client.session import \
      register_session_run_conversion_functions
except Exception as e:
  raise ImportError("{0}. Your TensorFlow version is not supported.".format(e))

RANDOM_VARIABLE_COLLECTION = "random_variables"


class RandomVariable(object):
  """Base class for random variables.

  A random variable is an object parameterized by tensors. It is
  equipped with methods such as the log-density, mean, and sample.

  It also wraps a tensor, where the tensor corresponds to a sample
  from the random variable. This enables operations on the TensorFlow
  graph, allowing random variables to be used in conjunction with
  other TensorFlow ops.

  The random variable's shape is given by

  ``sample_shape + batch_shape + event_shape``,

  where ``sample_shape`` is an optional argument representing the
  dimensions of samples drawn from the distribution (default is
  a scalar); ``batch_shape`` is the number of independent random variables
  (determined by the shape of its parameters); and ``event_shape`` is
  the shape of one draw from the distribution (e.g., ``Normal`` has a
  scalar ``event_shape``; ``Dirichlet`` has a vector ``event_shape``).

  Notes
  -----
  ``RandomVariable`` assumes use in a multiple inheritance setting. The
  child class must first inherit ``RandomVariable``, then second inherit a
  class in ``tf.contrib.distributions``. With Python's method resolution
  order, this implies the following during initialization (using
  ``distributions.Bernoulli`` as an example):

  1. Start the ``__init__()`` of the child class, which passes all
     ``*args, **kwargs`` to ``RandomVariable``.
  2. This in turn passes all ``*args, **kwargs`` to
     ``distributions.Bernoulli``, completing the ``__init__()`` of
     ``distributions.Bernoulli``.
  3. Complete the ``__init__()`` of ``RandomVariable``, which calls
     ``self.sample()``, relying on the method from
     ``distributions.Bernoulli``.
  4. Complete the ``__init__()`` of the child class.

  Methods from both ``RandomVariable`` and ``distributions.Bernoulli``
  populate the namespace of the child class. Methods from
  ``RandomVariable`` will take higher priority if there are conflicts.

  Examples
  --------
  >>> p = tf.constant(0.5)
  >>> x = Bernoulli(p)
  >>>
  >>> z1 = tf.constant([[1.0, -0.8], [0.3, -1.0]])
  >>> z2 = tf.constant([[0.9, 0.2], [2.0, -0.1]])
  >>> x = Bernoulli(logits=tf.matmul(z1, z2))
  >>>
  >>> mu = Normal(tf.constant(0.0), tf.constant(1.0))
  >>> x = Normal(mu, tf.constant(1.0))
  """
  def __init__(self, *args, **kwargs):
    """
    Parameters
    ----------
    sample_shape : tf.TensorShape, optional
      Shape of samples to draw from the random variable.
    value : tf.Tensor, optional
      Fixed tensor to associate with random variable. Must have shape
      ``sample_shape + batch_shape + event_shape``.
    collections : list, optional
      Optional list of graph collections keys. The random variable is
      added to these collections. Defaults to ["random_variables"].
    *args, **kwargs
      Passed into parent ``__init__``.
    """
    # pop and store RandomVariable-specific parameters in _kwargs
    sample_shape = kwargs.pop('sample_shape', ())
    value = kwargs.pop('value', None)
    collections = kwargs.pop('collections', [RANDOM_VARIABLE_COLLECTION])

    # store args, kwargs for easy graph copying
    self._args = args
    self._kwargs = kwargs.copy()

    if sample_shape != ():
      self._kwargs['sample_shape'] = sample_shape
    if value is not None:
      self._kwargs['value'] = value
    if collections != [RANDOM_VARIABLE_COLLECTION]:
      self._kwargs['collections'] = collections

    super(RandomVariable, self).__init__(*args, **kwargs)

    self._sample_shape = tf.TensorShape(sample_shape)
    if value is not None:
      t_value = tf.convert_to_tensor(value, self.dtype)
      value_shape = t_value.shape
      expected_shape = self._sample_shape.concatenate(
          self.batch_shape).concatenate(self.event_shape)
      if not value_shape.is_compatible_with(expected_shape):
        raise ValueError(
            "Incompatible shape for initialization argument 'value'. "
            "Expected %s, got %s." % (expected_shape, value_shape))
      else:
        self._value = t_value
    else:
      try:
        self._value = self.sample(self._sample_shape)
      except NotImplementedError:
        raise NotImplementedError(
            "sample is not implemented for {0}. You must either pass in the "
            "value argument or implement sample for {0}."
            .format(self.__class__.__name__))

    with tf.name_scope(self.name) as ns:
      self._unique_name = ns

    for collection in collections:
      tf.add_to_collection(collection, self)

  @property
  def sample_shape(self):
    """Sample shape of random variable."""
    return self._sample_shape

  @property
  def shape(self):
    """Shape of random variable."""
    return self._value.shape

  @property
  def unique_name(self):
    """Name of random variable with its unique scoping name. Use
    ``name`` to just get the name of the random variable."""
    return self._unique_name

  def __str__(self):
    return "RandomVariable(\"%s\"%s%s%s)" % (
        self.unique_name,
        (", shape=%s" % self.shape)
        if self.shape.ndims is not None else "",
        (", dtype=%s" % self.dtype.name) if self.dtype else "",
        (", device=%s" % self.value().device) if self.value().device else "")

  def __repr__(self):
    return "<ed.RandomVariable '%s' shape=%s dtype=%s>" % (
        self.unique_name, self.shape, self.dtype.name)

  def __add__(self, other):
    return tf.add(self, other)

  def __radd__(self, other):
    return tf.add(other, self)

  def __sub__(self, other):
    return tf.subtract(self, other)

  def __rsub__(self, other):
    return tf.subtract(other, self)

  def __mul__(self, other):
    return tf.multiply(self, other)

  def __rmul__(self, other):
    return tf.multiply(other, self)

  def __div__(self, other):
    return tf.div(self, other)

  __truediv__ = __div__

  def __rdiv__(self, other):
    return tf.div(other, self)

  __rtruediv__ = __rdiv__

  def __floordiv__(self, other):
    return tf.floor(tf.div(self, other))

  def __rfloordiv__(self, other):
    return tf.floor(tf.div(other, self))

  def __mod__(self, other):
    return tf.mod(self, other)

  def __rmod__(self, other):
    return tf.mod(other, self)

  def __lt__(self, other):
    return tf.less(self, other)

  def __le__(self, other):
    return tf.less_equal(self, other)

  def __gt__(self, other):
    return tf.greater(self, other)

  def __ge__(self, other):
    return tf.greater_equal(self, other)

  def __and__(self, other):
    return tf.logical_and(self, other)

  def __rand__(self, other):
    return tf.logical_and(other, self)

  def __or__(self, other):
    return tf.logical_or(self, other)

  def __ror__(self, other):
    return tf.logical_or(other, self)

  def __xor__(self, other):
    return tf.logical_xor(self, other)

  def __rxor__(self, other):
    return tf.logical_xor(other, self)

  def __getitem__(self, key):
    """Subset the tensor associated to the random variable, not the
    random variable itself."""
    return self.value()[key]

  def __pow__(self, other):
    return tf.pow(self, other)

  def __rpow__(self, other):
    return tf.pow(other, self)

  def __invert__(self):
    return tf.logical_not(self)

  def __neg__(self):
    return tf.negative(self)

  def __abs__(self):
    return tf.abs(self)

  def __hash__(self):
    return id(self)

  def __eq__(self, other):
    return id(self) == id(other)

  def __iter__(self):
    raise TypeError("'RandomVariable' object is not iterable.")

  def __bool__(self):
    raise TypeError(
        "Using a `ed.RandomVariable` as a Python `bool` is not allowed. "
        "Use `if t is not None:` instead of `if t:` to test if a "
        "random variable is defined, and use TensorFlow ops such as "
        "tf.cond to execute subgraphs conditioned on a draw from "
        "a random variable.")

  def __nonzero__(self):
    raise TypeError(
        "Using a `ed.RandomVariable` as a Python `bool` is not allowed. "
        "Use `if t is not None:` instead of `if t:` to test if a "
        "random variable is defined, and use TensorFlow ops such as "
        "tf.cond to execute subgraphs conditioned on a draw from "
        "a random variable.")

  def eval(self, session=None, feed_dict=None):
    """In a session, computes and returns the value of this random variable.

    This is not a graph construction method, it does not add ops to the graph.

    This convenience method requires a session where the graph
    containing this variable has been launched. If no session is
    passed, the default session is used.

    Parameters
    ----------
    session : tf.BaseSession, optional
      The ``tf.Session`` to use to evaluate this random variable. If
      none, the default session is used.
    feed_dict : dict, optional
      A dictionary that maps ``tf.Tensor`` objects to feed values. See
      ``tf.Session.run()`` for a description of the valid feed values.

    Examples
    --------
    >>> x = Normal(0.0, 1.0)
    >>> with tf.Session() as sess:
    >>>   # Usage passing the session explicitly.
    >>>   print(x.eval(sess))
    >>>   # Usage with the default session.  The 'with' block
    >>>   # above makes 'sess' the default session.
    >>>   print(x.eval())
    """
    return self.value().eval(session=session, feed_dict=feed_dict)

  def value(self):
    """Get tensor that the random variable corresponds to."""
    return self._value

  def get_ancestors(self, collection=None):
    """Get ancestor random variables."""
    from edward.util.random_variables import get_ancestors
    return get_ancestors(self, collection)

  def get_blanket(self, collection=None):
    """Get the random variable's Markov blanket."""
    from edward.util.random_variables import get_blanket
    return get_blanket(self, collection)

  def get_children(self, collection=None):
    """Get child random variables."""
    from edward.util.random_variables import get_children
    return get_children(self, collection)

  def get_descendants(self, collection=None):
    """Get descendant random variables."""
    from edward.util.random_variables import get_descendants
    return get_descendants(self, collection)

  def get_parents(self, collection=None):
    """Get parent random variables."""
    from edward.util.random_variables import get_parents
    return get_parents(self, collection)

  def get_siblings(self, collection=None):
    """Get sibling random variables."""
    from edward.util.random_variables import get_siblings
    return get_siblings(self, collection)

  def get_variables(self, collection=None):
    """Get TensorFlow variables that the random variable depends on."""
    from edward.util.random_variables import get_variables
    return get_variables(self, collection)

  def get_shape(self):
    """Get shape of random variable."""
    return self.shape

  @staticmethod
  def _session_run_conversion_fetch_function(tensor):
    return ([tensor.value()], lambda val: val[0])

  @staticmethod
  def _session_run_conversion_feed_function(feed, feed_val):
    return [(feed.value(), feed_val)]

  @staticmethod
  def _session_run_conversion_feed_function_for_partial_run(feed):
    return [feed.value()]

  @staticmethod
  def _tensor_conversion_function(v, dtype=None, name=None, as_ref=False):
    _ = name, as_ref
    if dtype and not dtype.is_compatible_with(v.dtype):
      raise ValueError(
          "Incompatible type conversion requested to type '%s' for variable "
          "of type '%s'" % (dtype.name, v.dtype.name))
    return v.value()


register_session_run_conversion_functions(
    RandomVariable,
    RandomVariable._session_run_conversion_fetch_function,
    RandomVariable._session_run_conversion_feed_function,
    RandomVariable._session_run_conversion_feed_function_for_partial_run)

tf.register_tensor_conversion_function(
    RandomVariable, RandomVariable._tensor_conversion_function)
