


saat=int(input("Kaldigıniz sureyi Girin:"))

ucret=0

if saat <=1 :
    ucret =5
elif saat <=5:
    ucret = 4 * saat
else:
    ucret = 3*saat

    print("Odemeniz Gereken Ucret : {}".format(ucret))
    