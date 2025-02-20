# Save the original __new__ method
original_new = type

def add_repr(cls):
    """Decorator to add custom representation to a specific class."""
    def custom_repr(self):
        attribute_list = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                formatted_value = f'"{value}"'
            else:
                formatted_value = repr(value)
            attribute_string = f"{key}: {formatted_value}"
            attribute_list.append(attribute_string)
        attributes_string = ", ".join(attribute_list)
        result = f"{self.__class__.__name__}({attributes_string})"
        return result
    
    # Only set __repr__ if it hasn't been explicitly defined
    if '__repr__' not in cls.__dict__:
        cls.__repr__ = custom_repr
    return cls


