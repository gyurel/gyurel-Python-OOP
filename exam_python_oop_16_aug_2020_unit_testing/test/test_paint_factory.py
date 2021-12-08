from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.expected_name = 'PaintFactory'
        self.expected_capacity = 50
        self.expected_valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        self.expected_ingredients = {}
        self.expected_products = {}
        self.paint_factory = PaintFactory(self.expected_name, self.expected_capacity)

    def test_paint_factory_initialization(self):
        # expected_name = 'PaintFactory'
        # expected_capacity = 50
        # expected_valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        # expected_ingredients = {}
        # expected_products = {}
        self.assertEqual(self.expected_name, self.paint_factory.name)
        self.assertEqual(self.expected_capacity, self.paint_factory.capacity)
        self.assertEqual(self.expected_valid_ingredients, self.paint_factory.valid_ingredients)
        self.assertEqual(self.expected_ingredients, self.paint_factory.ingredients)
        self.assertEqual(self.expected_products, self.paint_factory.products)

    def test_add_ingredient_raises_type_error_if_ingredient_not_in_valid_ingredients(self):
        product_type = self.expected_valid_ingredients[0] + self.expected_valid_ingredients[1]
        product_quantity = self.expected_capacity /10
        expected = f"Ingredient of type {product_type} not allowed in {self.paint_factory.__class__.__name__}"

        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertEqual(expected, str(context.exception))

    def test_if_add_ingredient_adds_a_valid_ingredient_when_capacity_sufficient_and_ingredient_not_in_ingredients(self):
        product_type = self.expected_valid_ingredients[0]
        product_quantity = self.expected_capacity / 10
        expected = self.expected_capacity / 10

        self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertEqual(expected, self.paint_factory.ingredients[product_type])

    def test_if_add_ingredient_adds_a_valid_ingredient_when_capacity_sufficient_and_ingredient_in_ingredients(self):
        product_type = self.expected_valid_ingredients[0]
        product_quantity = self.expected_capacity / 10
        expected = (self.expected_capacity / 10) * 2

        self.paint_factory.add_ingredient(product_type, product_quantity)
        self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertEqual(expected, self.paint_factory.ingredients[product_type])

    def test_if_add_ingredient_raises_value_error_when_capacity_not_sufficient_and_ingredient_in_ingredients(self):
        product_type = self.expected_valid_ingredients[0]
        product_quantity = self.expected_capacity
        expected = "Not enough space in factory"

        self.paint_factory.add_ingredient(product_type, product_quantity)

        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient(product_type, product_quantity)

        self.assertEqual(expected, str(context.exception))

    def test_remove_ingredient_raises_key_error_if_ingredient_not_in_ingredients(self):
        product_type = self.expected_valid_ingredients[0] + self.expected_valid_ingredients[1]
        product_quantity = self.expected_capacity / 10
        expected = "'No such ingredient in the factory'"

        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient(product_type, product_quantity)

        self.assertEqual(expected, str(context.exception))

    def test_remove_ingredient_raises_value_error_if_quantity_not_enough(self):
        product_type = self.expected_valid_ingredients[0]
        product_quantity = self.expected_capacity / 10
        expected = "Ingredients quantity cannot be less than zero"

        self.paint_factory.add_ingredient(product_type, product_quantity)

        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient(product_type, product_quantity * 2)

        self.assertEqual(expected, str(context.exception))

    def test_remove_ingredient_removes_if_ingredient_in_ingredients_and_quantity_enough(self):
        product_type = self.expected_valid_ingredients[0]
        product_quantity = self.expected_capacity / 10
        expected = 0  # self.paint_factory.ingredients[product_type] = 0

        self.paint_factory.add_ingredient(product_type, product_quantity)
        self.paint_factory.remove_ingredient(product_type, product_quantity)

        self.assertEqual(expected, self.paint_factory.products[product_type])

    def test__repr__if_returns_proper_string(self):
        expected_name = 'PaintFactory'
        expected_capacity = 50
        expected_valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        product_type1 = expected_valid_ingredients[0]
        product_type2 = expected_valid_ingredients[1]
        product_quantity = expected_capacity / 10
        expected_string = f"Factory name: {expected_name} with capacity {expected_capacity}.\n" \
                          f"{expected_valid_ingredients[0]}: {product_quantity}\n" \
                          f"{expected_valid_ingredients[1]}: {product_quantity}\n"

        self.paint_factory.add_ingredient(product_type1, product_quantity)
        self.paint_factory.add_ingredient(product_type2, product_quantity)

        self.assertEqual(expected_string, repr(self.paint_factory))


if __name__ == '__main__':
    main()
