import inspect
import pprint


def introspection_info(obj):
    attributes = []
    methods = []
    for name in dir(obj):
        if callable(getattr(obj,name)) is True:
            methods.append(name)
        else:
            attributes.append(name)
    return {'type': type(obj).__name__,
            'attributes':  attributes,
            'methods': methods,
            'module': inspect.getmodule(obj)}


number_info = introspection_info(42)
pprint.pprint(number_info)



