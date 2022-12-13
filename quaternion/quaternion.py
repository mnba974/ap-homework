
class Quaternion:
    def __init__(self, a, b=0, c=0, d=0):
        if isinstance(a,complex):
            self.a=a.real
            self.b=a.imag
            self.c=c
            self.d=d 
        else:
            self.a=a
            self.b=b
            self.c=c
            self.d=d 
    def __repr__(self):
        st=''
        if self.a!=0:
            st+=f"{self.a}"
        if self.b!=0:
            if st!='':
                st+=' + '
            st+=f"{self.b}i"
        if self.c!=0:
            if st!='':
                st+=' + '
            st+=f"{self.c}j"
        if self.d!=0:
            if st!='':
                st+=' + '
            st+=f"{self.d}k"
        return st
    def __eq__(self,num):
        if isinstance(num, Quaternion):
            if (self.a,self.b,self.c,self.d)==(num.a,num.b,num.c,num.d):
                return True
            return False
        if isinstance(num, int) or isinstance(num, float):
            if (self.a,self.b,self.c,self.d)==(num,0,0,0):
                return True
            return False
        if isinstance(num, complex):
            if (self.a,self.b,self.c,self.d)==(num.real,num.imag,0,0):
                return True
            return False
        return False
    def __mul__(self,x):
        a1 = self.a*x.a -(self.b*x.b +self.c*x.c + self.d*x.d)
        a2 = self.a*x.b + self.b*x.a +self.c*x.d -self.d*x.c
        a3 = self.a*x.c - self.b*x.d +self.c*x.a +self.d*x.b
        a4 = self.a*x.d + self.b*x.c -self.c*x.b +self.d*x.a
        return Quaternion(a1,a2,a3,a4)
    def __add__(self,num):
        if isinstance(num, Quaternion):
            return Quaternion(self.a +num.a,self.b + num.b ,self.c + num.c, self.d + num.d)
        if isinstance(num, int) or isinstance(num, float):
            return Quaternion(self.a +num,self.b ,self.c, self.d )
        if isinstance(num, complex):
            return Quaternion(self.a + num.real, self.b + num.imag ,self.c , self.d )