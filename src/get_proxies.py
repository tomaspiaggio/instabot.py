import re
import requests
import time
import lxml.html as lh

class ProxyProvider(object):
    def __init__(self, time_until_refresh):
        self.proxies = []
        self.time_until_refresh = time_until_refresh

    def next(self):
        raise ValueError('This class should not be used, implement a subclass for each website')

    def refresh(self):
        raise ValueError('This class should not be used, implement a subclass for each website')


class SSLProxyProvider(ProxyProvider):
    def __init__(self, time_until_refresh=60 * 5): # updates after 5 minutes
        ProxyProvider.__init__(self, time_until_refresh + int(time.time())) 
        self.current = 0
        self.refresh()

    def next(self):
        if self.time_until_refresh < time.time():
            self.refresh()
        aux = self.current
        self.current += 1
        return self.proxies[aux % len(self.proxies)]

    def refresh(self):
        def remove_countries(tup):
            first = re.match('[1-9.]+', tup[0])
            second = re.match('[1-9.]+', tup[1])
            return first is not None and second is not None

        def clean_cols(col):
            ips = col[0][1]
            ports = col[1][1]
            ips_with_ports = zip(ips, ports)
            ips_with_ports = filter(remove_countries, ips_with_ports)
            return map(lambda tup: '{}:{}'.format(tup[0], tup[1]), ips_with_ports)

        def get_table_elements(url):
            page = requests.get(url)
            doc = lh.fromstring(page.content)
            return doc.xpath('//tr')

        def get_headers(tf_elements):
            col = []
            i = 0
            for t in tr_elements[0]:
                name=t.text_content()
                col.append((name,[]))
                i += 1

            return col
        
    
        tr_elements = get_table_elements('https://www.sslproxies.org/')
        col = get_headers(tr_elements)

        # appending data to each header
        j = 0
        for element in tr_elements:
            if j is not 0:
                i = 0
                for t in element:
                    col[i][1].append(t.text_content())
                    i += 1
            j += 1

        self.proxies = list(clean_cols(col))
        self.current = 0