class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"manager: {self._class}"
    
    def search(self, **kwargs): 
        """
        :prim kwargs: a=1, c=2, name='John'
        :return: list of objects: [a=1 , c=2, name='John']
        """
        # TODO: check range in search, for  exaple: (area__min=12, area__max=13)
        results = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'
            for obj in self._class.objects_list:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = bool(getattr(obj, key) >= value)
                    elif compare_key == 'max':
                        result = bool(getattr(obj, key) <= value)
                    else:
                        result = bool(getattr(obj, key) == value) 
                    if result:
                        results.append(obj)
        return results
    
    def get(self, **kwargs):
        """
        :prim kwargs: a=1, c=2, name='John'
        :return: single object
        """ 
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value: # Check if the object has an attribute with the given key, and its value matches the expected value
                    return obj
        return None

    def count(self):
        return len(self._class.objects_list)

