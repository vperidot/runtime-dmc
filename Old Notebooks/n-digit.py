import numpy as np
import zipfile

def npz_headers(npz):
    with zipfile.ZipFile(npz) as archive:
        for name in archive.namelist():
            if not name.endswith('.npy'):
                continue
            npy = archive.open(name)
            version = np.lib.format.read_magic(npy)
            shape, fortran, dtype = np.lib.format._read_array_header(npy, version)
            print(name, shape, fortran, dtype)

npz_headers('dataset_mnist_2_number_test_seen.npz')

# print(one)