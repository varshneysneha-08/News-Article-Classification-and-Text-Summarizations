import threading
from queue import Queue
from spider import spider
from link_finder import *
from domain import *
from general import *

PROJECT_NAME='education'
HOMEPAGE='https://sport360.com/'
DOMAINNAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE= PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=8
queue=Queue()
spider(PROJECT_NAME,HOMEPAGE,DOMAINNAME)

#create worker threads die when main exit
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()
#do the next job in queue
def work():
    while True:
        url=queue.get()
        spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

#each queued links is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
    crawl()


def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links))+' links in the queue')
        create_jobs()

create_workers()
crawl()