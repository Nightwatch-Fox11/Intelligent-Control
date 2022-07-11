from torch.nn.modules.utils import _triple, _single

a = ((3, 3, 4), (3, 1, 4), (3, 2, 4))
b = (3, 4, 1)
c = 3
# print(_single(a))
# print(_triple(a))
# print(_triple(a))
# print(a(1))
print(_triple(b))
print(_triple(c))
