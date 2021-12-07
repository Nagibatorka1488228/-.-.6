def rot(num: int) -> int:
l = list(map(int, str(num)))
for idx, i in enumerate(l):
if i == 6:
l[idx] = 9
break
return int(''.join(map(str, l)))

assert rot(9669) == 9969
assert rot(9996) == 9999
assert rot(9999) == 9999
print('OK')
