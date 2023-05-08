``` mermaid
classDiagram
    class Person {
        + string name
        + string address
        + letterbox
        + letters
        - encryption key
        + read_letter()
        + write_letter()
    }
    class Letter {
        + Person sender
        + Person receiver
        - string message
        + is_read()   
        + read_letter()
    }
    class Postboy {
        + name
        + address
        + letters
        + post office
        + get_letters()
        + has_letters()
        + deliver_letters()
    }
    class PostOffice {
        + String address
        + Letter letters
        + has_letters()
        + get_letters()
        + set_letters()
    }
    
    class Letterbox {
        + list letters
        + has_letters()
        + get_letters()     
        + set_letters()
    }
    Letterbox --* "*" Person: Reads
    Person --> Letter: Writes
    Letter --o "*" PostOffice: Holds
    PostOffice <-- Postboy
    Postboy --> Letterbox
    Letter "*" --o Letterbox
```

``` mermaid
sequenceDiagram
    actor Bob
    participant BobLetter
    participant BobLetterbox
    participant PostOffice
    
    actor Postboy
    
    participant OpheliaLetterbox
    participant OpheliaLetter
    
    actor Ophelia
    
    Bob ->> BobLetterbox: Check for letter/s
    alt has letter/s
        BobLetterbox ->> Bob: Read letter/s
    end
    Bob ->> PostOffice: Write letter/s
    Postboy ->> PostOffice: Get Letter/s
    Postboy ->> OpheliaLetterbox: Deliver Letter/s
    Ophelia ->> OpheliaLetterbox: Check for letter/s
    alt has letter/s
        OpheliaLetterbox ->> Ophelia: Read letter/s
    end
    Ophelia ->> PostOffice: Writes letter/s
    Postboy ->> PostOffice: Get Letter/s
    Postboy ->> BobLetterbox: Deliver Letter/s
```

``` mermaid
flowchart
    id1((Bob))
    id2((Alice))
    id3((Bob's Letterbox))
    id4((Alice's Letterbox))
    id5((Bob's Letter))
    id6((Alice's Letter))
    id7((Post Office))
    id8((Postboy))
    
    id1 -- 1.1: Check for letter/s --> id3
    id1 -- 1.2: Write letter/s --> id5
    id5 -- 2.1: Post letter/s --> id7
    id7 -- 3.1: Get letter/s --> id8
    id8 -- 4.1: Deliver letter/s --> id4
    id8 -- 4.2: Deliver letter/s --> id3
    id2 -- 1.3: Check for letter/s --> id4
    id2 -- 1.4: Write letter/s --> id6
    id6 -- 2.2: Post letter/s --> id7
  

    
    
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