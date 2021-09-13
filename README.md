# DIY CRYPTO

A repository containing common encryption and key exchange algorithms and the mathematics behind them.

The implementations are grose simplifications and just demonstrate the basic logic of the algorithm.

## !!! DO NOT USE FOR PRODUCTION !!!

### Currently implemented algorithms
- Python
    - RSA key generation, ecryption and decryption

### Planned for future
- Python
    - Diffie-Hellmann key-exchange
    - Elliptic curve cryptography
    - DES
    - AES

- C++
    - RSA
    - Diffie-Hellmann key-exchange
    - Elliptic curve cryptography
    - DES
    - AES

## PyRSA

A naive implementation of RSA encryption using ~1000 first prime numbers for key generation
Encrypts and decrypts integers but it is rahter slow as the implementation of the mathematics isn't very clever right now...

Planned to implement a fixed message and key size and to optimize the mathematical functions.
- "Understanding Cryptography - Cristof Paar Chapter 7.5 Speed-up Techniques for RSA"
