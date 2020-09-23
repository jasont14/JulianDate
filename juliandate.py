def GetJulianDate(yr, mnth, dy, tme):
    cal = 'g'

    t = tme / 24
    dy = dy + t

    if mnth == 1 or mnth ==2:
        mnth += 12
        yr = yr - 1
    
    if yr <= 1582:
        cal = 'j'
        if yr == 1582 and mnth >= 10:
            cal = 'g'
    
    A = 0
    B = 0

    if cal == 'g':
        A = int(yr/100)
        B = 2 - A + int(A/4)

    p1 = int(365.25*(yr + 4716))
    p2 = int(30.6001*(mnth + 1))
    
    result = p1 + p2 + dy + B -1524.5
    return result

j = GetJulianDate(1957, 10, 4, 19.44);
print(j)

k = GetJulianDate(333, 1, 27, 12);
print(k)

l = GetJulianDate(2020, 9, 22, 0)
print(l)

def GetJD1900(yr, mnth, dy, tme):
    jd = GetJulianDate(yr,mnth,dy,tme)

    result = (jd - 2415020.31352)

    return result

m = GetJD1900(2020, 9, 22,0)

print(m)

