# pUyjhmn-n
A Uyjhmn n (esoteric programming language made by Truttle1) interpreter in Python  
Wayyy less evil than Truttle1's IDE, but still annoying enough to **piss you off**

---

## About Uyjhmn n
Uyjhmn n is an esoteric programming language created by Truttle1.
It was (*was?*) originally created in Visual J# 2005 (yep, the one that *only* works for Windows 8.1 and under)

The laguage was designed to frustrate the user by combining:
- **Verbose syntax**: every command is a full sentence in ALL CAPS
- **Inconsistent syntax**: like how you *DECLARE* THE NEW VARIABLE but you *DEFINE* THE NEW LABEL.
- **Painful IDE**: There's a whole section about it so idk scroll down a few lines maybe

The name Uyjhmn n comes from gibberish typed when you slam your head on the keyboard out of frustration (look at where they are on the keyboard)

### Why name it pUYjhmn n
There's a Node.js interpreter that's named **j**Uyjhmn n which the j at the start stands for Java (maybe idk) so this one continues the tradition by naming it **p**Uyjhmn n which the p stands for Python, wow!

---

## Acerca del doloroso IDE
- Closed if you try to *pegar* code
- Every 10 seconds (indecated by white text in cyan textbox) will move the top line in the white textbox to the *verde* texhbox
- When you type in *inválida* code, the line will not get moved and instead get removed and the timer is halved
- Had 2 radio buttons and a *barra de progresso* that ultimately does nothing
- Feacherd a "JUST INTERPRET MY CODE ALREADY" button and ran code *a costa de* copying

This interpreter will skip all that nonsense, you can actually run code without accidentally typing Uyjhmn n.  
but worry not! The docstring still has enough errors to **piss you off**

---

## Commands
###### (figure them out yourself lol)
- PRINT THE CHARACTER WITH THE ASCII VALUE [c]
- DECLARE THE NEW VARIABLE [v]
- OPEN THE VARIABLE [v]
- ASSIGN [c] TO THE OPEN VARIABLE
- ADD [v] TO THE OPEN VARIABLE
- MULTIPLY TO THE OPEN VARIABLE BY [v]
- PRINT THE OPEN VARIABLE'S CHARACTER
- PRINT THE OPEN VARIABLE'S VALUE
- DEFINE NEW LABEL [i]
- JUMP TO [i] IF [v1] IS EQUAL TO [v2]
- JUMP TO [i] IF [v1] IS GREATER THAN [v2]
- JUMP TO [i] IF [v1] IS LESS THAN TO [v2]
- GET INPUT AND STORE INTO OPEN VARIABLE AS A CHARACTER
- GET INPUT AND STORE INTO OPEN VARAIBLE AS A NUMBER
- END THIS PROGRAM
###### (It's actually VARIABLE instead of VARAIBLE, whoops)

Note: No `USE: [extension name]` command, for reasons known but not shown (why did that *rhyme*?)

---

## Example programs
A cat program which you literally have to type each character in 1 by one and type ! to end the program which is also printed
```
DECLARE THE NEW VARIABLE !
OPEN THE VARIABLE !
ASSIGN 33 TO THE OPEN VARIABLE
DECLARE THE NEW VARIABLE X
OPEN THE VARIABLE X
JUMP TO AGAIN IF ! IS EQUAL TO !
DEFINE THE NEW LABEL AGAIN
JUMP TO BYE IF ! IS EQUAL TO X
GET INPUT AND STORE INTO OPEN VARIABLE AS A CHRACTER
PRINT THE OPEN VARIABLE'S CHARACTER
JUMP TO AGAIN IF! IS EQUAL TO !
DEFINE THE NEW LABEL BYE
END THIS PROGRAM
```
### Test run:  
Input: (each character seperated by a enter since well yk)
```
Hello, world!
```
Output:
```
Hello, world!
```

