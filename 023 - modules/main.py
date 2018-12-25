# import module
import mathematic as math

math.tambah(10,20)
math.kurang(30,10)

# Import function only
from mathematic import tambah, kurang

# Import all => from mathematic import *
tambah(90,10)
kurang(300,50)

# Import function only as alias
from mathematic import tambah as plus
plus(20,30)
