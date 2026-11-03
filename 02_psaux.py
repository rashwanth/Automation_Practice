import subprocess

processes = subprocess.run(["ps","aux"], capture_output=True, text=True)

lines = processes.stdout.splitlines()

zombies = []

for line in lines[1:]:
	fields = line.split(None, 10)
	pid, stat = fields[1],fields[7]
	if stat.startswith("Z"):
		zombies.append(pid)

print(zombies)
