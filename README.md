# Anki_FDeluxe

<H1>Conversion of flashcards from Anki to Flashcards Deluxe</H1>

This snippet of code is used for the conversion from Anki (PC) to Flashcards deluxe. This is for the purpose of optimizing the speed of making flashcards (use Anki free on PC and then upload to Flashcards Deluxe server)
This Git is one workaround for what mentioned in this thread: http://flashcardsdeluxe.com/forum/viewtopic.php?t=9
NOTE: This Git have only supported traditional flashcards (2 sides of text, there can be 1 picture on each side)

Intro: (Or more like why do I made this)
Anki on PC is super convenient for making flashcards (Freeware, with clipboard support), so that it's preferable to use Anki software to build flashcards.
However, Anki on mobile, e.g. iOS, is much more expensive than its peer, Flashcards Deluxe, which is another excellent app for learning flashcards on mobile.
I just want to take advantage of Anki and Flashcards deluxe, as they both have pros and cons (pls check the reviews if you haven't make up your mind for any of them)
Here are the links for aforementioned apps:
+ Anki flashcards: https://apps.ankiweb.net/
+ Flashcards Deluxe: http://orangeorapple.com/Flashcards/

How to use:
  1. Open Anki, build your flashcards package
  2. Export to "Notes/Cards in Plain text", note the location of your export txt to fill in the python code
  3. Check if the media files (imgs) is in this default directory "C:/Users/[YOUR USERNAME]/AppData/Roaming/Anki2/User 1/collection.media/" (The part before Anki2 can be accessed via this shortcut, type in the address bar: %appdata%)
     If that is the right folder, note its location and fill in the code (I have pointed it out in the source code)
  4. Change the directory of your export folder as you wish, in this case I have set 'E:/AnkiDeluxe' as the export folder
  5. Run the code. The export folder will have the text file (tab delimiter for uploading to Flashcards Deluxe server) and images you used in your deck
  6. Copy the text file for the structure of deck and zip images to upload them on Flashcards deluxe server or any other service (Dropbox, Gdrive,...)


P/s: Hope this helps for anyone who is struggling with flashcards building. I made this quite long ago for personal purpose at first as I'm using Flashcards Deluxe on my phone. I'll consider upgrading it with more types of flashcards when I can find enough time (and interest).

I'll publish the Quizlet - Deluxe conversion Git as well. Happy learning !
