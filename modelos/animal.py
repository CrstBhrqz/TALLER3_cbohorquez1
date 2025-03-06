from abc import ABC, abstractmethod


# Interfaz IAnimal
class IAnimal(ABC):
    
    # Defini las funciones abstractas que deben de cumplir las subclases los Hijos
    @abstractmethod
    def hacer_ruido(self):
        pass


# Clase Animal
class Animal(IAnimal):


    
    # constructor de la clase
    def __init__(self, name:str,  weight:float,age:int):
        
        # Atributos protegidos
        self._name = name
        self._weight = weight
        self._age = age
        
        # print("Constructor de la clase Animal")
        # print(self.__dict__)
        

    def hacer_ruido(self):
        pass
    
    
    # Getter y Setter para _name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip() != "":
            self._name = value.strip()
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    # Getter y Setter para _weight
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._weight = value
        else:
            raise ValueError("El peso debe ser un número positivo.")

    # Getter y Setter para _age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("La edad debe ser un entero no negativo.")
