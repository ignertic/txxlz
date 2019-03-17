



class Txxlz(object):
    """Documentation Will be released on 9 April 2019."""
    def __init__(self, setting):
        super(Txxlz, self).__init__()
        self.setting = setting or {}

    def prepare_json(self, json_body : str):
        """replaces characters that trigger TypeErrors"""
        return json_body.replace("null", "None").replace("true", "True").replace("false", "False")
        
