print 3 * 'un' + 'ium'
print '4' '2'
fas = 'hello world'
print fas[2:-1]
print fas[:2] + fas[2:]

print len(fas)
nums = [1, 2, 3]
squares = [1, 4, 9]
res = nums + squares
res.append(100)
res[2:5] = ['a', 'b', 'c']
print len(res)
for i in res:
    print i
