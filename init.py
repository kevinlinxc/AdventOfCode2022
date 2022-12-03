# creates all .txt and .py files
import os
inputs_dir = "inputs"
for i in range(1, 26):
    inputs_path = os.path.join(inputs_dir, f"{i}.txt")
    if not os.path.exists(inputs_path):
        with open(inputs_path, "a") as f:
            f.write("")
    if not os.path.exists(f"{i}.py"):
        with open(f"{i}.py", "w") as f:
            f.write("import fileinput\n")
            f.write(f"lines = [line.strip() for line in fileinput.input(files=\"inputs/{i}.txt\")]")
