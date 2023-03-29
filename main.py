from person import Person

if __name__ == "__main__":
    bob = Person("Bob", "123 Lambini Road")
    ophelia = Person("Ophelia", "456 Bughinghi Drive")

    bob.read_letter()

    # bob.write_letter(bob, "test")

    bob.write_letter(ophelia, "g'day")
    bob.write_letter(ophelia, "how u do")
    for letter in ophelia.letterbox.letters:
        print(letter)

    ophelia.read_letter()
    ophelia.write_letter(bob, "'sup")
    ophelia.write_letter(bob, "am gud thank")
    ophelia.write_letter(bob, "what u do")
    for letter in bob.letterbox.letters:
        print(letter)
