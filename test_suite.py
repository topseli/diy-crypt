from random import randint
from PyRSA.rsa_suite import rsa_suite
from PyRSA.logger import info, error
# PyRSA tests

RSA_test = rsa_suite()

for i in range(10):
    RSA_input = randint(1, 1024)
    info("Test # %d Input: %d" % (i + 1, RSA_input))
    RSA_test.generate_keys()
    encrypted = RSA_test.rsa_encrypt(RSA_input, RSA_test.public_key)
    RSA_output = RSA_test.rsa_decrypt(encrypted, RSA_test.private_key)

    if RSA_input != RSA_output:
        error("Decrytping message failed")
