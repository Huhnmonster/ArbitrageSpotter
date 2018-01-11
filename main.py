from Source import Compare
import time

init_statement = """
#####################################
# Initiated ArbSpot! Happy hunting! #
#####################################"""

print(init_statement)

compare = Compare.Compare()

try:
    start = time.time()
    while True:
        compare.compare_prices()
        time.sleep(60.0 - ((time.time() - start) % 60.0))
except KeyboardInterrupt:
    print("Keyboard Interrupt detected! Exiting now...")