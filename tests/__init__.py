import subprocess


def shell(command, cwd=None, raise_exception=True):
    "execute shell command"
    process = subprocess.Popen(command, stderr=subprocess.STDOUT,
                               stdout=subprocess.PIPE, shell=True,
                               cwd=cwd, env=env)

    lines = []
    for line in iter(process.stdout.readline, b""):
        line = line.rstrip().decode("utf8")
        lines.append(line)

    process.communicate()
    output = "\n".join(lines)
    if process.returncode and raise_exception:
        raise Exception(f"failed to run command: {command} return_code \
                        {process.returncode} content: {output}")

    return process.returncode, output
