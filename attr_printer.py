# -*- coding: utf-8 -*-
def attr_printer(obj, known_objects=None, stack=None):
    if stack is None:
        known_objects = {}
        stack = []
    if isinstance(obj, (int, float, bytes, str)) or obj.__class__.__name__ == 'ndarray':
        print('ax' + ''.join(stack), '=', repr(obj).replace('\n', ''))
    elif isinstance(obj, (list, tuple, set)):
        for i, sub_obj in enumerate(obj):
            stack.append('[' + str(i) + ']')
            known_objects[id(sub_obj)] = min(len(stack), known_objects.get(id(sub_obj), 999))
            attr_printer(sub_obj, known_objects, stack)
            stack.pop()
    elif isinstance(obj, (dict, OrderedDict)):
        for key, sub_obj in obj.items():
            stack.append('[' + repr(key) + ']')
            known_objects[id(sub_obj)] = min(len(stack), known_objects.get(id(sub_obj), 999))
            attr_printer(sub_obj, known_objects, stack)
            stack.pop()
    elif 'function' in obj.__class__.__name__:
        return
    else:
        for atr in (x for x in dir(obj) if not x.startswith('__')):
            try:
                sub_obj = obj.__getattribute__(atr)
            except TypeError:
                continue
            if id(sub_obj) in known_objects and len(stack) > known_objects[id(sub_obj)]:
                continue
            stack.append('.' + atr)
            known_objects[id(sub_obj)] = min(len(stack), known_objects.get(id(sub_obj), 999))
            attr_printer(sub_obj, known_objects, stack)
            stack.pop()
