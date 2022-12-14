basketball = set(['John', 'Mohamed', 'Mike', 'Ismail',])
baseball = set(['Yusuf', 'Mohamed', 'Mike', 'Ismail'])

print('The following students are on the baseball team: ')
for name in baseball:
    print(name)

print('The following students are on the basketball team: ')
for name in basketball:
    print(name)

print()
print('The following students play both: ')
for name in baseball.intersection(basketball):
    print(name)

print()
print('The following students play either:')
for name in baseball.union(basketball):
    print(name)

print()
print('The following students play baseball, but not basketball: ')
for name in baseball.difference(basketball):
    print(name)

