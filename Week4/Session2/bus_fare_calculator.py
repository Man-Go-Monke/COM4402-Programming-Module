def get_fare(age: int, is_peak: bool) -> float:


        price = 2.50
        if not type(is_peak) is bool:
            raise TypeError
        if not type(age) is int:
            raise TypeError

        if age < 0:
            raise ValueError

        if age < 16:
            price = price * 0.5
        elif age >= 16 and age < 65:
            price = 2.50
        else:
            price = 1.00
        if is_peak == False:
            price = price * 0.8





        return float(price)

