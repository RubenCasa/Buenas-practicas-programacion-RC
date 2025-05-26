import cProfile
import pstats
from codigo_original import encontrar_primos

def main():
    cProfile.run('encontrar_primos(100000)', 'profile_original.prof')

if __name__ == '__main__':
    main()