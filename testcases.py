import unittest
from person import Person
from postboy import Postboy
from post_office import PostOffice
from letter import Letter
from letterbox import Letterbox

post_office = PostOffice()
bob = Person("Bob", "123 Lambini Road", 5)
ophelia = Person("Ophelia", "456 Bughinghi Drive", 5)
charli = Postboy("Charli", post_office)
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
        self.assertEqual(charli.name, "Charli")
        self.assertEqual(charli.address, "Big Boy Post")

    def test_read_letter(self):
        """Tests that the letterbox no longer had letters once they've been read"""
        bob.read_letter()
        self.assertTrue(len(letterbox.letters) == 0)

    def test_write_letter(self):
        """Tests that the letterbox returns ture that it has letters when they're created"""
        if bob.write_letter(ophelia, "test", post_office):
            self.assertTrue(ophelia.letterbox.has_letters() is True)

    def test_write_letter_sender_receiver(self):
        """Tests that the sender and receiver if a letter match"""
        bob.write_letter(ophelia, "g'day", post_office)
        self.assertTrue(bob_letter.sender == bob)
        ophelia.write_letter(bob, "'sup", post_office)
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


class TestPostOffice(unittest.TestCase):

    def test_post_office_has_letters(self):
        """Tests letters are added to the post office letters list when written and removed when taken by the postboy"""
        bob.write_letter(ophelia, "g'day", post_office)
        bob.write_letter(ophelia, "how u do", post_office)
        self.assertTrue(len(post_office.letters) == 2)
        charli.get_letters()
        self.assertTrue(len(post_office.letters) == 0)


class TestPostboy(unittest.TestCase):

    def test_postboy_has_letters(self):
        """Tests the postboy collects the same letters sent to the post office"""
        bob.write_letter(ophelia, "g'day", post_office)
        ophelia.write_letter(bob, "how it do", post_office)
        charli.get_letters()
        self.assertTrue(len(charli.letters) == 2)
        self.assertEqual(charli.letters[1].sender.name, "Bob")
        self.assertEqual(charli.letters[1].receiver.name, "Ophelia")
        self.assertEqual(charli.letters[0].sender.name, "Ophelia")
        self.assertEqual(charli.letters[0].receiver.name, "Bob")


class TestEncryptedLetter(unittest.TestCase):

    def test_encrypted_letter_encrypt_message(self):
        bob.write_encrypted_letter(ophelia, "hello", post_office)
        charli.get_letters()
        self.assertEqual(charli.letters[0]._message, "mjqqt")

    def test_encrypted_letter_decrypt_message(self):
        bob.write_encrypted_letter(ophelia, "g'day", post_office)
        charli.get_letters()
        self.assertEqual(charli.letters[0]._message, "l,if~")
        charli.deliver_letters()
        ophelia.read_letter()
        self.assertEqual(ophelia.letters[0], "g'day")


class TestLetterbox(unittest.TestCase):

    def test_letterbox_attributes(self):
        """Tests default attributes"""
        self.assertEqual(bool(letterbox.letters), 0)

    def test_letterbox_letters(self):
        bob.write_letter(ophelia, "g'day", post_office)
        charli.get_letters()
        charli.deliver_letters()
        self.assertTrue(len(ophelia.letterbox.letters) == 1)


if __name__ == "__main__":
    unittest.main()


