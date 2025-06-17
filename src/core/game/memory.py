from typing import List, Dict

class Memory:
    """
    A memory is a collection of items that the agent can use to remember things.
    """
    def __init__(self):
        self.items = []
    
    def add_memory(self,memory : dict):
        self.items.append(item)
    
    def get_memories(self, limit: int = None) -> List[Dict]:
        return self.items[:limit]
    
    def copy_without_system_memories(self):
        filtered_items = [memory for memory in self.items if memory.get("type") != "system"]
        memory = Memory()
        memory.items = filtered_items
        return memory
        