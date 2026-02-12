import subprocess


class Client:
    login : str
    passwd : str
    def __init__(self, name: str, passwd :str, host: str):
        self.name = name
        self.passwd = passwd
        self.host = host
    def connect(self):
        ssh_command = f"ssh {self.name} {self.passwd}"
        process = subprocess.Popen([
            'gnome-terminal',
            '--',
            'bash',
            '-c',
            ssh_command
        ])
        print("Окно открыто, а я работаю дальше!")
        return process

if __name__ == "__main__":
    file = open("localhost.txt")
    cmd = file.readlines()
    client1 = Client(cmd[0], cmd[1], cmd[2])
    client1.connect()