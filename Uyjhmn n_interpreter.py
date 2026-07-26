import re
def pUyjhmn_n(code: str):
    """
    An Uyjhmn n interpreter written in Python. Way less evil than Truttle1's IDE.

    About Uyjhmn n
    --------------
        Uyjhmn n is an esoteric programming language made by Truttle1.
        Uyjhmn n is written in Visual J# 2005, which only works for wIndows <= 8.1 only.
        Uyjhmn n was designed to annoy the user by combining verbose syntax with a terrible looking
        IDE that rushes the user. It was named after the giBberish that gets typed when you bang 
        your head on your keyboard out of frustration (look at where those characters are on the 
        keyboard)
        Note that this docstring is also made to annoy you, but wayyy less than Truttle1's.
        
        About the IDE
        -------------
            Wait can I nest this? Actually whatever as long as you get it, but I will nest.
            I'm shortening this: all Uyj code must written in Uyj IDE. IF u try copy code into IDE, it
            close. Ide feachers a white textbox wher user input code. After timer in long cyan box
            (orginly 10)equal 0 the first line in da white textbox is removed to the green textbox and
            now it's inWebdings so u can't read it and made so that u can't see mistakes unless u learn
            how to read it. If usr write BAD code, bad cod is not put in the green textbox but is
            removed and the timr is halved to punish usr. if top line is empty, code in green textbox
            is interpreted yay. the IDe also has 2 radio butons that do no'in and a "progress" bar dat
            constatly fills up and resets, which also does no'in. Above le white textbox is "JUST
            INTERPRET MY CODE ALREADY" button which just... interprets yo code when pressed. Also you
            can now copy it but youll have to retype that.
        
        Commands (figure them out yourself lol)
        -------- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        PRINT THE CHARACTER WITH THE ASCII VALUE [c]
        DECLARE THE NEW VARIABLE [v]
        OPEN THE VARIABLE [v]
        ASSIGN [c] TO THE OPEN VARIABLE
        ADD [v] TO THE OPEN VARIABLE
        MULTIPLY TO THE OPEN VARIABLE BY [v]
        PRINT THE OPEN VARIABLE'S CHARACTER
        PRINT THE OPEN VARIABLE'S VALUE
        DEFINE NEW LABEL [i]
        JUMP TO [i] IF [v1] IS EQUAL TO [v2]
        JUMP TO [i] IF [v1] IS GREATER THAN [v2]
        JUMP TO [i] IF [v1] IS LESS THAN TO [v2]
        GET INPUT AND STORE INTO OPEN VARIABLE AS A CHARACTER
        GET INPUT AND STORE INTO OPEN VARAIBLE AS A NUMBER
        END THIS PROGRAM
        
        Also note that I'm not adding the command
        USE: [e]
        Since why not, oh and also because I'm lazy, yeah, deal with it, also a bunch of other interpreters add this, so why pick mine anyway. Oh and so that Drexel will not hate anyone who uses this

    Credits
    -------
        Creator of Uyjhmn n: Truttle1
        Website that convinently includes just about all information about Uyjhmn n: https::/esolangs.org/wiki/Uyjhmn_n#IDE

    Notes
    -----
        Don't carelessly name variables, the regex might cry
        don't you loooove inconsistencies?
    """
    def isopen():
        if opened_var == None:
            raise SyntaxError('No variables were opened, did you forget to open a variable?')
    def isinvars(x):
        if x not in vars:
            raise SyntaxError(f'{x} is not declared, did you forget to declare variable {x}?')
    def isinlabels(x):
        if x not in labels:
            raise SyntaxError(f'{x} is not defined, did you forget to define label {x}?')
    def print_alt(x):
        print(x, end='', flush=True)
    def check_idk():
        isinlabels(label)
        isinvars(var1)
        isinvars(var2)
    code = code.split('\n')
    vars={}
    labels={}
    opened_var = None
    lcode = len(code) - 1
    curr_line = 0
    # Word shortcuts
    tov = ' THE OPEN VARIABLE'
    ttov = f' TO{tov}'
    ptov = f'PRINT{tov}\'S '
    pat = r'JUMP TO (.*?) IF (.*?) IS '
    giasiopaa = 'GET INPUT AND STORE INTO OPEN VARIABLE AS A '
    # The labels get processed first lol
    for line, idx in enumerate(code):
        if idx.startswith('DEFINE THE NEW LABEL '):
            if line == lcode:
                raise SyntaxError(f'Nothing is after the label {idx.lstrip('DEFINE THE NEW LABEL ')}. Did you forget to add something after the label?')
            labels[idx[21:]] = line + 1
    while True:
        if curr_line > lcode:
            raise SyntaxError('The program reached the end of the program without ending, did you forget to end the program?')
        line = code[curr_line]
        sw = line.startswith
        ew = line.endswith
        jump = False
        if sw('PRINT THE CHARACTER WITH THE ASCII VALUE '):
            print_alt(chr(int(line.lstrip('PRINT THE CHARACTER WITH THE ASCII VALUE '))))
        elif sw('DECLARE THE NEW VARIABLE '):
            vars[line[25:]] = 0
        elif sw('OPEN THE VARIABLE '):
            var = line[18:]
            isinvars(var)
            opened_var = var
        elif sw('ASSIGN ') and ew(ttov):
            isopen()
            vars[opened_var] = int(line[7:-21])
        elif sw('ADD ') and ew(ttov):
            var = line[4:-21]
            isopen()
            isinvars(var)
            vars[opened_var] += vars[var]
        elif sw(f'MULTIPLY{tov} BY '):
            var = line[30:]
            isopen()
            isinvars(var)
            vars[opened_var] *= vars[var]
        elif line == f'{ptov}CHARACTER':
            isopen()
            print_alt(chr(vars[opened_var]))
        elif line == f'{ptov}VALUE':
            isopen()
            print_alt(vars[opened_var])
        elif line == giasiopaa+'CHARACTER':
            inp = input()
            if len(inp) != 1:
                raise ValueError('Inoutted string is too long or too short, input in 1 character only.')
            vars[opened_var] = ord(inp)
        elif line == giasiopaa+'NUMBER':
            inp = input()
            try:
                inp = int(inp)
            except ValueError:
                raise ValueError(f'Invalid literal for int(): \'{inp}\'') # Yep
            else:
                vars[opened_var] = inp
            
        elif line == 'END THIS PROGRAM':
            break
        else:
            pat_temp = pat + r'EQUAL TO (.*?)$'
            m = re.match(pat_temp, line)
            if m:
                label, var1, var2 = m.groups()
                check_idk()
                if vars[var1] == vars[var2]:
                    curr_line = labels[label]
                    jump = True
            else:
                # Now do it 2 more times with each time indented by 1 more
                pat_temp = pat + r'GREATER THAN (.*?)$'
                m = re.match(pat_temp, line)
                if m:
                    label, var1, var2 = m.groups()
                    check_idk()
                    if vars[var1] > vars[var2]:
                        curr_line = labels[label]
                        jump = True
                else:
                    pat_temp = pat + r'LESS THAN (.*?)$'
                    m = re.match(pat_temp, line)
                    if m:
                        label, var1, var2 = m.groups()
                        check_idk()
                        if vars[var1] < vars[var2]:
                            curr_line = labels[label]
                            jump = True
                    else:
                        if not sw('DEFINE THE NEW LABEL'):
                            raise SyntaxError(f'Unknown command: {line}')
        if not jump:
            curr_line += 1
