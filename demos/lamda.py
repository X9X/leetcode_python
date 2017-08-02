def log(prefix):
    return lambda content: prefix + content

log1 = log('hello')
print log1('world')
print log1('tom')
