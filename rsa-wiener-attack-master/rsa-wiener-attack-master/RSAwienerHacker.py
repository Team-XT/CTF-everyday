'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    #test_is_perfect_square()
    #print("-------------------------")
    e=1063045321283844468344531168992778520651192162100948533991539097447031440090068191835838938460807260866872379834796862916118785271062209281267667069640000501698142693389209275376843382863579650119977059768375028586326490055087394631528241983631462471709913758728591459476799115050977493979613545056736162868049
    n=837165022918376318972691589160491375229372195625940137121740685432530132860541010174727630660292946071507342455170833392895060048564125597915757582027572284342507277083636059558106672685400173531425920294781499112027917632497954958437660357575400222692979844873372105801998210845285775146263117399191185379347
    d= hack_RSA(n,e)
    print(d)


    


        
    
