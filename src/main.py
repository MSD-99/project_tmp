import src.utils
import src.arithmetic

from src.utils import *
from src.arithmetic import *


print('\n'.join(dir()))

print()
print('-'*50)
print('Calling utils.read_file()\n')
print(src.utils.read_file('src/file.txt'))

print()
print('-'*50)
print('calling arithmetic ...\n')
print(src.arithmetic.operations.add(3, 4))