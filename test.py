from typing import Type
class A(object):
    def print(self):
        print('hello')


print(type(Type[A]))