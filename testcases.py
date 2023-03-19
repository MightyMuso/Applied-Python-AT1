import unittest
from person import Person
from letter import Letter
from letterbox import Letterbox

bob = Person("Bob", "123")
ophelia = Person("Ophelia", "456")
letter = Letter(bob, "test", ophelia)
letterbox = Letterbox()


class TestPerson(unittest.TestCase):

    def test_person_attributes(self):
        """Tests default attributes"""
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.address, "123")
        self.assertEqual(ophelia.name, "Ophelia")
        self.assertEqual(ophelia.address, "456")

    def test_read_letter(self):
        """Tests that the letterbox does not have a letter when the letter has been read"""
        bob.read_letter_from_letterbox()
        self.assertTrue(letterbox.has_letter is False)
        self.assertTrue(letterbox.letter is None)

    def test_write_letter(self):
        """Tests that when a letter is created it is no longer a 'None' type"""
        bob.write_letter("g'day", ophelia)
        self.assertTrue(letterbox.letter is not None)

    def test_post_letter(self):
        """Tests that the sender of a letter will be a different 'Person' to the receiver"""
        if bob.post_letter(ophelia) is True:
            self.assertTrue(letter.sender == bob)
            self.assertTrue(letter.receiver == ophelia)
        if ophelia.post_letter(bob) is True:
            self.assertTrue(letter.sender == ophelia)
            self.assertTrue(letter.receiver == bob)


class TestLetter(unittest.TestCase):
    def test_letter_attributes(self):
        """Tests default attributes"""
        self.assertTrue(Letter(bob, "g'day", ophelia).is_read is False)
        self.assertTrue(Letter(ophelia, "g'day", bob).is_read is False)


class TestLetterbox(unittest.TestCase):

    def test_letterbox_attributes(self):
        """Tests default attributes"""
        self.assertTrue(Letterbox().has_letter is False)
        self.assertTrue(Letterbox().letter is None)


if __name__ == "__main__":
    unittest.main()


