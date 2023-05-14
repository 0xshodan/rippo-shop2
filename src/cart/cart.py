from decimal import Decimal

from django.conf import settings


class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, spacer, car, type) -> dict:
        spacer_id = str(spacer.pk) + "_" + type

        if spacer_id not in self.cart:
            if type == "20mm":
                price = spacer.price20mm
            elif type == "30mm":
                price = spacer.price30mm
            elif type == "40mm":
                price = spacer.price40mm
            car_name = car.car.car.brand.name + " " + car.car.car.name
            if car.car.name != car.car.car.name:
                car_name += " " + car.car.name
            if car.name != car.car.name:
                car_name += " " + car.name
            data = {
                    "id": spacer_id,
                    "quantity": 0,
                    "price": str(price),
                    "type": type,
                    "article": spacer.article,
                    "photo_url": spacer.photo.url,
                    "car_name": car_name,
                    "car_slug": car.slug,
                }
            self.cart[spacer_id] = data
            self.save()
            return data
        else:
            self.cart[spacer_id]["quantity"] += 1
            self.save()
            return {}

    def increment_quantity(self, spacer_id):
        self.cart[spacer_id]["quantity"] += 1
        self.save()

    def decrement_quantity(self, spacer_id):
        self.cart[spacer_id]["quantity"] -= 1
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, spacer=None, type=None, spacer_id=None):
        """
        Удаление товара из корзины.
        """
        if spacer_id:
            del self.cart[spacer_id]
            self.save()
            return
        spacer_id = str(spacer.id) + "_" + type
        if spacer_id in self.cart:
            del self.cart[spacer_id]
            self.save()

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return len(self.cart)

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        for item in self.cart.values():
            item["price"] = int(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item
