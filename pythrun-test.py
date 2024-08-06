import sys
import time

def main():
    # First set: 5 lines of stdout
    print("Expected: 5 lines of stdout - 1st set")
    for i in range(1, 6):
        print(f"stdout: Line {i}")
        time.sleep(0.2)

    # Second set: 5 lines of stderr
    print("Expected: 5 lines of stderr - 2nd set", file=sys.stderr)
    for i in range(1, 6):
        print(f"stderr: Line {i}", file=sys.stderr)
        time.sleep(0.2)

    # Third set: 5 interleaved lines of stdout and stderr
    print("Expected: 5 interleaved lines of stdout and stderr - 3rd set")
    for i in range(1, 6):
        print(f"stdout: Interleaved Line {i}")
        print(f"stderr: Interleaved Line {i}", file=sys.stderr)
        time.sleep(0.1)

    # Fourth set: Character by character output with pauses
    print("Expected: Character by character output with pauses - 4th set")
    for char in "stdout: Character output\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    for char in "stderr: Character output\n":
        sys.stderr.write(char)
        sys.stderr.flush()
        time.sleep(0.05)

    print("Exiting with code 42")
    sys.exit(42)

if __name__ == "__main__":
    main()
