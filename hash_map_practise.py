
from hash_map import HashMap

hash_map = HashMap(3)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
hash_map.assign('stone', 'simple')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
print(hash_map.retrieve('stone'))

hash_map.remove('gabbro')

print(hash_map.retrieve('gabbro'))
