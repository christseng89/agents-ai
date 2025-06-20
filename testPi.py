# Calculate pi using Leibniz series with 10,000 terms

def compute_pi_leibniz(n_terms=10000):
    result = 0.0
    for i in range(n_terms):
        term = (-1)**i / (2 * i + 1)
        result += term
    return 4 * result

if __name__ == "__main__":
    pi_approx = compute_pi_leibniz(10000)
    print(f"Approximation of π using 10,000 terms: {pi_approx}")
