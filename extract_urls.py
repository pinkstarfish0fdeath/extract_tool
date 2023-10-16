import re
import sys

def extract_urls_and_domains(file_path):
  """Extracts all URLs and domains from a file using regex.

  Args:
    file_path: The path to the file to extract URLs and domains from.

  Returns:
    A list of all URLs and domains extracted from the file.
  """

  urls_and_domains = []

  with open(file_path, "r") as f:
    for line in f:
      # Extract all URLs from the line.
      urls = re.findall(r"(https?://[^\s]+)", line)

      # Extract all domains from the URLs.
      domains = [re.search(r"(?:https?://)?(?P<domain>[^\s/]+)", url).group("domain") for url in urls]

      # Add the URLs and domains to the list.
      urls_and_domains.extend(urls)
      urls_and_domains.extend(domains)

  return urls_and_domains

if __name__ == "__main__":
  # Get the file path from the command line arguments.
  file_path = None
  for arg in sys.argv:
    if arg == "-f":
      file_path = sys.argv[sys.argv.index(arg) + 1]

  # If no file path was provided, print an error message and exit.
  if file_path is None:
    print("Usage: python extract_urls_and_domains.py -f <file_path>")
    exit(1)

  # Extract all URLs and domains from the file.
  urls_and_domains = extract_urls_and_domains(file_path)

  # Print the URLs and domains to the console.
  for url_or_domain in urls_and_domains:
    print(url_or_domain)
