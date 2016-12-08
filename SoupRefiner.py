# -*- coding: utf-8 -*-

"""
SoupRefiner
~~~~~~~~~~~~~~~~~~~~~~~~

SoupRefiner is a links parser in Python

~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
    import SoupRefiner
    sr = SoupRefiner(soup_obj, starting_url)
    internal_links = sr.get_internal_links

    external_links = sr.get_external_links

    """

from urllib import parse

__title__ = 'SoupRefiner'
__author__ = 'LMarTinnnn'


class SoupRefiner(object):
    def __init__(self, soup, starting_url):
        self.soup = soup
        self.starting_url = starting_url
        self.all_links = self.get_links()

    def get_links(self):
        links = set()
        for link in self.soup.findAll('a'):
            href = link.get('href', False)
            if href:
                links.add(href)
        return links

    def get_internal_links(self):
        """
        :return: return a list of internal links in a web page
        """

        # 获得协议和域名组成的url用于下面的内链检测 和 不完整url的完整化
        p = parse.urlparse(self.starting_url)
        include_url = '%s://%s' % (p.scheme, p.netloc)

        internal_links = set()
        all_links = self.all_links
        for link in all_links:
            if include_url in link:
                internal_links.add(link)
            elif link.startswith('/'):
                complete_link = include_url + link
                internal_links.add(complete_link)
        return internal_links

    def get_external_links(self):
        """
        :return: return a list of external links in a web page
        """
        p = parse.urlparse(self.starting_url)
        exclude_url = '%s://%s' % (p.scheme, p.netloc)

        external_links = set()
        all_links = self.all_links

        for link in all_links:
            # 正则还要好好深入啊 这样实在太麻烦了
            if link.startswith('www') or link.startswith('http') or link.startswith('https'):
                if exclude_url not in link:
                    external_links.add(link)

        return external_links
