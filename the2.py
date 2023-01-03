a = input()
if a.find("?") == -1:
    if a[5] == "X": 
        upperx = list(a[0:5])
        upperx.append(10)
        if upperx[5] == (2 * int(a[0]) + 3 * int(a[1]) + 5 * int(a[2]) + 7 * int(a[3]))%11:
            print("VALID")
        else:
            print("INVALID")
        
    elif int(a[5])  == (2 * int(a[0]) + 3 * int(a[1]) + 5 * int(a[2]) + 7 * int(a[3]))%11:
            print("VALID")
    elif int(a[5]) != (2 * int(a[0]) + 3 * int(a[1]) + 5 * int(a[2]) + 7 * int(a[3]))%11:
            print("INVALID")
elif a.find("?") != -1:
        x = a[0]
        y = a[1]
        z = a[2]
        k = a[3]
        l = a[5]
        if a.find("?") == 5:
            c = str((2 * int(a[0]) + 3 * int(a[1]) + 5 * int(a[2]) + 7 * int(a[3]))%11)
            if c == "10":
                last = a[0:5] + "X"
                print(last)
            else:
                print(a.replace("?", c))
        elif a.find("?") == 0:
            if a[5] == "X":
                d = (10) - ((3*int(a[1]) + 5*int(a[2]) + 7 * int(a[3]))%11)
            else:
                d = (int(a[5])) - ((3*int(a[1]) + 5*int(a[2]) + 7 * int(a[3]))%11)
            if d < 0:
                    b = int(d + 11)
                    if b%2 == 0:
                        e = str(int(b/2))
                        print(a.replace("?",e))
                    elif b%2 == 1:
                        e = str(int((b + 11)/2))
                        print(a.replace("?",e))
                
            elif d >= 0:
                    if d%2 == 0:
                        c = str(int(d/2))
                        print(a.replace("?",c))
                    elif d%2 == 1:
                        e = str(int((d + 11)/2))
                        print(a.replace("?",e))
                    
        elif a.find("?") == 1:
            if a[5] == "X":
                d = (10) - (((2 * int(x)) + (5 * int(z)) + (7 * int(k)))%11)
            else:
                d = (int(l)) - (((2 * int(x)) + (5 * int(z)) + (7 * int(k)))%11)
            if d < 0:
                b = int(d + 11)
                if b%3 == 0:
                    e = str(int(b/3))
                    print(a.replace("?",e))
                elif b%3 == 1:
                    e = str(int((b + 11)/3))
                    print(a.replace("?",e))
                elif b%3 == 2:
                    e = str(int((b + 22)/3))
                    print(a.replace("?",e))
            elif d >= 0:
                if d%3 == 0:
                    c = str(int(d/3))
                    print(a.replace("?",c))
                elif d%3 == 1:
                    e = str(int((d + 11)/3))
                    print(a.replace("?",e))
                elif d%3 == 2:
                    e = str(int((d + 22)/3))
                    print(a.replace("?",e))
        elif a.find("?") == 2:
            if a[5] == "X":
                d = (10) - (((2 * int(x)) + (3 * int(y)) + (7 * int(k)))%11)
            else:
                d = (int(l)) - (((2 * int(x)) + (3 * int(y)) + (7 * int(k)))%11)
            if d < 0:
                b = int(d + 11)
                if b%5 == 0:
                    e = str(int(b/5))
                    print(a.replace("?",e))
                elif b%5 == 1:
                    e = str(int((b + 44)/5))
                    print(a.replace("?",e))
                elif b%5 == 2:
                    e = str(int((b + 33)/5))
                    print(a.replace("?",e))
                elif b%5 == 3:
                    e = str(int((b + 22)/5))
                    print(a.replace("?",e))
                elif b%5 == 4:
                    e = str(int((b + 11)/5))
                    print(a.replace("?",e))
            elif d >= 0:
                if d%5 == 0:
                    e = str(int(d/5))
                    print(a.replace("?",e))
                elif d%5 == 1:
                    e = str(int((d + 44)/5))
                    print(a.replace("?",e))
                elif d%5 == 2:
                    e = str(int((d + 33)/5))
                    print(a.replace("?",e))
                elif d%5 == 3:
                    e = str(int((d + 22)/5))
                    print(a.replace("?",e))
                elif d%5 == 4:
                    e = str(int((d + 11)/5))
                    print(a.replace("?",e))
        elif a.find("?") == 3:
            if a[5] == "X":
                d = (10) - (((2 * int(x)) + (3 * int(y)) + (5 * int(z)))%11)
            else:
                d = (int(l)) - (((2 * int(x)) + (3 * int(y)) + (5 * int(z)))%11)
            if d < 0:
                b = int(d + 11)
                if b%7 == 0:       
                    e = str(int(b/7))
                    print(a.replace("?",e))
                elif b%7 == 1:
                    e = str(int((b + 55)/7))
                    print(a.replace("?",e))
                elif b%7 == 2:
                    e = str(int((b + 33)/7))
                    print(a.replace("?",e))
                elif b%7 == 3:
                    e = str(int((b + 11)/7))
                    print(a.replace("?",e))
                elif b%7 == 4:
                    e = str(int((b + 66)/7))
                    print(a.replace("?",e))
                elif b%7 == 5:
                    e = str(int((b + 44)/7))
                    print(a.replace("?",e))
                elif b%7 == 6:
                    e = str(int((b + 22)/7))
                    print(a.replace("?",e))
            elif d >= 0:
                if d%7 == 0:       
                    e = str(int(d/7))
                    print(a.replace("?",e))
                elif d%7 == 1:
                    e = str(int((d + 55)/7))
                    print(a.replace("?",e))
                elif d%7 == 2:
                    e = str(int((d + 33)/7))
                    print(a.replace("?",e))
                elif d%7 == 3:
                    e = str(int((d + 11)/7))
                    print(a.replace("?",e))
                elif d%7 == 4:
                    e = str(int((d + 66)/7))
                    print(a.replace("?",e))
                elif d%7 == 5:
                    e = str(int((d + 44)/7))
                    print(a.replace("?",e))
                elif d%7 == 6:
                    e = str(int((d + 22)/7))
                    print(a.replace("?",e))
                         

                    
                
                
            

              



