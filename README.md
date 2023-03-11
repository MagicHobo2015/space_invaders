# space_invaders
###This is a space invaders clone for CPSC 386###
CPSC 386: Introduction to Game Design - Spring 2023
Project One, Space Invaders, due Saturday, 11 Mar 2023 (by 2359)
In this assignment, you will create the Space Invaders game, based on the Alien Invasions! code
from Project One. The image resources you will need (ship, ship animation destruction, bunker,
different types of aliens, alien animation destruction, and ufo destruction) will all have to be
created using an Image editing tool such as Inkscape, Gimp, or Piskel. The audio resources you
will need can be captured using Audacity from an online version of Space Invaders.
Online versions can be found on Youtube, or by searching on Google.
![image](https://user-images.githubusercontent.com/57689601/224385085-6e0ee5c1-63da-4a4b-8d6c-bfb60a555d1e.png)
Classic Space Invaders has several differences from the Alien Invasions! Game. You will need to
complete the following:
1. You will need PyCharm or vsCode, Pygame, and Python 3 installed on your computer.
2. Using classic Space Invaders as a guide, and using your favorite Image editor such
as Inkscape, Gimp, or Piskel, create the four types of aliens shown above, the
traditional Space Invaders ship, and the bunkers to hide behind.
3. The aliens must include a simple, slow, two-state animation while they are
moving (it looks better if alternating aliens are synchronized). Aliens must have a different
image when they explode (could show a simple, fast animation as well).
4. A UFO should move across the screen at random intervals. It makes a continuous oscillating
sound as it moves. If it is destroyed, it shows its (random) value instead of an explosion.5. The ship must have a fast. animated explosion (8-12 frames) when it is destroyed. Be sure to
move the pixels of the exploding parts around from frame to frame. (Note: the ship we used in
Alien Invasions! Is not the same as that used in Classic Space Invaders.)
6. Create a LAUNCH screen, that shows the name of the game (in white and green), the aliens
and their values, and the menus for Play Game and High Scores. The start screen should
show at the beginning of each game, including if you have just lost a game.
7. Add lasers to the aliens, so they can shoot back at the ship. Use a random number generator
and a timer (pygame.time.get_ticks()) so they don’t shoot too often.
8. Add bunkers to the game that the ship can hide behind. The bunker can be damaged by both
the ship’s and aliens’ lasers. Use a random number generator to set the bunker’s pixels to
transparent when a laser strikes a part of the bunker to avoid a bite-out-of-a-sandwich look.
Use the Python Imaging Library to set the pixels.
9. Submit the zipped contents to Canvas AND submit to Canvas a GIF file showing your program
running. Do not put the GIF file inside the zip file. A short gif file should show basic game
aspects. A longer gif file, or mov or mp4 file should show all game aspects. Do not submit any
other type of movie file.
Submission
Turn in the code for this homework by uploading all of the Python source files you created, the
images directory, and the sounds directory as a zip file to Canvas. You must also take a screen
recording of your game playing, convert it to a GIF format, AND submit the GIF file to Canvas.
You may work as a team of up to TWO team members; be sure to submit the names of all team
members. Both team members should understand all aspects of the implementation.
Individuals submitting assignments on their own may discuss this homework assignment with other
students, however the work you submit must have been completed on your own.
To complete your submission, print the following sheet, fill out the spaces below, and submit it to the
professor in class by the deadline. Failure to follow the instructions exactly will incur a 10% penalty
on the grade for this assignment.
