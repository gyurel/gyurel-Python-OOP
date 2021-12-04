from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.petshop = PetShop('Pias Pet Shop')

    def test_initialization(self):
        expected_name = 'Pias Pet Shop'
        expected_foods = {}
        expected_pets = []

        self.assertEqual(expected_name, self.petshop.name)
        self.assertEqual(expected_foods, self.petshop.food)
        self.assertEqual(expected_pets, self.petshop.pets)

    def test_add_food_when_quantity_less_or_equal_to_zero_raises_exeption(self):
        food_name = 'Food name'

        for qty in [0, -15]:
            with self.assertRaises(ValueError) as context:
                self.petshop.add_food(food_name, qty)

            self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_when_name_not_in_food_adds_the_food_and_the_quantity_and_returns_the_proper_string(self):
        food_name = 'Food name'
        food_quantity = 15.0
        expected_result = f"Successfully added {food_quantity:.2f} grams of {food_name}."

        self.assertEqual(expected_result, self.petshop.add_food(food_name, food_quantity))

    def test_add_food_when_name_in_food_adds_the_food_and_the_quantity_and_returns_the_proper_string(self):
        food_name = 'new food'
        food_quantity1 = 15.0
        food_quantity2 = 25.0
        expected_string1 = f"Successfully added {food_quantity1:.2f} grams of {food_name}."
        expected_string2 = f"Successfully added {food_quantity2:.2f} grams of {food_name}."
        expected_final_quantity = food_quantity1 + food_quantity2

        stringt_after_food1 = self.petshop.add_food(food_name, food_quantity1)
        self.assertEqual(expected_string1, stringt_after_food1)

        stringt_after_food2 = self.petshop.add_food(food_name, food_quantity2)
        self.assertEqual(expected_string2, stringt_after_food2)

        self.assertEqual(expected_final_quantity, self.petshop.food[food_name])

    def test_add_pet_when_name_not_in_pets(self):
        pet_name = 'Sharo'
        expected = f"Successfully added {pet_name}."

        self.assertEqual(expected, self.petshop.add_pet(pet_name))

    def test_if_add_pet_raises_exeption_if_pet_name_already_in_pets(self):
        pet_name = 'Sharo'

        self.petshop.add_pet(pet_name)

        with self.assertRaises(Exception) as context:
            self.petshop.add_pet(pet_name)

        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_if_pet_name_not_in_pets(self):
        pet_name = 'Sharo'
        food_name = 'Kokal'

        with self.assertRaises(Exception) as context:
            self.petshop.feed_pet(food_name, pet_name)

        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_pet_if_food_name_not_in_food(self):
        pet_name = 'Sharo'
        food_name = 'Kokal'
        expected = f'You do not have {food_name}'

        self.petshop.add_pet(pet_name)

        self.assertEqual(expected, self.petshop.feed_pet(food_name, pet_name))

    def test_feed_pet_if_food_quantity_less_than_100_units_adds_1000_units_and_returns_proper_string(self):
        pet_name = 'Sharo'
        food_name = 'Kokal'
        food_quantity = 50
        expected_quantity = 1000 + food_quantity

        self.petshop.add_pet(pet_name)
        self.petshop.add_food(food_name, food_quantity)

        self.assertEqual("Adding food...", self.petshop.feed_pet(food_name, pet_name))
        self.assertEqual(expected_quantity, self.petshop.food[food_name])

    def test_feed_pet_if_pet_in_pets_food_in_food_quantity_more_than_100(self):
        pet_name = 'Sharo'
        food_name = 'Kokal'
        food_quantity = 150
        expected_quantity = food_quantity - 100

        self.petshop.add_pet(pet_name)
        self.petshop.add_food(food_name, food_quantity)

        self.assertEqual(f"{pet_name} was successfully fed", self.petshop.feed_pet(food_name, pet_name))
        self.assertEqual(expected_quantity, self.petshop.food[food_name])

    def test_if__repr__method_returns_proper_string(self):
        self.petshop.add_pet('Sharo')
        self.petshop.add_pet('Roshko')
        self.petshop.add_pet('Gosho')
        self.petshop.add_pet('Pesho')
        self.petshop.add_pet('Taro')
        self.petshop.add_pet('Dodo')

        expected = f'Shop {self.petshop.name}:\n' \
               f'Pets: {", ".join(self.petshop.pets)}'

        self.assertEqual(expected, self.petshop.__repr__())


if __name__ == '__main__':
    main()
