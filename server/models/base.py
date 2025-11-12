# filepath: server/models/base.py
from . import db

class BaseModel(db.Model):
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name, value, min_length=2, allow_none=False):
        """Validate that a string field meets minimum length requirements.
        
        Args:
            field_name: Name of the field being validated (for error messages)
            value: The value to validate
            min_length: Minimum required length for the string (default: 2)
            allow_none: Whether None values are acceptable (default: False)
            
        Returns:
            The validated value if it passes all checks
            
        Raises:
            ValueError: If the value is None and allow_none is False
            ValueError: If the value is not a string
            ValueError: If the string length is less than min_length
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value