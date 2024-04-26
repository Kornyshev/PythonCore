class FlexibleDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        """
        Allows accessing items using dictionary keys.
        """
        return self.data.get(key, f"No such key: {key}")

    def __setitem__(self, key, value):
        """
        Allows setting items using dictionary keys.
        """
        self.data[key] = value

    def __delitem__(self, key):
        """
        Allows deleting items using dictionary keys if they exist.
        """
        if key in self.data:
            del self.data[key]

    def __len__(self):
        """
        Returns the number of items in the dictionary.
        """
        return len(self.data)

    def __contains__(self, item):
        """
        Checks if the item is a key in the dictionary.
        """
        return item in self.data


# Using the FlexibleDict class
f_dict = FlexibleDict()
f_dict['hello'] = 'world'
print(f_dict['hello'])  # Uses __getitem__, output: 'world'
print(f_dict['nonexistent'])  # Uses __getitem__, output: 'No such key: nonexistent'
print('hello' in f_dict)  # Uses __contains__, output: True
print(len(f_dict))  # Uses __len__, output: 1
del f_dict['hello']  # Uses __delitem__
print('hello' in f_dict)  # Uses __contains__, output: False
