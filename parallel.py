from mpi4py import MPI
from mpi4py.futures import MPICommExecutor


def is_prime(n):
    return not any(n % i == 0 for i in range(2, n))


if __name__ == '__main__':
    with MPICommExecutor(MPI.COMM_WORLD, root=0) as executor:
        if executor is not None:
            print(list(executor.map(is_prime, range(150000000, 150001000))))
