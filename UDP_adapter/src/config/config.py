import os
from typing import get_type_hints, Union


class EnvMapError(Exception):
	pass


class EnvRequiredError(EnvMapError):
	pass


class EnvCastError(EnvMapError):
	pass


# Returns the same class as was passed in, with dunder methods added based on the fields defined in the class.
def envclass(cls):
	"""
	Returns the same class as was passed in, with its field mapped to environment variables

	Examines PEP 526 __annotations__ to determine fields.

	Maps environment variables to class fields according to these rules:
		- Field won't be parsed unless it has a type annotation
		- Field will be skipped if not in all caps
		- Class field and environment variable name are the same

	A field with type bool will be True with the environment variable with value ['true', 'yes', '1']
	"""

	def wrap(cls):
		return _process_class(cls)

	# See if we're being called as @dataclass or @dataclass().
	if cls is None:
		# We're called with parens.
		return wrap

	# We're called as @envclass without parens.
	return wrap(cls)


def _parse_bool(val: Union[str, bool]) -> bool:  # pylint: disable=E1136
	return val if type(val) == bool else val.lower() in ['true', 'yes', '1']


def _process_class(cls):
	env = os.environ
	for field in cls.__annotations__:
		if not field.isupper():
			# Field will be skipped if not in all caps
			continue

		# Raise EnvRequiredError if required field not supplied
		default_value = getattr(cls, field, None)
		if default_value is None and env.get(field) is None:
			raise EnvRequiredError(f"The {field} field is required")

		# Cast env var value to expected type and raise EnvCastError on failure
		try:
			var_type = get_type_hints(cls)[field]
			if var_type == bool:
				value = _parse_bool(env.get(field, default_value))
			else:
				value = var_type(env.get(field, default_value))

			setattr(cls, field, value)
		except ValueError:
			raise EnvCastError(f'Unable to cast value of "{env[field]}" to type "{var_type}" for "{field}"')

	return cls
