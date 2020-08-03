## Keyshare

Keyshare is tool to share a secret without sharing the secret over the network.
It is based on __(k, n) Threshold Scheme__ given in [How to Share a Secret](https://cs.jhu.edu/~sdoshi/crypto/papers/shamirturing.pdf), Shamir.

Use [polynomial interpolation over finite field](https://people.eecs.berkeley.edu/~daw/teaching/cs70-s08/notes/n10.pdf) to generate `k` points, these `k` points are used in future to generate a `k-1`
 degree polynomial from which the secret can be obtained.




### USAGE
- Create `K-POINTS`

    ```
    python3 keyshare.py -g <N> <K> <INPUT_file>
    ```
    - preferably <img src="https://render.githubusercontent.com/render/math?math=n=2*k-1">
    - `<input_file>` should have format similar to [this](./sample_files/input_file)
    - output file should look something like [this](./sample_files/k_points)

- Get Secret 
    ```
    python3 keyshare.py -s <K_POINTS_file>
    ```
    - `<K_POINTS_file>` should have format similar to [this](./sample_files/k_points)
    - output file should look something like [this](./sample_files/secret)

- Create More points
    ```
    python3 keyshare.py -m <K_POINTS_file>
    ```
    - `<K_POINTS_file>` should have format similar to [this](./sample_files/k_points)
    - output file should look something like [this](./sample_files/extra_points)


### NOTES
- it has been tested to work for secrets that are decimal numbers upto `2000 digits`, it does so in reasonable time `<30 sec`
