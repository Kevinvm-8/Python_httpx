import subprocess


class ToolHTTPX:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = []

    def enumerate_subdomains(self):
        subfinder_command = ['subfinder', '-d', self.domain]
        httpx_command = ['httpx', '-title', '-tech-detect', '-status-code', '-title', '-follow-redirects']
        try:
            subfinder_output = subprocess.check_output(subfinder_command, universal_newlines=True)
            subdomains = list(set(subfinder_output.strip().split('\n')))
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the subfinder command: {e.output.strip()}")
            return

        for subdomain in subdomains:
            try:
                httpx_command[-1] = subdomain
                httpx_output = subprocess.check_output(httpx_command, universal_newlines=True)
                httpx_output = httpx_output.strip().split('\n')
                status_code= httpx_output[0].split()[1]
                if status_code.startswith("2") or status_code.startswith("3"):
                    print(f"Subdomain {subdomain} is live.")
                else:
                    print(f"Subdomain {subdomain} is dead.")
                self.subdomains.append(subdomain)
            except subprocess.CalledProcessError:
                print(f"An error occurred for subdomain {subdomain}.")

    def get_unique_subdomains(self):
        return self.subdomains