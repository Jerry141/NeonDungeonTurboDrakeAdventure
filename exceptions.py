

class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.
    
    Reason of that is given as a message.
    """

class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""