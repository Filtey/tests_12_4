import logging
import runner
import unittest
import runner_and_tournament as runner2


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding="UTF-8", format="%(levelname)s => %(message)s" )

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.runner = runner2.Runner(name="Ivan", speed=-2)
        try:
            for i in range (10):
                self.runner.walk()
            self.assertEqual(self.runner.distance, 50)
            logging.info(f"test_walk выполнен успешно!")
        except :
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            self.runner = runner.Runner("Name", "OTHER")
            for i in range (10):
                self.runner.run()
            self.assertEqual(self.runner.distance, 100)
            logging.info(f"test_run выполнен успешно!")

        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")



    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.runner = runner.Runner("Runner1")
        self.runner2 = runner.Runner("Runner2")
        for i in range (10):
            self.runner.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner.distance, self.runner2.distance)





class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner2.Runner("Усэйн", 10)
        self.runner2 = runner2.Runner("Андрей", 9)
        self.runner3 = runner2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key} : {value}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg1(self):
        tournament = runner2.Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усейн")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg2(self):
        tournament = runner2.Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Андрей")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_zabeg3(self):
        tournament = runner2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усэйн")

if __name__ == "__main__":
    unittest.main()
