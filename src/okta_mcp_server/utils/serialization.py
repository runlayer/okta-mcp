def serialize_okta_object(obj):
    """Convert an Okta SDK object to a JSON-serializable dict.

    Handles single objects and lists. Objects with an `as_dict()` method
    (all okta-sdk-python model classes) are converted; everything else
    passes through unchanged.
    """
    if isinstance(obj, list):
        return [serialize_okta_object(item) for item in obj]
    if hasattr(obj, "as_dict"):
        return obj.as_dict()
    return obj
