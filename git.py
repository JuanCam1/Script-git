import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    # Tipos de commit recomendados (Convencional Commits)
    types = ["fix", "feat", "chore", "style", "refactor", "test", "docs"]

    print("Seleccione el tipo de commit:")
    for i, t in enumerate(types, start=1):
        print(f"{i}. {t}")

    choice = int(input("Número del tipo: "))
    commit_type = types[choice - 1] if 1 <= choice <= len(types) else "chore"

    # Mensaje del commit
    message = input("Mensaje del commit: ")

    # Ejecutar git add .
    run_command("git add .")

    # Ejecutar git commit
    commit_command = f'git commit -m "{commit_type}: {message}"'
    run_command(commit_command)

    # Ejecutar git push
    run_command("git push origin main")

if __name__ == "__main__":
    main()
