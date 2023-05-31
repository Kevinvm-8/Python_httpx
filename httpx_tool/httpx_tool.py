import subprocess

class ToolHTTPX:
    def __init__(self, subdomains):
        self.subdomains = subdomains

    def enumerate_subdomains(self):
        httpx_command = ['httpx', '-status-code']
        httpx_output = subprocess.check_output(httpx_command, universal_newlines=True)
        self.subdomains = list(set(httpx_output.strip().splitlines()))
        print(self.subdomains)
        for subdomain in self.subdomains:
            try:
                httpx_command_https = httpx_command + [f"https://{subdomain}/"]
                # httpx_output_https = subprocess.check_output(httpx_command_https, stderr=subprocess.STDOUT, universal_newlines=True)
                if any(response.startswith(("2", "3")) for response in httpx_command_https.strip().split('\n')):
                    print(f"Subdomain {subdomain} (HTTPS) is live.")
                    subdomain.append(f"https://{subdomain}")
                else:
                    print(f"Subdomain {subdomain} (HTTPS) is dead.")
                    subdomain.append(f"https://{subdomain}")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred for subdomain {subdomain}")

    def get_unique_subdomains(self):
        return self.subdomains

