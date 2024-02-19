class BaseClass:
    def __init_subclass__(cls, my_name):
        print(f"Subclass created and my name is {my_name}")
        # super().__init_subclass__() Needed only in case of
        # multiple inheritance


MyDynamicSubClass = type("MyDynamicSubClass", (BaseClass,), {}, my_name="John")
