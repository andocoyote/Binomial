import sys
import matplotlib.pyplot as plt

# This will allow ~1000 iterations for n
sys.setrecursionlimit(1010)

def Menu():
    print('1: Factorial()')
    print('2: Choose()')
    print('3: Probability()')
    print('4: Binomial()')
    print('5: Graph binomial distribution')
    print('0: Quit')
    
    selection = input('Please make your selection: ')
    
    return int(selection)
    

# n choose k
def Choose(n, k):
    return int( Factorial(n) / (Factorial(k) * Factorial(n-k)) )


# Standard method of computing factorial via recursion
def Factorial(n):
    if n <= 1:
        return 1
    
    return n * Factorial(n-1)


# Return the probability of desired outcomes/outcomes
def Probability(outcomes, desired):
    outcomes = outcomes if outcomes > 0 else 0

    return desired / outcomes


# Calculate the probability of k outcomes over n trials
def Binomial(k, n, p):
    # If n is > 1000, set it to 1000 so our Factorial doesn't blow up
    n = n if n <= 1000 else 1000

    return Choose(n, k) * (p**k) * ((1-p)**(n-k))


if __name__ == '__main__':

    while True:
        selection = Menu()
        
        if selection == 0:
            print('Good-bye.')
            break
        elif selection == 1:
            print('Running Factorial() ...')
            
            num = int(input('Enter a number: '))
            
            print('{0} factorialized is {1}'.format(num, Factorial(num)))
        elif selection == 2:
            print('Running Choose() ...')
            
            n = int(input('Enter your n (1-1000): '))
            k = int(input('Enter your k: '))
            
            num = Choose(n, k)
            
            print('{0} choose {1} is {2}'.format(n, k, num))
        elif selection == 3:
            print('Running Probability() ...')
            
            o = int(input('Enter your possible outcomes: '))
            d = int(input('Enter your desired outcomes: '))
            
            num = Probability(o, d)
            
            print('Probability: ', num)
        elif selection == 4:
            print('Running Binomial() ...')
            
            o = int(input('Enter your possible outcomes: '))
            d = int(input('Enter your desired outcomes: '))
            p = Probability(o, d)
            
            n = int(input('Enter your n (1-1000): '))
            k = int(input('Enter your k: '))
            
            print('Running Binomial() with:')
            print('Desired outcomes: ', k)
            print('Trials: ', n)
            print('Probability: ', p)
            
            num = Binomial(k, n, p)
            
            print('Probability is {0}'.format(num))
        elif selection == 5:
            o = int(input('Enter your possible outcomes: '))
            d = int(input('Enter your desired outcomes: '))
            p = Probability(o, d)
            
            n = int(input('Enter your n (1-1000): '))

            dist = [Binomial(k, n, p) for k in range(n+1)]
            
            print('Distribution: ', dist)

            print('Graphing a binomial distribution ...')
            
            plt.hist(x=range(n+1), bins=n+1, weights=dist)
            plt.xlabel('Count of desired outcomes')
            plt.ylabel('Probability for count of desired outcomes')
            plt.show()
