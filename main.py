from ArbitrageSpotter import Compare
import time

init_statement = """
#####################################
# Initiated ArbSpot! Happy hunting! #
#####################################
"""

print(init_statement)

compare = Compare.Compare()

try:
    start = time.time()
    while True:
        benchmark_begin = time.time()
        compare.compare_prices()
        benchmark_end = time.time()
        print(benchmark_end-benchmark_begin)
        time.sleep(30.0 - ((time.time() - start) % 30.0))
except KeyboardInterrupt:
    print("Keyboard Interrupt detected! Exiting now...")