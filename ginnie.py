import pty
import os
import select
import sys

def main():
    master_fd, slave_fd = pty.openpty()

    try:
        while True:
            rlist, _, _ = select.select([sys.stdin, master_fd], [], [])

            if sys.stdin in rlist:
                user_input = sys.stdin.readline().encode()
                os.write(slave_fd, user_input)

            if master_fd in rlist:
                output = os.read(master_fd, 4096)
                sys.stdout.write(output.decode())
                sys.stdout.flush()
    finally:
        os.close(master_fd)
        os.close(slave_fd)

if __name__ == "__main__":
    main()
