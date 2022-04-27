# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:17:55 2022

@author: Andy

The Stanley Parable ULTRA DELUXE Launch Preparedness Initiative (TSPUDLPI)

https://crowscrowscrows.com/email/46/
https://crowscrowscrows.com/email/46/assets/images/socialchart.jpg


THE UNLICENSE

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

"""

import random
import pyperclip

p1 = ["I was a big fan of ",
      "My favourite part was ",
      "Crows Crows Crows have outdone themselves when it comes to ",
      "I'm literally in tears over ",
      "I'm super mad about ",
      "I can't believe they got rid of",
      "I hate Crows. They ruined ",
      "I'll never buy another Crows game after seeing ",
      "Ngl, I absolutely hated ",
      "OMG I can't believe ",
      "I am a sucker for ",
      "WOW!!!! I've never seen something so cool as ",
      "Fuming doesn't cover it. What the hell have they done to ",
      "I'm literally shaking with excitement after seeing ",
      "Wow... ",
      "I laughed, I cried, I fist pumped the air. Just wait until you see ",
      "Crows screwed up ",
      "The Stanley Parable wiki makes no mention of ",
      "Absolutely insane that they've done to ",
      "I can't stop telling my family about ",
      "My entire contact list received a 3am message about ",
      "Maybe the best gameplay experience of my life was ",
      "Gotta say, I'm loving ",
      "I will never forgive Kevan Brighting for ",
      "Crows removing Stanley's soul patch is justified by ",
      "Kinda disappointed by ",
      "Okay.... loving ",
      "I'm neutral on ",
      "The entire Godfather Trilogy < ",
      "Won't be playing TSPUD again because of "]

p2 = ["the freedom ending",
      "the new subtitles",
      "that final boss fight in the pyramid",
      "all the Elden Ring references",
      "those dumb sidekick characters",
      "the new third-person view mode",
      "the adventure line",
      "the kingdom ending",
      "Stanley's dad",
      "that new cop character",
      "the parrot mini-game in the jungle ending",
      "the new narrator",
      "all of jack black's appearances",
      "the beard ending",
      "the graphics",
      "that employee 428 scene",
      "Stanley",
      "the broom closet fight",
      "the apartment ending",
      "Stanley's death",
      "the moment when the narrator appears in person",
      "the Cypress Hill cameo",
      "the point system",
      "all the product placement",
      "the credits",
      "the 3 new playable characters",
      "that final action sequence",
      "the buggy mess that is this game",
      "the jetpack ending"]

s1 = random.choice(p1)
s2 = random.choice(p2)
s3 = s1 + s2
pyperclip.copy(s3)
