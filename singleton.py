# class SingletonMeta(type):
#     """
#     A metaclass for Singleton that ensures only one instance of the class is created
#     By the compare between instances if they similar so class create.. two instances
#     """
#     _instances = {}  # Dictionary to hold the single instances of the classes.
#
#     def __call__(cls, *args, **kwargs):
#         # If the class does not have an instance yet, create one.
#         if cls not in cls._instances:
#             # Call the superclass __call__ method to create the instance.
#             instance = super().__call__(*args, **kwargs)
#             # Store the instance in the _instances dictionary.
#             cls._instances[cls] = instance
#         # Return the existing instance.
#         return cls._instances[cls]
#
# class Singleton(metaclass=SingletonMeta):
#     """
#     Example Singleton class. Any attempt to instantiate this class will return
#     the same instance.
#     """
#     def __init__(self):
#         # Initialize an instance attribute.
#         self.value = None
#
# # Example usage of the Singleton class.
# if __name__ == "__main__":
#     # Create the first instance of Singleton.
#     s1 = Singleton()
#     # Create the second instance of Singleton.
#     s2 = Singleton()
#
#     # Set a value to the attribute of the first instance.
#     s1.value = "Singleton Instance"
#
#     # Both instances should have the same value because they are the same instance.
#     print(s1.value)  # Output: Singleton Instance
#     print(s2.value)  # Output: Singleton Instance
#
#     # Check if both variables point to the same instance.
#     print(s1 is s2)  # Output: True

import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")
