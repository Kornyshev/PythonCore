class SingletonNew:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Testing the Singleton implementation with __new__
# singleton_a = SingletonNew()
# singleton_b = SingletonNew()
#
# print("Singleton with __new__:")
# print(singleton_a is singleton_b)  # Should print True


def singleton_decorator(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton_decorator
class SingletonDecorator:
    pass


# Testing the Singleton implementation with a decorator
# singleton_c = SingletonDecorator()
# singleton_d = SingletonDecorator()
#
# print("Singleton with Decorator:")
# print(singleton_c is singleton_d)  # Should print True


def main():
    # Testing Singleton with __new__ method
    singleton_a = SingletonNew()
    singleton_b = SingletonNew()
    print("Singleton with __new__:")
    print(singleton_a is singleton_b)  # Output: True

    # Testing Singleton with a decorator
    singleton_c = SingletonDecorator()
    singleton_d = SingletonDecorator()
    print("Singleton with Decorator:")
    print(singleton_c is singleton_d)  # Output: True


if __name__ == "__main__":
    main()
