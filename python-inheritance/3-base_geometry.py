#!/usr/bin/python3
'''creating an empty class script'''
class BaseGeometryMetaClass(type):
    '''
    creating the meta Class to remove unwanted subclasses.
    '''
    def __dir__(cls):
        '''
        function method creats a list of all attributes for the class and excludes the init_subclass.
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass = BaseGeometryMetaClass):
    '''empty class created'''
    def __dir__(cls):
        '''
        function method creats a list of all attributes for the class and excludes the init_subclass.
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    pass