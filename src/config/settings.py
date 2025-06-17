from .env_variables import env_variables

class Settings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
        return cls._instance
    
    def getConfigVariables(self):
        return env_variables
        
    
    