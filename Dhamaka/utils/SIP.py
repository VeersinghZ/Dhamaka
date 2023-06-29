import platform
import os


class SIP:
    def __init__(self):
        self.os_name = None
        self.url = None
        self.navigate()

    def navigate(self):
        self.os_name = platform.system()

        if self.os_name == 'Windows':
            try:
                os.chdir('C:/Windows/System32/drivers/etc')
            except():
                raise PermissionError('Permission Denied!')
        else:
            print('OS not supported')

    def block_site(self, url, redirect_ip: str = '127.0.0.1'):
        self.url = url
        try:
            with open('hosts', 'a') as f:
                f.write(f'\n {redirect_ip} {self.url}')
        except():
            raise PermissionError('Permission Denied!')

    @staticmethod
    def unblock_site(self):
        try:
            # self.navigate()
            with open('hosts', 'r') as f:
                lines = f.readlines()
            updated_lines = []
            for line in lines:
                if self.url not in line:
                    updated_lines.append(line)
            with open('hosts', 'w') as f:
                f.writelines(updated_lines)
        except():
            raise PermissionError('Permission Denied!')
