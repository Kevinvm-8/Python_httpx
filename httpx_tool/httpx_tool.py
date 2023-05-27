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
            print(f"An error occurred while running the subfinder command: {str(e)}")
            return

        for subdomain in subdomains:
            try:
                httpx_command[-1] = subdomain
                httpx_output = subprocess.check_output(httpx_command, universal_newlines=True)
                httpx_output = httpx_output.strip().split('\n')
                if "200 OK" in httpx_output:
                    print(f"Subdomain {subdomain} is live.")
                else:
                    print(f"Subdomain {subdomain} returned a non-200 status code.")
            except subprocess.CalledProcessError:
                print(f"An error occurred for subdomain {subdomain}.")

    def get_unique_subdomains(self):
        return self.subdomains
