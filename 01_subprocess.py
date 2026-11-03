import subprocess

result = subprocess.run(["git","status"])
print(result)
