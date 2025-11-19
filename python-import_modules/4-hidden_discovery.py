#!/usr/bin/python3
import dis
import marshal
import types

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"

    with open(pyc_file, "rb") as f:
        f.read(16)  # Skip header
        code = marshal.load(f)

    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
