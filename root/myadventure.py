user_choice = None

story = """You wake up in a dark room with a bad headache.

Footsteps and a dragged bat approach. Granny is coming!

A : Hide under the bed.
OR
B : Sneak out to the hall.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """You hide under the bed. Granny steps inside, looks around, but misses you.

A : Stay quiet and don't move.
OR
B : Crawl toward the window.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """Granny walks out and leaves the door open. You crawl out safely.

A : Run downstairs to unlock the door.
OR
B : Search the closet for a weapon.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You sprint downstairs, break the locks, and escape!

YOU ESCAPED! 
THE END
"""
            print(story)
        else:
            story = """You find a crossbow, but knock over a vase. CRASH!

Granny appears behind you and swings her bat. GAME OVER.

THE END
"""
            print(story)

    else:
        story = """You crawl toward the window, but the floor squeaks! Granny turns around.

A : Smash the window and jump out.
OR
B : Hide inside the wardrobe.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You smash the glass and jump out! You hurt your leg, but crawl away safely.

YOU ESCAPED!
THE END
"""
            print(story)
        else:
            story = """You hide in the wardrobe, but Granny opens the door and catches you. GAME OVER.

THE END
"""
            print(story)

else:
    story = """You step into the hallway. Granny is downstairs in the kitchen.

A : Sneak down the squeaky stairs.
OR
B : Check the bathroom for keys.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """The stairs squeak loud! Granny hears you and runs over.

A : Dash past her into the garage.
OR
B : Run back upstairs.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You dodge her, get into the car, and crash through the garage door!

YOU ESCAPED!
THE END
"""
            print(story)
        else:
            story = """You run back up, trip, and hit a trap. GAME OVER.

THE END
"""
            print(story)

    else:
        story = """You find a key in the bathroom, but Granny is coming!

A : Climb out the bathroom window to the roof.
OR
B : Run into the secret wall passage.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You climb onto the roof, drop down safely, and run away!

YOU ESCAPED!
THE END
"""
            print(story)
        else:
            story = """The passage leads to the basement, right into a giant spider web. GAME OVER.

THE END
"""
            print(story)