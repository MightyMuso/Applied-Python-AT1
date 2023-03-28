from person import Person

if __name__ == "__main__":
    bob = Person("Bob", "123 Lambini Road")
    ophelia = Person("Ophelia", "456 Bughinghi Drive")

    bob.read_letter_from_letterbox()
    bob.write_letter("g'day")
    bob.write_letter("how u do")
    bob.post_letter(ophelia)
    for letter in ophelia.letterbox.letterbox_letters:
        print(letter)

    ophelia.read_letter_from_letterbox()
    ophelia.write_letter("'sup")
    ophelia.write_letter("am gud thank")
    ophelia.write_letter("what u do")
    ophelia.post_letter(bob)
    for letter in bob.letterbox.letterbox_letters:
        print(letter)
