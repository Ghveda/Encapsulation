class Celsius:
    def __init__(self, temperature) -> None:
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature
    def set_temp(self, temperature):
        self.__temperature = temperature
        return self.__temperature
    def del_temp(self):
        del self.__temperature
    
    name = property(get_temp, set_temp, del_temp)

temp = Celsius(10)
temp.name = 20
del temp.name
print(temp.name)

    
