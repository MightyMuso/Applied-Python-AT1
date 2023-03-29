import unittest
from person import Person
from letter import Letter
from letterbox import Letterbox

bob = Person("Bob", "123 Lambini Road")
ophelia = Person("Ophelia", "456 Bughinghi Drive")
bob_letter = Letter(bob, ophelia, "test")
ophelia_letter = Letter(ophelia, bob, "test")
letterbox = Letterbox()


class TestPerson(unittest.TestCase):

    def test_person_attributes(self):
        """Tests default attributes"""
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.address, "123 Lambini Road")
        self.assertEqual(ophelia.name, "Ophelia")
        self.assertEqual(ophelia.address, "456 Bughinghi Drive")

    def test_read_letter(self):
        """Tests that the letterbox no longer had letters once they've been read"""
        bob.read_letter()
        self.assertTrue(len(letterbox.letters) == 0)

    def test_write_letter(self):
        """Tests that the letterbox returns ture that it has letters when they're created"""
        if bob.write_letter(ophelia, "test"):
            self.assertTrue(ophelia.letterbox.has_letters() is True)

    def test_write_letter_sender_receiver(self):
        """Tests that the sender and receiver if a letter match"""
        bob.write_letter(ophelia, "g'day")
        self.assertTrue(bob_letter.sender == bob)
        ophelia.write_letter(bob, "'sup")
        self.assertTrue(ophelia_letter.sender == ophelia)

        if bob_letter.sender == bob and bob_letter.receiver == bob:
            self.assertRaises(Exception)
        if ophelia_letter.sender == ophelia and ophelia_letter.receiver == ophelia:
            self.assertRaises(Exception)


class TestLetter(unittest.TestCase):
    def test_letter_attributes(self):
        """Tests default attributes"""
        self.assertTrue(bob_letter.is_read() is False)
        self.assertTrue(ophelia_letter.is_read() is False)

    def text_letter_read_letter(self):
        if bob.read_letter():
            self.assertTrue(bob_letter.is_read() is True)
        else:
            self.assertFalse((bob_letter.is_read() is False))


class TestLetterbox(unittest.TestCase):

    def test_letterbox_attributes(self):
        """Tests default attributes"""
        self.assertEqual(len(letterbox.letters), 0)

    def test_letterbox_letters(self):
        bob.write_letter(ophelia, "g'day")
        bob.write_letter(ophelia, "how u do")
        self.assertTrue(len(ophelia.letterbox.letters) == 2)
        ophelia.write_letter(bob, "'sup")
        self.assertTrue(len(bob.letterbox.letters) == 1)


if __name__ == "__main__":
    unittest.main()


