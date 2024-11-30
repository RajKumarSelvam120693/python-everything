import threading
from bs4 import BeautifulSoup
import requests

urls =['https://stackoverflow.com/questions/11947587/is-there-a-naming-convention-for-git-repositories',
       'https://stackoverflow.com/questions/24244908/change-naming-convention-of-tags-inside-a-git-repository?rq=3',
       'https://stackoverflow.com/questions/852943/how-can-i-change-the-tag-given-when-using-git-describe?rq=3']

def fetch_content(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.content, 'html.parser')
       print(f"Fetched {len(soup.text)} characters from '{url}'")

threads = []
for url in urls:
       thread = threading.Thread(target=fetch_content, args=[url])
       thread.start()
       threads.append(thread)

for thread in threads:
       thread.join()

