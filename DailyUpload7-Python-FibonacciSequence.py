# Fibonacci Sequence

def fibseq():
    num = 0
    max = 500
    listy = []

    i = 1
    listy.append(num)
    num += 1
    while i < max:
        listy.append(num)
        num = num + listy[i-1]
        i += 1
    print(listy)
        
fibseq()
