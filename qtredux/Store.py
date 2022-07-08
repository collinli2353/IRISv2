class Store():

    state = None
    listeners = []
    
    def __init__(self, reducer=None):
        
        if reducer is not None:
            self._setReducer(reducer)

    @classmethod
    def _setReducer(cls, reducer):
        
        cls.reducer = reducer
        cls.state = cls.reducer(cls.state)

    @classmethod
    def subscribe(cls, listener, action_types=[]):
        
        cls.listeners.append([listener,action_types])
    
    @classmethod
    def getState(cls):
        
        return cls.state

    @classmethod
    def dispatch(cls, action):
        
        def checkTypeValid(acts, action_types):
            
            if type(acts)==dict:
                return acts['type'] in action_types
            
            for act in acts:
                if act['type'] in action_types:
                    return True
            
            return False
            
        cls.state = cls.reducer(cls.state, action)
        for listener, action_types in cls.listeners:
            if checkTypeValid(action, action_types):
                listener()