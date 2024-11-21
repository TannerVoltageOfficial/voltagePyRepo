import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

print("Welcome to the Python Bash Terminal")
print("Type 'exit' to quit")

while True:
    command = input("$ ")
    if command.lower() == 'exit':
        break
    output = run_command(command)
    print(output)

print("Goodbye!")