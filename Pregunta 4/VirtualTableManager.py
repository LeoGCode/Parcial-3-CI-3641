# model and implement a virtual method table handler for an object-oriented system with simple inheritance and dynamic method dispatching:
# (a) You must know how to deal with class definitions, potentially with simple inheritance. These definitions will have only the names of the methods you will own.

# (b) Once the program is started, it will repeatedly prompt the user for an action to proceed. Such an action may be:

# i. CLASS <type> [<name>].
# Defines a new type that will possess methods with names set from the list provided. The <type> may be:
# - A name, which establishes a type that does not inherit from any other.
# - An expression of the form <name> : <super>, which establishes the name of the type and the fact that this type inherits from no other type. type and the fact that this type inherits from the type with name <super>.
# For example: CLASS A f g and CLASS B : A f h
# Note that it is possible to replace definitions of a super class in classes that inherit it. inherit it.
# The program must report an error and ignore the action if the name of the new class already exists, if the super class already exists. class already exists, if the super class does not exist, if there are repeated definitions in the list of method names, or if the super class is of method names or if a loop is generated in the inheritance hierarchy.
# ii. DESCRIBE <name>.
# Must display the virtual method table for the type with the proposed name.
# For example: DESCRIBE B
# This should show:
# f -> B :: f
# g -> A :: g
# h -> B :: h
# The program should report an error and ignore the action if the type name does not exist. exists.
# iii. EXIT
# You must exit the simulator.
# At the end of the execution of each action, the program should request the next action from the user. to the user.

from typing import List, Dict, Tuple

from matplotlib.pyplot import cla

class VirtualTableManager():
    
    def __init__(self):
        self.classes: Dict[str, List[Tuple[str, str]]] = {} # Example {'Base': [('f','Base'),('g','Base')]}

    def begin_program(self):
        print("Welcome to the Virtual Table Manager")

        while True:
            action = input("Enter an action: ")
            param = action.split()
            act = param.pop(0).lower()
            if act == "class" or act == "1":
                self.create_class(param)
            elif act == "describe" or act == "describir" or act == "2":
                self.describe_class(param)
            elif act == "exit" or act == "salir" or act == "3":
                print("Thank you for using the Virtual Table Manager")
                break
            else:
                print("Invalid action")

    def create_class(self, param: List[str]) -> None:
        if len(param) < 1:
            print("Invalid number of parameters")
            return
        class_name = param.pop(0)
        if class_name in self.classes.keys():
            print("Class already exists")
            return
        if param[0] == ":":
            if len(param) - 2 != len(set(param[2:])):
                print("Repeated method names")
                return
            super_name = param[1]
            if super_name not in self.classes.keys():
                print("Super class does not exist")
                return
            tmp = self.inherited_methods(class_name, param[2:], self.classes[super_name])
            if tmp == []:
                return
            self.classes[class_name] = tmp
        else:
            if len(param) != len(set(param)):
                print("Repeated method names")
                return
            self.classes[class_name] = [(class_name, method) for method in param]
        print("Class created")

    def inherited_methods(self, class_name: str, class_methods: List[str], super_methods: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        methods = super_methods.copy()
        new_methods = []
        modified: bool = False
        for method in class_methods:
            for i in range(len(methods)):
                if class_name == super_methods[i][0]:
                    print("Loop in inheritance hierarchy")
                    return []
                if method == super_methods[i][1]:
                    modified = True
                    methods[i] = (class_name, method)
                    break
            if not modified:
                new_methods.append((class_name, method))
            modified = False

        methods.extend(new_methods)
        return methods


    def describe_class(self, param: List[str]) -> None:
        if len(param) != 1:
            print("Invalid number of parameters")
            return
        name = param[0]
        if name not in self.classes.keys():
            print("Class does not exist")
            return
        print("Virtual table of methods for class " + name)
        for method in self.classes[name]:
            print(method[1] + " -> " + method[0] + " :: " + method[1])
        print("")