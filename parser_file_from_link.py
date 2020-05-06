import requests
from bs4 import BeautifulSoup
import io, zipfile

# to download and extract zip files to new folder output.
def download_zip(url_txt):
    for url in url_txt:
        response = requests.get(url)
        # print(type(response.content))
        if zipfile.is_zipfile(io.BytesIO(response.content)):
            with response, zipfile.ZipFile(io.BytesIO(response.content)) as archive:
                archive.extractall('output')





def trade_spider(max_pages, url):
    url_download = []
    page = 1
    while page <= max_pages:
        # url = 'https://www.rulit.me/books/es/' + str(page) + '/date'
        # take request object from webserver url
        source_code = requests.get(url)
        # print(type(source_code))  to see the type of the object
        # print(source_code.content)   - to see content of request object
        # convert request object to string, using .text method of REQUEST module
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select("#program_name"):
            href = link.a.get('href')
            # this .text is method of Bs4, to get text into link
            linker = href[-11:-5]
            # linker2 = href[:-25] + 'get' + href[-12:]
            download_link = 'https://www.rulit.me/download-books-563183.html?t=txt'
            url_download.append(download_link[:-17] + linker + download_link[-11:])
        page += 1
    return url_download
    # get_single_item_data(linker2)

def main():
    page = 1
    url = 'https://www.rulit.me/books/es/' + str(page) + '/date'
    download_zip(trade_spider(page, url))

if __name__ == '__main__':
    main()

# # func to go deeper on the next level. I don't use it in this problem
# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     # print(type(source_code))  to see the type of the object
#     # print(source_code.content)   - to see content of request object
#     # convert request object to string, using .text method of REQUEST module
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text, 'lxml')
#     for item_name in soup.findAll('h1'):
#         title = item_name.string
