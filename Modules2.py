# Whenever we are importing any module, that module executable code will run

import Modules1

Modules1.tetsingModuleFunc()

x = Modules1.sum(10, 13)
print(x)


# We need to create pbject of class written in any module
object = Modules1.A()
object.testing()