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

    # Seed the random number generator so that
    # it always generates the same sequence of numbers.
    np.random.seed(123)
    a = np.random.randint(0, 10, size=(3, 4))
    print(a)

    # Print the sum of all elements in the array.
    print(a.sum())
    # Print the min values in each column.
    print(a.min(axis=0))
    # Print the max values in each row.
    print(a.max(axis=1))
    # Print the mean of all elements in the array.
    print(a.mean())

    # Print the index of the max value in the array.
    # NOTE: `argmax` returns the index of the first
    # max value as if the array is 1 dimensional.
    # `unravel_index` is then used to find the
    # coordinate in the matrix.
    print(np.unravel_index(a.argmax(), a.shape))

    # Access the elements of the array.
    print(a[1, 2])
    print(a[1:3, 2:4])

    # Change the values of the array.
    a[1, 2] = 100
    print(a)
    a[2, :] = -1
    print(a)
    a[:-1, -1] = 1000
    print(a)
    a[1, :] = [1, 2, 3, 4]
    print(a)

    # Indexing an array with another array.
    b = np.random.randint(0, 100, size=10)
    print(b)
    indices = [7, 3, 1]
    print(b[indices])

    # Boolean array indexing.
    mean = b.mean()
    print(mean)
    # Returns an array of all values that are less than the mean.
    print(b[b < mean])
    # Assigns all values that are less than the mean to -1.
    b[b < mean] = -1
    print(b)
