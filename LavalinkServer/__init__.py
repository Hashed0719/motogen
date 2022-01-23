import os
import threading
import subprocess
import asyncio

def invoke_at(path: str):
    def parameterized(func):
        def wrapper(*args, **kwargs):
            cwd = os.getcwd()
            os.chdir(path)

            try:
                ret = func(*args, **kwargs)
            finally:
                os.chdir(cwd)

            return ret

        return wrapper

    return parameterized         
cwdpath = os.getcwd()
# print(path)
path = os.path.join(cwdpath,"LavalinkServer")
print(path)

@invoke_at(path)
def start_LavalinkServer():
    subprocess.Popen("java -jar Lavalink.jar")



if __name__ == "__main__":
    start_LavalinkServer()
