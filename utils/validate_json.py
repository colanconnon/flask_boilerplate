from functools import wraps
from flask import request, jsonify

class ValidationError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, message):
        self.message = message

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except Exception as e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_json_schema(arguements):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                for arguement in arguements:
                    nested_args = arguement.split('.')
                    if len(nested_args) == 1:
                        if arguement not in request.json:
                            raise ValidationError(
                                "{} does not exist in the json body".format(arguement)
                            )
                    else:
                        r_json = request.json
                        for n_arg in nested_args:
                            if n_arg not in r_json:
                                raise ValidationError(
                                    "{} does not exist in the json body".format(arguement)
                                )
                            else:
                                r_json = r_json[n_arg]
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator
