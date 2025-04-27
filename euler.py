def euler_method(f, x0, y0, h, x_point):
    """
    Էյլերի մեթոդը Կոշիի խնդրի լուծման համար:
    
    :param f: ֆունկցիա, որը ներկայացնում է y' = f(x, y)
    :param x0: սկզբնական x արժեքը
    :param y0: սկզբնական y արժեքը (y(x0) = y0)
    :param h: քայլի չափը
    :param x_point: x արժեքը, որի համար պետք է հաշվարկել y(x)
    :return: y(x_target) մոտավոր արժեքը
    """
    x = x0
    y = y0
    
    while x < x_point:
        # Եթե հաջորդ քայլը գերազանցում է x_target-ը, ապա կրճատում ենք քայլը
        if x + h > x_point:
            h = x_point - x
        y += h * f(x, y)
        x += h
        print(y)
    
    return y


if __name__ == "__main__":
    # Օրինակ բերենք տնայինի խնդիրը՝ y' = -y, y(0) = 1
    def f(x, y):
        return -y
    
    x0 = 0
    y0 = 1
    h = 0.1
    x_point = 1
    
    result = euler_method(f, x0, y0, h, x_point)
    print(f"y({x_point}) ≈ {result}")