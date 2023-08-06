"""CODA Modelling Tools.

References
----------

  - M.H. Eres et al, 2014. Mapping Customer Needs to Engineering
	Characteristics: An Aerospace Perspective for Conceptual Design -
	Journal of Engineering Design pp. 1-24
"""
import abc

import numpy as np


class CODA(object):

	@property
	def array(self):
		"""2D array of relationship functions."""
		try:
			array = self._array

		except AttributeError:
			array = self._array = self._create_array()

		shape = array.shape
		if shape != self.shape:
			new_array = self._create_array()
			new_array[0:shape[0],0:shape[1]] = array
			self._array = array = new_array

		return array

	@property
	def characteristics(self):
		"""Modelled characteristics."""
		if not hasattr(self, '_characteristics'):
			self._characteristics = ()
		return self._characteristics
	@characteristics.setter
	def characteristics(self, tup):
		if (isinstance(tup, tuple) and
			all([isinstance(x, BaseCharacteristic) for x in tup])):
			self._characteristics = tup
		else:
			raise ValueError("Value must be tuple of characteristics.")

	@property
	def requirements(self):
		"""Modelled requirements."""
		if not hasattr(self, '_requirements'):
			self._requirements = ()
		return self._requirements
	@requirements.setter
	def requirements(self, tup):
		if (isinstance(tup, tuple) and
			all([isinstance(x, BaseRequirement) for x in tup])):
			self._requirements = tup
		else:
			raise ValueError("Value must be tuple of requirements.")

	@property
	def shape(self):
		"""Return shape of model (M, N).

			M - Number of requirements
			N - Number of characteristics
		"""
		return len(self.requirements), len(self.characteristics)

	def _create_array(self):
		# Create an array sized by the shape of the coda model and
		# populate with Null relationships.
		array = np.empty(self.shape, dtype=object)
		array[:] = CODANull()
		return array


class CODARelationship(object):
	"""Relationship between a requirement and characteristic.

	Concrete implementations of this class are callables returning
	merit.
	"""
	__metaclass__ = abc.ABCMeta

	__valid_correlations = {0.0, 0.1, 0.3, 0.9}

	def __init__(self, correlation, target):
		"""
			correlation: real in {0.0, 0.1, 0.3, 0.9}
				Correlation strength between requirement and
				characteristic.

			target: real
				Target value of characteristic parameter.
		"""
		self.correlation = correlation
		self.target = target

	@property
	def correlation(self):
		return self._correlation
	@correlation.setter
	def correlation(self, value):
		if value not in self.__valid_correlations:
			raise ValueError("Invalid correlation value.")
		self._correlation = value

	@property
	def target(self):
		return self._target
	@target.setter
	def target(self, value):
		self._target = value

	@abc.abstractmethod
	def __call__(self, x):
		return 0.0


class CODANull(CODARelationship):
	"""Null relationship.

	Models the absence of a requirement-characteristic relationship,
	in other words the characteristic has no bearing on the
	requirement.
	"""

	def __init__(self):
		super(CODANull, self).__init__(0.0, None)

	@CODARelationship.correlation.setter
	def correlation(self, value):
		if value != 0.0:
			raise TypeError("Fixed correlation value.")
		else:
			self._correlation = value

	@CODARelationship.target.setter
	def target(self, value):
		if value is not None:
			raise TypeError("Fixed target value.")
		else:
			self._target = value

	def __call__(self, x):
		return 0.0






class BaseCharacteristic(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractproperty
	def value(self):
		return


class BaseRequirement(object):
	__metaclass__ = abc.ABCMeta


class CODACharacteristic(BaseCharacteristic):
	"""Design characteristic model."""

	def __init__(self, context, name,
