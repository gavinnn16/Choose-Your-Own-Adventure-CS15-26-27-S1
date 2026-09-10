user_choice = None

story = """You wake up on a dirty mattress in a dark, creepy bedroom. 

Your head is pounding. You have five days to escape. 

You hear heavy footsteps and the dragging of a baseball bat coming up the stairs. 

Granny is home, and she knows you're awake.

A : Hide under the dusty bed.
OR
B : Sneak out the bedroom door into the hallway.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """You slide under the bed just as the door creeps open. 

Granny limps into the room, looking around with her crazy white eyes. 

She mutters, "I see you..." but she's looking the wrong way.

A : Stay perfectly still and hold your breath.
OR
B : Try to quietly crawl out from under the bed towards the window.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """She grunts, gives up, and walks out of the room, leaving the door open. 

You crawl out. The coast is temporarily clear. 

You can either make a break for the main exit or look for something to defend yourself.

A : Sprint downstairs to try and unlock the front door.
OR
B : Search her creepy closet for a weapon.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You sprint down the stairs like your life depends on it! 

You rip the wooden planks off the front door, unlock the padlock, and burst out into the woods!

YOU ESCAPED! 
THE END
"""
            print(story)
        else:
            story = """You open the closet and find a loaded crossbow! 

But as you grab it, you knock over an old vase. CRASH! 

Granny instantly teleports behind you and swings her bat. GAME OVER.

THE END
"""
            print(story)

    else:
        story = """You slowly crawl toward the window, but the floorboards squeak! 

Granny snaps her head toward you and raises her bloody bat. 

You have a split second to react.

A : Grab a nearby lamp and smash the window to jump.
OR
B : Dive into the wooden wardrobe next to the bed.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You smash the glass and jump out the second-story window! 

You break your leg on the grass below, but you manage to crawl away into the fog before she catches you.

YOU ESCAPED (barely).
THE END
"""
            print(story)
        else:
            story = """You dive into the wardrobe and shut the door. 

Granny walks slowly over to the wardrobe, chuckles, and rips the doors open. 

There's no way out. GAME OVER.

THE END
"""
            print(story)

else:
    story = """You tip-toe out into the dark hallway. 

You can hear Granny downstairs in the kitchen chopping meat. 

You need to get downstairs, but the stairs are notoriously squeaky.

A : Risk it and sneak down the squeaky stairs.
OR
B : Duck into the bathroom to look for the car keys.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """You take one step and... CREAAAK! 

Granny screams from the kitchen and starts running toward the stairs. 

She's fast when she's pissed off!

A : Sprint past her towards the garage.
OR
B : Panic and run back upstairs.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You dodge her bat swing by an inch, slide into the garage, and lock the door! 

You hop into her rusty car, hotwire it, and smash straight through the garage door!

YOU ESCAPED!
THE END
"""
            print(story)
        else:
            story = """You try to run back up, but you trip on the top step! 

You fall backwards, right into one of Granny's hidden bear traps. GAME OVER.

THE END
"""
            print(story)

    else:
        story = """You sneak into the bloody bathroom and look in the toilet. 

Bingo. The blue padlock key is sitting at the bottom of the bowl. 

You grab it, but you hear Granny coming up the stairs!

A : Squeeze through the bathroom window onto the roof.
OR
B : Run to the secret passage hidden behind the boxes in the hall.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You slide out onto the roof just as she busts the bathroom door down! 

You slide down the shingles, drop to the grass, and sprint to the front gate. 

YOU ESCAPED!
THE END
"""
            print(story)
        else:
            story = """You dive into the secret passage and slide down a pipe into the basement. 

Unfortunately, this is where Granny keeps her giant pet spider. You become its dinner. GAME OVER.

THE END
"""
            print(story)