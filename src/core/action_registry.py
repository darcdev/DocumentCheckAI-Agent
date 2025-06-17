from core.action import Action
from typing import Dict, List

class ActionRegistry:
    def __init__(self):
        self.actions = {}
    
    def register(self, action : Action):
        self.actions[action.name] = action
    
    def get_action(self, name : str) -> [Action, None]:
        return self.actions.get(name, None)
    
    def get_actions(self) -> List[Action]:
        return list(self.actions.values())