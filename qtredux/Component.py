import os
from collections.abc import Iterable
from PyQt5 import QtWidgets

def wrap(x):
    if isinstance(x, Iterable):
        return x
    return (x,)

class qtComponent():
    
    required_args = set()  # To be overridden by subclasses
    required_props = set()  # To be overridden by subclasses
    
    def __init__(self, *a, args = None, props = None, **kwargs):
        '''
        :param a: other arguments to pass to the next constructor on the MRO
        :type a: tuple
        :param args: arguments, not expected to change after construction
        :type args: dict
        :param props: properties, set externally and expected to be changed after construction
        :type props: dict
        :param kwargs: other keyword arguments to pass to the next constructor on the MRO
        :type kwargs: dict
        '''
        super().__init__(*a, **kwargs)
        missing_args = {arg for arg in self.__class__.required_args if arg not in args}
        if missing_args:
            raise ValueError(f'Missing arguments {missing_args}')
        self.args = args or {}
        self.props = props or {}
        self.props_changed = set(self.props.keys())
        self.state = {}
        self.state_changed = set()
        self.children = {}
        
        self.uiInit()
        self.update()
        self.renderStyle()

    def uiInit(self):
        pass  # To be overridden by subclasses
    def renderStyle(self):
        pass  # To be overridden by subclasses
    def update(self):
        pass  # To be overridden by subclasses
    def missingProps(self):
        missing_props = {prop for prop in self.__class__.required_props if prop not in self.props}
        return missing_props

    def setProps(self, **kwargs):
        'For use by parent widgets.'
        self.props.update(**kwargs)
        self.props_changed = self.props_changed.union(set(kwargs.keys()))  # So that you can save some computations
        return self.update()
    
    def setState(self, **kwargs):
        'For use by self.'
        self.state.update(**kwargs)
        self.state_changed = self.state_changed.union(set(kwargs.keys()))  # So that you can save some computations
        return self.update()

    def __getitem__(self, key): # Children access shorthand
        return self.children[key]
    def __setitem__(self, key, value: QtWidgets.QWidget):  # Children access shorthand
        self.children[key] = value
    def __iter__(self):  # Children access shorthand
        return self.children.__iter__()
    def setChildren(self, **kwargs):  # Children access shorthand
        self.children.update(**kwargs)

    def attachChildren(self, layout, args = {}):  # No more messy layout.addWidget() stuff
        for child in self:
            if child in args:
                layout.addWidget(self[child], *wrap(args[child]))
            else:
                layout.addWidget(self[child])

class qtWrapper(qtComponent, QtWidgets.QWidget):
    '''
    Required args: layout, children\n
    Optional args: layout_args = {}\n
    '''
    def uiInit(self):
        
        if 'layout_args' not in self.args:
            self.args['layout_args'] = {}
            
        self.layout = self.args['layout']
        self.setLayout(self.layout)
        self.setChildren(**self.args['children'])
        self.attachChildren(self.layout, self.args['layout_args'])

        return True