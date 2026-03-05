import time,sys,threading
class practical:   
    def vow(x:str,edge:bool=False):
        v=list("aeiou")
        if edge:
            v.extend(["y"])
        for i in range(len(x)):
            if x[i].lower() in v:
                x=x.replace(x[i],"*")
            else:
                print("wrong")
        print(x)
        return x
    def two_smallnum(x:list):
        x=sorted(set(x))
        print(x[:2])
        return x[:2]
    def alt_series(x:int=1,n:int=1):
        sign=1
        nn=n
        n=0
        s=0
        while nn>=n:
            s+=(x**n)*sign
            n+=1
            sign*=-1
            print(s)
        return s
    def odd_cap(x: str):
        print(f"Original string: {x}")
        xx = ""
        for i in range(len(x)):
            if i % 2 == 1:
                xx += x[i].upper()
            else:
                xx += x[i]
        print(f"Changed string: {xx}")
    def pin_code(x:str):
        dig=""
        for ch in x:
            if ch.isdigit():
                dig+=ch
        print(dig)
        return dig
    def tru_pin(x:str):
        for i in range(len(x)):
            if x[i].isdigit():
                pincode=x[i:(i+6)]
                if pincode.isdigit() and len(pincode):
                    print(pincode)
                    break
        else:
            print("no pincode found")
    def sum_str(x:str):
        dig=""
        s=0
        for ch in x:
            if ch.isdigit():
                dig+=ch
                s+=int(ch)
        else:
            if len(dig)>1:
                pass
            else:
                print(f"{x} has no digits")
        print(f"{x} has digits {dig} which sum to {s}.")
    def char_checker(x:str):
        words=sc=0
        for i in x:
            sc+=1
            if i.isalnum():
                words+=1
        x=x.split()
        print(f"number of words is {len(x)} ,number of character in total {sc} ,\npercentage of alphanumeric charachters is {(words/sc)*100}%")
    def case_converter(x:str):
        f=""
        for ch in x:
            if ch.islower():
                f+=ch.upper()
            elif ch.isupper():
                f+=ch.lower()
            elif not ch.isalnum():
                f+=ch
        print(f)
    def ai_roman_converter(x:int):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        for i in range(len(val)):
            count = x // val[i]
            roman_num += syms[i] * count
            x -= val[i] * count
        print(roman_num)
        return roman_num
    def word_count(x:str):
        x=x.split()
        print(len(x))
    def paraenthesis_count(x:str):
        count=0
        while "()" in x:
            s=x.count("()")
            count+=s
            if s==1:
                x=x.replace("()","")
                print(x)
        else:
            print(x)
        print(f"number of ():{(count)}")
    def num_vowels(x:str):
        s=list("aeiou")
        count=0
        for ch in x:
            if ch in s:
                count+=1
        print(f"the number of vowels is {count}")
    def long_word(x:str):
        x=x.split()
        max=index=0
        for i in range(len(x)):
            word=len(x[i])
            if word>max:
                max=word
                index=i
        print(f"the longest word is {x[index]} with {max} characters")
    def reverse_words(x:str):
        x=x.split()
        l=[]
        s=""
        for i in range(len(x)):
            s=x[i]
            s=s[::-1]
            l.append(s)
        print(" ".join(l))
    def sqr_series(x:int,n:int):
        m=n
        n=s=0
        while m>=n:
            s+=x**n
            n+=1
            print(s)
    def pincode_new(x:str):
        s=""
        x.strip()
        x.rstrip(".")
        s=x[-6:-1]
        if s.isdigit():
            print(f"pincode is {s}")
        else:
            print("invalid address. pincode doesn't exist.")
    def dig_checker(x:str):
        for ch in x:
            if ch.isdigit():
                print(f"{x} contains digits")
                break
        else:
            print(f"{x} has no digits")
    def anime(txt:str,cd:float=0.1):
        a=10
        while True:
            sys.stdout.write("\t\t"+(txt*a)+"\r")
            sys.stdout.flush()
            time.sleep(cd)
            txt=txt[1:]+txt[0]
t=threading.Thread(target=practical.anime,args=(" jelloo world ",0.25))
t.daemon=True
t.start()
for i in range(109):
    print(f" numcer = {i}")
    time.sleep(0.1)
