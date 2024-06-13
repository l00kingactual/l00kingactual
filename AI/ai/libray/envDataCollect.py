import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def main():
    commands = [
        'python --version',
        'where python',
        'pip list',
        'echo %VIRTUAL_ENV%',
        'python -m site'
    ]

    with open("environment_info.txt", "w") as f:
        for command in commands:
            stdout, stderr = run_command(command)
            print(f"Command: {command}")
            print(f"Output:\n{stdout}")
            print(f"Error:\n{stderr}")

            f.write(f"Command: {command}\n")
            f.write(f"Output:\n{stdout}\n")
            f.write(f"Error:\n{stderr}\n")
            f.write("="*50 + "\n")

    # Check for import errors
    modules_to_check = [
        "tensorflow.keras.optimizers",
        "qiskit.providers.aer"
    ]

    with open("import_errors.txt", "w") as f:
        for module in modules_to_check:
            try:
                __import__(module)
                print(f"Successfully imported {module}")
                f.write(f"Successfully imported {module}\n")
            except ImportError as e:
                print(f"Failed to import {module}: {e}")
                f.write(f"Failed to import {module}: {e}\n")

if __name__ == "__main__":
    main()
