import unittest
from unittest.mock import patch
import main

class TestRockPaperScissors(unittest.TestCase):

    def setUp(self):
        with patch('main.tk.Label') as MockLabel:
            self.mock_result_label = MockLabel.return_value
            self.mock_score_label = MockLabel.return_value
            main.result_label = self.mock_result_label
            main.score_label = self.mock_score_label

    @patch('main.random.choice', return_value='rock')
    def test_user_wins(self, mock_random):
        with patch('main.result_label.config') as mock_result:
            main.play_game('paper')
            mock_result.assert_any_call(text='Computer chose: rock\nYou win!')
            self.mock_score_label.config.assert_any_call(text='Score - You: 1 | Computer: 0')

    @patch('main.random.choice', return_value='scissors')
    def test_user_loses(self, mock_random):
        with patch('main.result_label.config') as mock_result:
            main.play_game('paper')
            mock_result.assert_called_with(text='Computer chose: scissors\nYou lose!')

    @patch('main.random.choice', return_value='paper')
    def test_tie(self, mock_random):
        with patch('main.result_label.config') as mock_result:
            main.play_game('paper')
            mock_result.assert_called_with(text='Computer chose: paper\nIt\'s a tie!')

class TestGameLogic(unittest.TestCase):

    def test_get_game_result_tie(self):
        result = main.get_game_result('rock', 'rock')
        self.assertEqual(result, "It's a tie!")

    def test_get_game_result_user_wins(self):
        result = main.get_game_result('rock', 'scissors')
        self.assertEqual(result, "You win!")

    def test_get_game_result_user_loses(self):
        result = main.get_game_result('rock', 'paper')
        self.assertEqual(result, "You lose!")

class TestProcessGame(unittest.TestCase):

    def setUp(self):
        main.user_score = 0
        main.computer_score = 0

    @patch('main.random.choice', return_value='rock')
    def test_process_game_user_wins(self, mock_random):
        computer_choice, result, user_score, computer_score = main.process_game('paper')
        self.assertEqual(computer_choice, 'rock')
        self.assertEqual(result, 'You win!')
        self.assertEqual(user_score, 1)
        self.assertEqual(computer_score, 0)

    @patch('main.random.choice', return_value='scissors')
    def test_process_game_user_loses(self, mock_random):
        computer_choice, result, user_score, computer_score = main.process_game('paper')
        self.assertEqual(computer_choice, 'scissors')
        self.assertEqual(result, 'You lose!')
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 1)

    @patch('main.random.choice', return_value='paper')
    def test_process_game_tie(self, mock_random):
        computer_choice, result, user_score, computer_score = main.process_game('paper')
        self.assertEqual(computer_choice, 'paper')
        self.assertEqual(result, "It's a tie!")
        self.assertEqual(user_score, 0)
        self.assertEqual(computer_score, 0)

if __name__ == '__main__':
    unittest.main()