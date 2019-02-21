'''Stochastic processes classes:
---------------------------------------
1. Arrival type processes
--------------------------------
   1.1. Bernoulli processes (Discrete time)
   -------------------------------
      1.1.1. Bionomial processes
      1.1.2. Geometric processes
      1.1.3. Pascal PMF
      
   1.2. Poisson processes (Continious time)
   -----------------------------
      1.2.1. Bionomial alike processes
      1.2.2. Geometric alike processes
      1.2.3. Erlang PDF

      
2. Markov processes
'''

from math import factorial, exp

def combin(n, k):
     '''n choose k
'''
     return(factorial(n) / (factorial(k) * factorial(n-k)))
#-----------------------------------------------------------------------------------------------------------------------------

class Bionom :
    '''Bionomial  process
n ---> Total number of trials.
k ---> Number of successful trials.
p ---> Probability of success.
'''
    def __init__(self, n, p, k):
        self.n = n
        self.p = p
        self.k = k
        self.Probability = combin(n, k) * p**k * (1-p)**(n-k)
        self.Expectation = self.n * self.p
        self.Varience = self.Expectation * (1-p)
#-------------------------------------------------------------------------------------------------------------------------------
        
class Geom:
    '''Geometric  process
k ---> Number of successful trials.
p ---> Probability of success.
'''
    def __init__(self, p, k):
        self.p = p
        self.k = k
        self.Probability = p * (1-p)**(k-1)
        self.Expectation = 1 / self.p
        self.Varience = self.Expectation * (1-p)/p
#-------------------------------------------------------------------------------------------------------------------------------

class Pascal:
    '''A sequence of geometric processes  scenarios.
k th success at time slot t with indvidual success probability p
'''
    def __init__(self, t, p, k):
        self.t = n
        self.p = p
        self.k = k
        self.Probability = combin(t-1, k-1) * p**k * (1-p)**(t-k)
        self.Expectation = self.k * self.p
        self.Varience = self.Expectation * (1-p)/p
#-------------------------------------------------------------------------------------------------------------------------------
        
class BionomPois:
    '''Bionomial  alike Poisson process
t ---> Time interval to be studied.
k ---> Number of events that may occure.
r ---> Rate of the event occurance. In references it's usually taking the Greek symbol LAMBDA.
'''
    def __init__(self, t, r, k):
        self.t = t
        self.r = r
        self.k = k
        self.Probability = (((r * t) ** k) / factorial(k)) * exp(-1 * r * t)
        self.Expectation = self.r * self.t
        self.Varience = self.Expectation
#-------------------------------------------------------------------------------------------------------------------------------

class GeomPois:
    def __init__(self, t, r):
        self.t = t
        self.r = r
        self.Probability = r * exp(-1 * r * t)
        self.Expectation = 1 / r
        self.Varience = self.Expectation ** 2
#-------------------------------------------------------------------------------------------------------------------------------

class Erlang:
    def __init__(self, t, r, k):
        self.t = t
        self.r = r
        self.k = k
        self.Probability = ((r**k) * (t**(k-1)) / factorial(k-1)) * exp(-1 * t)
        self.Expectation = k / r
        self.Varience = self.Expectation * (1 / r)
        
        
        





        
    
    
        
        
