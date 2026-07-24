#       Python Program for executing multiple OS system calls
# code by tany ranka sycse b 8

import os
import sys

print()

file_opener = open("file.log", "w")
file_opener.write("Hello from python code\n")
status = os.stat("file.log")
print(status)

file_opener.close()
print(f"\n {os.uname()}\n")


command = "print('executed by using the exec() function')"
exec(command)


#pipe to the child process
read_buffer, write_buffer = os.pipe()
pid = os.fork()

if pid == 0:
    os.close(read_buffer)
    print(f"Child process initiated with PID: {os.getpid()}")
    message = "Hello from Child Process\n".encode()
    os.write(write_buffer, message)
    os.close(write_buffer)

else:
    os.close(write_buffer)
    sys.stdout.write("Hello from parent process       ")
    print(f"Hello from parent process with PID {os.getppid()}")

    buffer = os.read(read_buffer, 1024)
    print(buffer.decode())
    os.close(read_buffer)

exit()
