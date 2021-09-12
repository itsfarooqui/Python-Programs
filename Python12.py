#12. Print gender (Male/Female) program according to given M/F using switch.

def gender(i):
        switcher={
                'M':'Male',
                'F':'Female'
             }
        return switcher.get(i,"Please enter again!")

gender('M')