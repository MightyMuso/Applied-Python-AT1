``` mermaid
classDiagram
    class Person {
        + string name
        + string address
        + bool letterbox
        + post_letter()
        + read_letter()
        + write_letter()
    }
    class Letter {
        - string text
        - bool is_read
        - read()
    }
    class Letterbox {
        + bool has_letter
        + new_letter()
        + get_letter()     
    }
    Person *-- Letterbox
    Person --> Letter: Writes
    Letter o-- Letterbox
    Letterbox 
```

``` mermaid
sequenceDiagram
    actor Bob
    participant LetterB
    participant Letterbox
    participant LetterA
    actor Alice
    
    Bob ->> Letterbox: Checks for letter
    alt has letter
        Letterbox --> Bob: Get letter
        Bob ->> LetterB: Writes letter
        activate LetterB
        LetterB --> Bob: Return letter
        deactivate LetterB
        Bob ->> Letterbox: Posts letter
    end
    Alice ->> Letterbox: Checks for letter
    alt has letter
        Alice --> Letterbox: Gets letter
        Alice ->> LetterA: Reads letter
        Alice ->> LetterA: Writes letter
        activate LetterA
        LetterA --> Alice: Return Letter
        deactivate LetterA
        Alice ->> Letterbox: Posts letter
    end
```

``` mermaid
flowchart
    id1((Bob))
    id2((Alice))
    id3((Bob's Letterbox))
    id4((Alice's Letterbox))
    id5((Bob's Letter))
    id6((Alice's Letter))
    id1 -- 1.1: Check for letter --> id3
    id1 -- 2.1: Write letter --> id5
    id5 -- 3.1: Post letter --> id4
    id4 -- 4.1: Update status --> id2
    id2 -- 1.2: Check for letter --> id4
    id2 -- 2.2: Write letter --> id6
    id6 -- 3.2: Post letter --> id3
    id3 -- 4.2: Update status --> id1

    
    
```

``` mermaid
stateDiagram
state if_state_hasletter <<choice>>
state if_state_lettertaken <<choice>>
[*] --> HasLetter
HasLetter --> if_state_hasletter
if_state_hasletter --> True: if post_letter()
if_state_hasletter --> False: else
True --> if_state_lettertaken
if_state_lettertaken --> False : if get_letter()  
```

``` mermaid
flowchart
    Start([Start])
    Start --> CheckMail
    CheckMail --> if_mail{If mail exists}
    if_mail -- True --> GetMail
    if_mail -- False --> AwaitMail
    AwaitMail --> CheckMail
    GetMail --> ReadMail
    ReadMail --> WriteMail
    WriteMail --> PostMail
    PostMail --> AwaitMail
```