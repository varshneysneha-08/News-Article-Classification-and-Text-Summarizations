import os
#new folder for the particular link
def creating_new_directory(directory):
    if not os.path.exists(directory):
        print('directory '+directory)
        os.makedirs(directory)

#Creating queue and crawled file fo the particular link keeps count of link to be crawled and already crawled link
def create_data_file(project_name,base_url):
    queue = project_name+'/queue.txt'
    crawled = project_name+'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

#function to append data in existing file
def append_to(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

#delete the content of a file
def delete_file_content(path):
    with open(path,'w') as file:
        pass
#convert file to set
def file_to_set(path):
    result=set()
    with open(path,'rt') as file:
        for line in file:
            result.add(line.replace('\n',''))
    return result

#again converting the set to the file
def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to(file,link)
