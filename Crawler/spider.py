from urllib.request import urlopen
from general import *
from link_finder import linkfinder
from domain import *
class spider:
    #class variables(shared among all instanses)
    #text files are made so data can be stored even after we stop our program
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()
    def __init__(self,project_name,base_url,domain_name):
        spider.project_name=project_name
        spider.base_url=base_url
        spider.domain_name=domain_name
        spider.queue_file=spider.project_name+'/queue.txt'
        spider.crawled_file=spider.project_name+'/crawled.txt'
        #function for first spider that's why self
        self.boot()
        self.crawl_page('first spider',spider.base_url)

    @staticmethod
    def boot():
        creating_new_directory(spider.project_name)
        create_data_file(spider.project_name,spider.base_url)
        spider.queue=file_to_set(spider.queue_file)
        spider.crawled=file_to_set(spider.crawled_file)
        
    @staticmethod
    def crawl_page(threadname,page_url):
        if page_url not in spider.crawled:
            print(threadname+'now crawling'+page_url)
            print('Queue '+str(len(spider.queue))+' | '+'Crawled '+str(len(spider.crawled)))
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_files()
        else:
            print('already crawled')

    @staticmethod
    def gather_links(page_url):
        html_string=''
        try:
            # print('hi')
            response= urlopen(page_url)
            content_type = response.getheader('Content-Type')
            if content_type and 'text/html' in content_type.lower():
                html_bytes=response.read()
                html_string=html_bytes.decode("utf-8")      
            finder=linkfinder(spider.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Can not crawl page')
            return set()
        return finder.page_link()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            # if spider.domain_name not in url:
            #     continue
            if get_domain_name(url) != spider.domain_name:
                continue
            spider.queue.add(url)
    @staticmethod
    def update_files():
       set_to_file(spider.queue,spider.queue_file)
       set_to_file(spider.crawled,spider.crawled_file)
    

