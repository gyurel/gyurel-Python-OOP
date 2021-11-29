import unittest
from hero.project.hero import Hero


class TestingHero(unittest.TestCase):

    def test_hero_initialization(self):
        hero = Hero('Hero', 10, 155.5, 7.5)

        self.assertEqual('Hero', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(155.5, hero.health)
        self.assertEqual(7.5, hero.damage)

    def test__str__if_returns_proper_string(self):
        hero = Hero('Hero', 10, 155.5, 7.5)

        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
               f"Health: {hero.health}\n" \
               f"Damage: {hero.damage}\n"

        actual = str(hero)

        self.assertEqual(expected, actual)

    def test_if_battle_raises_error_when_the_enemy_hero_name_is_the_same_like_heroname(self):
        hero = Hero('Hero', 10, 155.5, 7.5)
        enemy_hero = Hero(hero.username, 12, 200, 30)

        with self.assertRaises(Exception) as context:
            hero.battle(enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_if__battle_returns_proper_string_when_hero_health_is_equal_or_less_than_zero(self):
        for health in [0, -10]:
            hero = Hero('Hero', 10, health, 7.5)
            enemy_hero = Hero('Enemy_hero', 12, 200, 30)

            with self.assertRaises(Exception) as context:
                hero.battle(enemy_hero)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_if_battle_returns_proper_string_when_enemy_hero_health_is_equal_or_less_than_zero(self):
        for health in [0, -10]:
            hero = Hero('Hero', 10, 155.5, 7.5)
            enemy_hero = Hero('Enemy_hero', 12, health, 30)

            with self.assertRaises(Exception) as context:
                hero.battle(enemy_hero)

            self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_bouth_enemy_hero_health_and_hero_health_fall_to_or_below_zero_after_atack(self):
        for health in [30, 20]:
            hero = Hero('Hero', 10, health, 30)
            enemy_hero = Hero('Enemy_hero', 12, health, 30)

            self.assertEqual("Draw", hero.battle(enemy_hero))

    def test_enemy_hero_health_falls_to_or_below_zero_after_atack(self):
        for health in [30, 20]:
            hero = Hero('Hero', 1, 200, 30)

            current_level = hero.level
            current_health = hero.health
            current_damage = hero.damage

            enemy_hero = Hero('Enemy_hero', 1, health, 30)

            self.assertEqual("You win", hero.battle(enemy_hero))
            self.assertEqual(current_level + 1, hero.level)
            self.assertEqual(current_health - enemy_hero.damage + 5, hero.health)
            self.assertEqual(current_damage + 5, hero.damage)

    def test_hero_health_falls_to_or_below_zero_after_atack(self):
        for health in [30, 20]:
            enemy_hero = Hero('Hero', 1, 200, 30)

            current_level = enemy_hero.level
            current_health = enemy_hero.health
            current_damage = enemy_hero.damage

            hero = Hero('Enemy_hero', 1, health, 30)

            self.assertEqual("You lose", hero.battle(enemy_hero))
            self.assertEqual(current_level + 1, enemy_hero.level)
            self.assertEqual(current_health - hero.damage + 5, enemy_hero.health)
            self.assertEqual(current_damage + 5, enemy_hero.damage)


if __name__ == '__main__':
    unittest.main()
