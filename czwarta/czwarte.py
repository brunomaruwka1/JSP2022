def n_ty_wyrazcgeo(n,a1=1,q=2):
    an=a1*q**(n-1)
    return an

#przykłady
#a1=1, q=2, n=5
print(n_ty_wyrazcgeo(5))

#a1=2, q=3 ,n=6
print(n_ty_wyrazcgeo(6,2,3))