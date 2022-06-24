import numpy as np

if __name__ == "__main__":
    print("Create a numpy array from Python list")
    print(np.array([1, 2, 3]))
    print(np.array([[1, 2, 3], [4, 5, 6]]))

    print("Create an empty numpy array")
    # The values will be whatever is in the memory at that location.
    print(np.empty(5))
    print(np.empty((2, 3)))

    print("A numpy array of 1s")
    print(np.ones(5))

    print("A numpy array of 0s")
    print(np.zeros((2, 3)))

    print("A numpy array of 1s as ints")
    print(np.ones(5, dtype=int))

    print("A numpy array of random numbers, uniformly sampled from [0, 1)")
    print(np.random.random((2, 3)))
    # Same as above, just different syntax.
    print(np.random.rand(2, 3))

    print(
        "A numpy array of random numbers, sampled from normal (Gaussian) distribution"
    )
    # mean = 0, standard deviation = 1.
    print(np.random.normal(size=(2, 3)))
    # mean = 100, standard deviation = 10.
    print(np.random.normal(100, 10, size=(2, 3)))

    print("A numpy array of random integers, uniformly sampled from [0, 10)")
    print(np.random.randint(0, 10, size=(2, 3)))

    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("Shape of the array:", a.shape)
    print("Number of dimensions of the array:", a.ndim)
    print("Total number of elements of the array:", a.size)
    print("Data type of the array:", a.dtype)

    # Seed the random number generator so that
    # it always generates the same sequence of numbers.
    np.random.seed(123)
    print("A numpy array of random integers (3x4), uniformly sampled from [0, 10)")
    a = np.random.randint(0, 10, size=(3, 4))
    print(a)

    print("Sum of all elements in the array:", a.sum())
    print("Min values in each column", a.min(axis=0))
    print("Max values in each row", a.max(axis=1))
    print("Mean of all elements in the array", a.mean())

    # NOTE: `argmax` returns the index of the first max value as if the array is 1 dimensional.
    # `unravel_index` is then used to find the coordinate in the matrix.
    print("Index of the max value in the array:", np.unravel_index(a.argmax(), a.shape))

    # Access the elements of the array.
    print("a[1, 2] = ", a[1, 2])
    print("a[1:3, 2:4] = ", a[1:3, 2:4])

    # Change the values of the array.
    print("Set a[1, 2] to 100")
    a[1, 2] = 100
    print(a)

    print("Set a[2, :] to -1")
    a[2, :] = -1
    print(a)

    print("Set a[:-1, -1] to 1000")
    a[:-1, -1] = 1000
    print(a)

    print("Set a[1, :] to [1, 2, 3, 4]")
    a[1, :] = [1, 2, 3, 4]
    print(a)

    a = np.random.randint(0, 100, size=10)
    print(a)

    print("Indexing an array a with array [7, 3, 1]")
    indices = [7, 3, 1]
    print(a[indices])

    # Boolean array indexing.
    mean = a.mean()
    print("Mean:", mean)

    print("Values less than the mean:", a[a < mean])

    print("Set values less than the mean to -1")
    a[a < mean] = -1
    print(a)

    # Arithmetic operations.
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("a")
    print(a)

    b = np.array([[10, 20, 30], [40, 50, 60]])
    print("b")
    print(b)

    c = np.array([[100, 200], [300, 400], [500, 600]])
    print("c")
    print(c)

    print("a * 2")
    print(a * 2)

    print("a / 2")
    print(a / 2)

    print("a / 2.0")
    print(a / 2.0)

    print("a + b")
    print(a + b)

    print("a - b")
    print(a - b)

    print("a * b")
    print(a * b)

    print("a / b")
    print(a / b)

    print("a • c")
    print(a.dot(c))
