''' A character in DnD
'''
import os
from data import _R

class Trait:
    """Characters carry traits, which affect their skills

    http://dungeons.wikia.com/wiki/UA:Character_Traits
    """
    pass


class Skill:
    """Characters have skills, which can affect abilities
    """
    pass


class Ability:
    """Characters have abilities, which are effective when performing actions.
    """
    pass


class Character:
    def __init__(**kwargs):
        self.name = kwargs.get("name", "Jeff")
        
