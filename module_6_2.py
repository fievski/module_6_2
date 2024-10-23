class Vehicle:
    __COLOR_VARIANTS = ['red', 'purple', 'orange', 'yellow', 'black']

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self, __model):
        return f'Модель: {self.__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self, __color):
        return f'Цвет авто: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        return f'Владелец авто: {self.owner}'

    def set_color(self):
        new_color = new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5
    pass

# Текущие цвета __COLOR_VARIANTS = ['red', 'purple', 'orange', 'yellow', 'black']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'red', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()