from person import Person
from postboy import Postboy
from post_office import PostOffice
from time import ctime

if __name__ == "__main__":
    bob = Person("Bob", "123 Lambini Road", 5)
    ophelia = Person("Ophelia", "456 Bughinghi Drive", 5)
    post_office = PostOffice()
    charli = Postboy("Charli", post_office)

    for letter in bob.letterbox.letters:
        print(f"\n>>> {letter}")
    bob.read_letter()
    print(f"\nLetters read by Bob at {ctime()}")

    bob.write_letter(ophelia, "g'day", post_office)
    bob.write_letter(ophelia, "how u do", post_office)
    print(f"\nLetters sent by Bob at {ctime()}")

    charli.get_letters()
    for letter in charli.letters:
        print(f"\n> {letter}")
    charli.deliver_letters()
    print(f"\nLetters delivered at {ctime()}")

    for letter in ophelia.letterbox.letters:
        print(f"\n>>> {letter}")
    ophelia.read_letter()
    print(f"\nLetters read by Ophelia at {ctime()}")
    ophelia.write_letter(bob, "'sup", post_office)
    ophelia.write_letter(bob, "am gud thank", post_office)
    ophelia.write_letter(bob, "what u do", post_office)
    print(f"\nLetters sent by Ophelia at {ctime()}")

    charli.get_letters()
    for letter in charli.letters:
        print(f"\n> {letter}")
    charli.deliver_letters()
    print(f"\nLetters delivered at {ctime()}\n")

