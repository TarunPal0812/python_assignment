def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


nested =  {"a": 10, "b": {"c": {"d": 20}}, "e": 100} 
print(flatten_dict(nested, sep='.'))

# Output: {'a': 10, 'b.c.d': 20, 'e': 100}
