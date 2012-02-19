import itertools
import math
from math import *
import decimal
from decimal import *
from collections import deque
import prime


class Prime:
    """ Object for testing long integers for primality.
        Tests a number n by dividing it by all primes <= sqrt(n).
        Memoizes primes already found so that repeated use
        does not pay the performance penalty.

        Exports:
            .factor ( n )
                [ if n is a positive long integer ->
                    if n is prime ->
                      return None
                    else ->
                      return the smallest prime factor of n
                ]

            .factorize ( n )
                [ if n is a positive long integer ->
                    return a list of the prime factors of n
                ]

        State/invariants:
            ._p == A list of known primes
                INVARIANT: Excludes 1, and includes at least 2 and 3;
                all members are prime and sorted in ascending order.
            ._pMax == Upper limit of self._p
                INVARIANT: self._p is guaranteed to contain all
                primes <= self._pMax.

        Verified, June 1997, by Al Stavely.
    """


# - - -   _ _ i n i t _ _   - - -

    def __init__ ( self ):
        self._p     =  [ 2L, 3L, 5L ]
        self._pMax  =  6L


# - - -   f a c t o r   - - -

    def factor ( self, n ):
        """ [ if n is a positive long integer ->
                if n is prime ->
                  return None
                else ->
                  return the smallest prime factor of n
                in any case ->
                  self._p     :=  self._p with all necessary primes
                                  appended so that it contains all primes
                                  in the range [2,floor(sqrt(n))]
                  self._pMax  :=  max ( self._pMax, floor(sqrt(n)) )
            ]
        """

        #-- 1 --
        if  n < 4L:
            return None

        #-- 2 --
        #-[ limit  :=  the largest integer <= floor(sqrt(n))
        #-]
        limit  =  long ( sqrt ( float ( n ) ) )

        #-- 3 --
        #-[ self._p     :=  self._p with all necessary values
        #                   added so that it contains all primes <= limit
        #-] self._pMax  :=  max ( self._pMax, limit )
        #-]
        self._fill ( limit )

        #-- 4 --
        #-[ if there is an element E of self._p such that
        #   (E<=limit) and (E divides n) ->
        #     return the smallest such element
        #   else -> I
        #-]
        for f in self._p:
            #-- 4 body --
            #-[ if f > limit ->
            #     break
            #   else if f divides n ->
            #     return f
            #   else -> I
            #-]
            if  ( n % f ) == 0L:
                return f
            elif  f >= limit:
                break

        #-- 5 --
        return None


# - - -   . _ f i l l   - - -

    def _fill ( self, limit ):
        """ [ if limit is a positive long integer ->
                if self._pMax >= limit -> I
                else ->
                  self._p     :=  self._p with all primes P added
                                  such that (P <= limit)
                  self._pMax  :=  limit
        """

        #-- 1 --
        if  self._pMax >= limit:
            return

        #-- 2 --
        #--
        # Note: since the invariant guarantees that self._p
        # contains at least 3, and since all primes greater than
        # 3 are odd, our candidates are the odd numbers starting
        # at 2 + the last element of self._p.  We can't use a
        # `for' loop here because xrange() doesn't handle longs.
        #--
        i  =  self._p[-1] + 2L

        #-- 3 --
        #-[ self._p  :=  self._p with all primes P added
        #                such that (i <= P <= limit)
        #   i        :=  <anything>
        #-]
        while i <= limit:
            #-- 3 loop --
            #-[ if i is prime ->
            #     self._p  :=  self._p with i appended
            #   else -> I
            #   In any case ->
            #     i = i + 2L
            #-]
            if  not self.factor ( i ):
                self._p.append ( long(i) )

            i = i + 2L

        #-- 4 --
        self._pMax  =  limit


# - - -   . f a c t o r i z e   - - -

    def factorize ( self, n ):
        """ [ if n is a positive long integer ->
                return a list of the prime factors of n, excluding 1,
                and including n iff n is prime
            ]
        """
        #-- 1 --
        #-[ if n is prime ->
        #     f0  :=  None
        #   else ->
        #     f0  :=  the smallest prime factor in n
        #-]
        n   =  long(n)      # Permit calling with normal integers
        f0  =  self.factor ( n )

        #-- 2 --
        #-[ if f0 is None ->
        #     return [n]
        #   else ->
        #     result   :=  [f0]
        #     residue  :=  n / f0
        #-]
        if  not f0:
            return [n]
        else:
            result   =  [f0]
            residue  =  n / f0

        #-- 3 --
        #-[ result   :=  result with all prime factors of residue
        #                appended (except 1)
        #   residue  :=  <anything>
        #-]
        while  residue > 1:
            #-- 3 loop --
            #-[ if residue has a prime factor ->
            #     result  :=  result with the smallest prime factor of
            #                 residue appended
            #     residue :=  residue / (that smallest prime factor)
            #-]

            #-- 3.1 --
            #-[ if residue has a prime factor ->
            #     f0  :=  that factor
            #   else ->
            #     f0  :=  None
            #-]
            f0  =  self.factor ( residue )
            
            #-- 3.2 --
            #-[ if f0 is None ->
            #     result   :=  result with residue appended
            #     residue  :=  1
            #   else ->
            #     result   :=  result with f0 appended
            #     residue  :=  residue / f0
            #-]
            if  not f0:
                result.append ( residue )
                residue  =  1
            else:
                result.append ( f0 )
                residue = residue / f0

        #-- 4 --
        return result

def pandigitalN(n):
	num=""
	for i in range(0,len(str(n))):
		num+=str(i+1)
		numbers=list(num)
		string=list(str(n))
		if(len(string)==len(str(n))):
			for i in range(0,len(numbers)):
				if numbers[i] in string:
					None
				else:
					return False
		else:
			return False
	return True


p1 = Prime()




p=[]
st=""

def removeFromList(n,l):
	lis=[]
	for iL in range(0,len(l)):
			if(n == l[iL]):
				lis=l[:iL]+l[iL+1:]
	return lis			
ra1=[1,2,3,4,5,6,7,8,9]
for i1 in ra1:
	ra2=removeFromList(i1,ra1)
	for i2 in ra2:
		ra3=removeFromList(i2,ra2)
		for i3 in ra3:
			ra4=removeFromList(i3,ra3)
			for i4 in ra4:
				ra5=removeFromList(i4,ra4)
				for i5 in ra5:
					ra6=removeFromList(i5,ra5)
					for i6 in ra6:
						ra7=removeFromList(i6,ra6)
						for i7 in ra7:
								st=str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)
								if(p1.factor(int(st))==None and pandigitalN(int(st))):
									p.append(st)
						
	
print p