import math

def timeConversion(s):
    l=len(s)
    if s[l-2]=='A' and int(s[0:2])>=12:
        return(f'0{int(s[0:2])%12}{s[2:l-2]}')
    if s[l-2]=='P' and int(s[0:2])<12:
        return(f'{int(s[0])+1}{int(s[1])+2}{s[2:l-2]}')
    else:
        return(s[0:l-2])
