from cmath import sqrt
from colorama import Fore
from os import system
_ = system('cls')

known_prime_numbers = [2]

def print_known_primes():
    for prime in known_prime_numbers:
        print(prime, end= ", ")
    print("\b\b", flush=True, end=" \b\n")                                

def test_prime_up_to(max):
    print()
    print("1 is trivial, and not prime")
    print("2 is the first prime", end="   ")
    for number_we_are_testing in range (3, max + 1, 1):
        number_is_prime = True
        root = sqrt(number_we_are_testing).real
        for known_prime in known_prime_numbers:
            if root < known_prime:                                      
                break                                                   
            if number_we_are_testing % known_prime == 0:
                number_is_prime = False
                print(Fore.GREEN + f"[{known_prime}]",end="" + Fore.RESET)
                break                                                   
        if number_is_prime:            
            print(Fore.BLUE + "\b\b", flush=True, end="...\b" + Fore.RESET)
            print(Fore.YELLOW + f"\nPrime: {number_we_are_testing}..." + Fore.RESET)
            known_prime_numbers.append(number_we_are_testing)
            print(Fore.BLUE + "Not Prime :", end="" + Fore.RESET)
        else:
            print(Fore.BLUE + f"{number_we_are_testing}, ", end="" + Fore.RESET)            
    print(Fore.BLUE + "\b\b", flush=True, end="...\b" + Fore.RESET)
    print(f"\nThese are the numbers we saw were prime:")
    print_known_primes()
    print(f"We found {len(known_prime_numbers)} prime numbers between 1 and {max}!")

test_prime_up_to(int(input("How high would you like to look for prime numbers? ")))