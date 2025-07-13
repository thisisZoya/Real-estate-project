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
        result = list()
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value: # Check if the object has an attribute with the given key, and its value matches the expected value
                    result.append(obj)
        return result
    
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

