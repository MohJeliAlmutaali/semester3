import math

# Fungsi yang akan dihitung turunannya
def f(x):
    return 7 * math.exp(0.5 * x)

# Turunan analitis
def true_derivative(x):
    return 3.5 * math.exp(0.5 * x)

# Fungsi untuk menghitung pendekatan turunan
def approx_derivative(x, h):
    return (f(x + h) - f(x)) / h

# Nilai x dan h
x = 2.0  # Gantilah dengan nilai x yang sesuai
h = 0.3

# Hitung pendekatan turunan
approx_value = approx_derivative(x, h)

# Hitung true value (turunan sejati)
true_value = true_derivative(x)

# Hitung absolute relative error
absolute_relative_error = abs(approx_value - true_value) / abs(true_value)

# Cetak hasil
print("Pendekatan Turunan:", approx_value)
print("True Value Turunan:", true_value)
print("Absolute Relative Error:", absolute_relative_error)
