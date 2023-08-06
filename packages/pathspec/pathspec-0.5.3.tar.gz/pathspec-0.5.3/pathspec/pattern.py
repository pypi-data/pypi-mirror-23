# encoding: utf-8
"""
This module provides the base definition for patterns.
"""

import re

from .compat import unicode


class Pattern(object):
	"""
	The ``Pattern`` class is the abstract definition of a pattern.
	"""

	# Make the class dict-less.
	__slots__ = ('include',)

	def __init__(self, include):
		"""
		Initializes the ``Pattern`` instance.

		*include* (``bool``) is whether the matched files should be included
		(``True``), excluded (``False``), or is a null-operation (``None``).
		"""

		self.include = include
		"""
		*include* (``bool``) is whether the matched files should be included
		(``True``), excluded (``False``), or is a null-operation (``None``).
		"""

	def match(self, files):
		"""
		Matches this pattern against the specified files.

		*files* (``collections.Iterable``) contains each file (``str``)
		relative to the root directory (e.g., "relative/path/to/file").

		Returns an ``collections.Iterable`` yielding each matched file path
		(``str``).
		"""
		raise NotImplementedError("{0}.{1} must override match().".format(self.__class__.__module__, self.__class__.__name__))


class RegexPattern(Pattern):
	"""
	The ``RegexPattern`` class is an implementation of a pattern using
	regular expressions.
	"""

	# Make the class dict-less.
	__slots__ = ('regex',)

	def __init__(self, pattern, include=None):
		"""
		Initializes the ``RegexPattern`` instance.

		*pattern* (``unicode``, ``bytess, ``re.RegexObject``, or ``None``)
		is the pattern to compile into a regular expression.

		*include* (``bool`` or ``None``) must be ``None`` unless *pattern*
		is a precompiled regular expression (``re.RegexObject``) in which
		case it is whether matched files should be included (``True``),
		excluded (``False``), or is a null operation.

		.. NOTE:: Subclasses do not need to support the *include* parameter.
		"""

		self.regex = None
		"""
		*regex* (``re.RegexObject``) is the regular expression for the
		pattern.
		"""

		if isinstance(pattern, (unicode, bytes)):
			assert include is None, "include:{0!r} must be null when pattern:{1!r} is a string.".format(include, pattern)
			regex, include = self.pattern_to_regex(pattern)
			# NOTE: Make sure to allow a null regular expression to be
			# returned for a null-operation.
			if include is not None:
				regex = re.compile(regex)

		elif pattern is not None and hasattr(pattern, 'match'):
			# Assume pattern is a precompiled regular expression.
			# - NOTE: Used specified *include*.
			regex = pattern

		elif pattern is None:
			# NOTE: Make sure to allow a null pattern to be passed for a
			# null-operation.
			assert include is None, "include:{0!r} must be null when pattern:{1!r} is null.".format(include, pattern)

		else:
			raise TypeError("pattern:{0!r} is not a string, RegexObject, or None.".format(pattern))

		super(RegexPattern, self).__init__(include)
		self.regex = regex

	def __eq__(self, other):
		"""
		Tests the equality of this ``RegexPattern`` with *other* based on
		their *pattern* and *include* attributes.

		*other* (``RegexPattern``) is the other pattern to compare against.

		Returns whether the patterns are equal (``True``), or not
		(``False``).
		"""
		if isinstance(other, RegexPattern):
			return self.include == other.include and self.regex == other.regex
		else:
			return NotImplemented

	def match(self, files):
		"""
		Matches this pattern against the specified files.

		*files* (``collections.Iterable``) contains each file (``str``)
		relative to the root directory (e.g., "relative/path/to/file").

		Returns an ``collections.Iterable`` yielding each matched file path
		(``str``).
		"""
		if self.include is not None:
			for path in files:
				if self.regex.match(path) is not None:
					yield path

	@classmethod
	def pattern_to_regex(cls, pattern):
		"""
		Convert the pattern into an uncompiled regular expression.

		*pattern* (``str``) is the pattern to convert into a regular
		expression.

		Returns the uncompiled regular expression (``str`` or ``None``), and
		whether matched files should be included (``True``), excluded
		(``False``), or is a null-operation (``None``).

		.. NOTE:: The default implementation simply returns *pattern* and
		   ``True``.
		"""
		return pattern, True
