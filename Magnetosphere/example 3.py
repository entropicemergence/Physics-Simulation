import numpy
import time
start_time = time.time()

a = numpy.array(range(5*10**7), dtype=numpy.float32)
b = numpy.array(range(5*10**7), dtype=numpy.float32)

c=10*a+ b+(a*b)+(a*b)/1000+(a*b)*0.001+(a*b)

print c
print("--- %s seconds ---" % (time.time() - start_time))

# --- 13.3980000019 seconds ---
# --- 11.611000061 seconds ---
# --- 11.9240000248 seconds ---
# --- 11.1859998703 seconds ---
# --- 12.0460000038 seconds ---
