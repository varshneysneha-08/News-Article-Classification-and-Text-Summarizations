import requests
import re
from bs4 import BeautifulSoup
import threading
import pandas as pd
import queue

def file_to_queue(file_name):
    url_queue=queue.Queue()
    with open(file_name,'rt') as file:
        for line in file:
            url_queue.put(line.replace('\n',''))
    return url_queue

url_queue=file_to_queue('/content/drive/MyDrive/Colab Notebooks/crawling and scraping/pol_queue.txt')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://theprint.in/',
    'Accept-Language': 'en-US'
}
lists=[]
def worker():
    while True:
        url=url_queue.get()
        if url is None:
            break
        try:
            response = requests.get(url, headers=headers)
            if(response.status_code==200):
                soup = BeautifulSoup(response.text, "html.parser")
                # Remove <video>, <img>, <tag>, and <footer> tags
                for tag in soup.find_all(['video', 'img', 'tag','head','footer','script','style','header','table']):
                    tag.extract()

                # Get the text and remove spaces and newlines
                text = ' '.join(soup.stripped_strings)

                extra_spaces_to_remove = re.compile(r'\s+')

                text = extra_spaces_to_remove.sub(' ', text)

                # Convert text to lowercase
                text = text.lower()

                # Remove empty lines
                lines = text.split('\n')
                non_empty_lines = [line.strip() for line in lines if line.strip()]
                text = '\n'.join(non_empty_lines)
                print(threading.current_thread().name+" now scarping "+ url)
                
                lists.append(text)
                # print(str(url_queue.qsize))
                # print(text)

        except Exception as e:
            print("error occuring in scraping")
            print("Error:", str(e))
        # mark task as done
        url_queue.task_done()

no_of_threads=8
threads=[]

for _ in range(no_of_threads):
    thread=threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

for _ in range(no_of_threads):
    url_queue.put(None)

for thread in threads:
    thread.join()
df=pd.DataFrame({"article":lists})
df.to_csv("pol2.csv", escapechar='\\')
print("scraping done")