A simple number guessing program with the number being the signed 64-bit integer limit
```
DECLARE THE NEW VARIABLE NUM
OPEN THE VARIABLE NUM
ASSIGN 9223372036854775807 TO THE OPEN VARIABLE
DECLARE THE NEW VARIABLE X
JUMP TO AGAIN IF NUM IS EQUAL TO NUM
DEFINE THE NEW LABEL AGAIN
OPEN THE VARIABLE X
GET INPUT AND STORE INTO OPEN VARIABLE AS A NUMBER
JUMP TO LESS IF X IS LESS THAN NUM
JUMP TO EQUAL IF X IS EQUAL TO NUM
JUMP TO MORE IF X IS GREATER THAN NUM
DEFINE THE NEW LABEL LESS
PRINT THE CHARACTER WITH THE ASCII VALUE 84
PRINT THE CHARACTER WITH THE ASCII VALUE 111
PRINT THE CHARACTER WITH THE ASCII VALUE 111
PRINT THE CHARACTER WITH THE ASCII VALUE 32
PRINT THE CHARACTER WITH THE ASCII VALUE 115
PRINT THE CHARACTER WITH THE ASCII VALUE 109
PRINT THE CHARACTER WITH THE ASCII VALUE 97
PRINT THE CHARACTER WITH THE ASCII VALUE 108
PRINT THE CHARACTER WITH THE ASCII VALUE 108
PRINT THE CHARACTER WITH THE ASCII VALUE 33
PRINT THE CHARACTER WITH THE ASCII VALUE 10
JUMP TO AGAIN IF NUM IS EQUAL TO NUM
DEFINE THE NEW LABEL EQUAL
PRINT THE CHARACTER WITH THE ASCII VALUE 73
PRINT THE CHARACTER WITH THE ASCII VALUE 116
PRINT THE CHARACTER WITH THE ASCII VALUE 32
PRINT THE CHARACTER WITH THE ASCII VALUE 119
PRINT THE CHARACTER WITH THE ASCII VALUE 97
PRINT THE CHARACTER WITH THE ASCII VALUE 115
PRINT THE CHARACTER WITH THE ASCII VALUE 32
PRINT THE OPEN VARIABLE'S VALUE
PRINT THE CHARACTER WITH THE ASCII VALUE 33
JUMP TO BYE IF NUM IS EQUAL TO NUM
DEFINE THE NEW LABEL MORE
PRINT THE CHARACTER WITH THE ASCII VALUE 84
PRINT THE CHARACTER WITH THE ASCII VALUE 111
PRINT THE CHARACTER WITH THE ASCII VALUE 111
PRINT THE CHARACTER WITH THE ASCII VALUE 32
PRINT THE CHARACTER WITH THE ASCII VALUE 108
PRINT THE CHARACTER WITH THE ASCII VALUE 97
PRINT THE CHARACTER WITH THE ASCII VALUE 114
PRINT THE CHARACTER WITH THE ASCII VALUE 103
PRINT THE CHARACTER WITH THE ASCII VALUE 101
PRINT THE CHARACTER WITH THE ASCII VALUE 33
PRINT THE CHARACTER WITH THE ASCII VALUE 10
JUMP TO AGAIN IF NUM IS EQUAL TO NUM
DEFINE THE NEW LABEL BYE
END THIS PROGRAM
```
Example run: (alternating input and printed)
```
5
Too small!
123456789098765432123456789098765432123456789098765432
Too big!
9223372036854775807
It is 9223372036854775807!
```
###### (not to be confused with 9223372036854775807 factorial)

There's also 99 bottles of beer on the wall but it's in like the contents of this repo, the .txt with the name "Uyjhmn n_99_bottles_of_beer"

---

## Credits
- Original language creator: Truttle1
- Wiki with all the elegantly cursed details: https::/esolangs.org/wiki/Uyjhmn_n
- The third letter of the alphabet: C

---

## Notes
- Don't carelessly name variables, the regex might cry
- don't you looooooooove inconsistencies?
- Ah yes, unprofessionally typing a docstring with a professional template.

---

## License
Published under the Unlicense.  
You can freely fork it, break it, make it sentient, remake the IDE on tkinter and make it more evil than Truttle1's by removing the timer on the screen so the timer is still there but you can't see it, add the extensions, turn it into a plum, yeah whatever.

---

O7DeOaDdZIW9VJVIZGDdOaZeOnVeO7DdOaA9O7DeOaDdZGDdOaZeOnVIZIW9VJVeO7DdOaA9OaZeO7DdZIW9VJVIZGZeOaDeOnVeO7DdOaA9OaZeO7DdZGDdOaZeOnVIZIW9VJVeO7DdOaA9VJVeO7DdOaA9OaZeO7DdZIW9VJVIZGDdOaZeOnVeO7DdOaA=
