from httpx_tool import ToolHTTPX

def main():
    domain = "bugcrowd.com"

    tool = ToolHTTPX(domain)
    tool.enumerate_subdomains()

    unique_subdomains = tool.get_unique_subdomains()
    print("Unique subdomains:")
    for subdomain in unique_subdomains:
        print(subdomain)

if __name__ == "__main__":
    main()
