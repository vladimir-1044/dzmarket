class Market:
    # задаем цену для продуктов
    __MILK = 20
    __CANDIES = 40
    __ICE_CREAM = 30
    __BREAD = 10
    __WHISKEY = 80
    __DISH = 100
    # задаем возможные наименования атрибутов класса
    __slots__ = ['__price_list', '__my_basket']

    # задаем атрибуты экземпляров класса
    def __init__(self):
        # в данном словаре представлен ассортимент, состоящий из названия продукта, его цены, количестве на складе и порядкового номера
        self.__price_list = {
            'молоко': [Market.__MILK, 10, 1],
            'конфеты': [Market.__CANDIES, 20, 2],
            'мороженное': [Market.__ICE_CREAM, 30, 3],
            'хлеб': [Market.__BREAD, 30, 4],
            'виски': [Market.__WHISKEY, 5, 5],
            'закуска': [Market.__DISH, 10, 6]
        }
        # данный словарь пользовательский - в нем хранится инфоромация о выбранных продуктах
        self.__my_basket = {}

    #  статический метод проверяет корректность введенного значения относительно выбора номера продукта и его количества
    @staticmethod
    def verify_value(str):  # в параметр передается текст, указывающий что нужно ввести
        try:
            return int(input(str))
        except:
            print("Значение не корректно!")
            return -1

    # метод класса предоставляет возможность изменить цену продуктов
    @classmethod
    def change_price(cls, milk, candies, ice_cream, bread, whiskey, dish):
        cls.__MILK = milk
        cls.__CANDIES = candies
        cls.__ICE_CREAM = ice_cream
        cls.__BREAD = bread
        cls.__WHISKEY = whiskey
        cls.__DISH = dish
        print("Цена изменена")
        print()

    # метод показывает ассортимент магазина
    def show_price(self):
        print("Добро пожаловать в магазин! Мы готовы предложить Вам:")
        for i in self.__price_list:
            j = self.__price_list[i][2]
            print(f"{j}. {i} (в наличии {self.__price_list[i][1]} шт.) - {self.__price_list[i][0]} руб.")
        print()

    # метод добавляет продукт в корзину
    def choice(self):
        price = 0
        while True:
            x = Market.verify_value("Введите номер товара (для выхода 0): ")
            while x > len(self.__price_list):
                x = Market.verify_value("Значение не корректно. Введите номер товара (для выхода 0): ")
            if x == 0: break
            if x == -1: continue
            for i in self.__price_list:
                if self.__price_list[i][2] == x:
                    self.__my_basket[i] = self.__price_list[i][1]
                    y = Market.verify_value("Сколько штук вы хотите купить?: ")
                    while y == -1 or y > self.__price_list[i][1]:
                        y = Market.verify_value(
                            "Не верен тип значения или указанное количество больше имеющегося. Введите корректное значение: ")
                    self.__my_basket[i] = y
                    price += self.__price_list[i][0] * y
                    print(f"Ваша корзина: {self.__my_basket} общей стоимостью {price} руб.")
        print(f"Итог покупок: {self.__my_basket} общей стоимостью {price} руб.")
        if len(self.__my_basket) > 0:
            print("Спасибо за покупки! Приходите к нам еще.")
        else:
            print("Покупок 0")
        print()


# создание экземпляров класса и запуск работы методов
a = Market()
a.show_price()
a.choice()

Market.change_price(1000, 20, 40, 2000, 4000, 10000)

b = Market()
b.show_price()
b.choice()


