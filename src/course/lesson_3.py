import numpy as np

if __name__ == "__main__":
    # Create a numpy array from Python list.
    # print(np.array([1, 2, 3]))
    # print(np.array([[1, 2, 3], [4, 5, 6]]))

    # Create an empty numpy array.
    # The values will be whatever is in the memory at that location.
    # print(np.empty(5))
    # print(np.empty((2, 3)))

    # A numpy array of 1s.
    # print(np.ones(5))

    # A numpy array of 0s.
    # print(np.zeros((2, 3)))

    # A numpy array of 1s as ints.
    print(np.ones(5, dtype=int))

    # A numpy array of random numbers, uniformly sampled from [0, 1).
    print(np.random.random((2, 3)))
    # Same as above, just different syntax.
    print(np.random.rand(2, 3))

    # A numpy array of random numbers, sampled from normal (Gaussian) distribution.
    # mean = 0, standard deviation = 1.
    print(np.random.normal(size=(2, 3)))
    # mean = 100, standard deviation = 10.
    print(np.random.normal(100, 10, size=(2, 3)))

    # A numpy array of random integers, uniformly sampled from [0, 10).
    print(np.random.randint(0, 10, size=(2, 3)))

    a = np.array([[1, 2, 3], [4, 5, 6]])
    # Print the shape of the array.
    print(a.shape)
    # Print the number of dimensions of the array.
    print(a.ndim)
    # Print the total number of elements of the array.
    print(a.size)
    # Print the data type of the array.
    print(a.dtype)
