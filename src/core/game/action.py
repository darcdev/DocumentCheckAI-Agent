class Action:
    """
    An action is a function that the agent can take.
    """
    def __init__(self, name, function, description, terminal, parameters):
        self.name = name
        self.function = function
        self.description = description
        self.parameters = parameters
        self.terminal = terminal
    
    def _execute(self, **args):
        """
        Execute the action with the given arguments.
        """
        self.function(**args)
        
        
        