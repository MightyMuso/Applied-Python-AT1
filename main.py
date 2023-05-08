from person import Person
from postboy import Postboy
from post_office import PostOffice
from time import ctime

if __name__ == "__main__":
    bob = Person("Bob", "123 Lambini Road", 5)
    ophelia = Person("Ophelia", "456 Bughinghi Drive", 5)
    post_office = PostOffice()
    charli = Postboy("Charli", post_office)

    bob.read_letter()
    bob.write_encrypted_letter(ophelia, "Hello", post_office)
    bob.write_letter(ophelia, "hello all", post_office)

    charli.get_letters()
    for letter in charli.letters:
        print(f">>> {letter}")
    charli.deliver_letters()

    ophelia.read_letter()
    for letter in ophelia.letters:
        print(letter)

