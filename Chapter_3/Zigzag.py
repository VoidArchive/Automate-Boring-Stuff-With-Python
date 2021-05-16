import time
import sys
indent = 0  # how many spaces to indent
indentIncreasing = True  # Whether the indentation is increasing or not.

try:
    while True:
        print(' ' * indent, end='')
        print('ANISH')
        time.sleep(0.1)  # Pause for 1/10 of a second

        if indentIncreasing:
            # Incresing the number of spaces
            indent += 1
            if indent == 20:
                # Change direction
                indentIncreasing = False

        else:
            # Decresing the number of spaces
            indent -= 1
            if indent == 0:
                # change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
