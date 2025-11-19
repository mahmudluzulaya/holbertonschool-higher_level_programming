#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"

    # .pyc faylını aç və header-ı skip et
    with open(pyc_file, "rb") as f:
        f.read(16)  # header hissəsini oxu
        code = marshal.load(f)  # code object oxu

    # boş bir module yaradıb code object-i icra et
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    # module içindəki adları al və __ ilə başlamayanları çap et
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
