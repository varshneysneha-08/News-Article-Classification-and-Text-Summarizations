from urllib.parse import urlparse

#get main domain(newboston.com)
def get_domain_name(url):
    try:
        results= get_subdomain_name(url).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''
        
#get subdomain name(name.hi.thenewboston.com)
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
 