from crawler import *


def main():
    # Main function. It gets url from the user,
    # checks if it is a proper url and if approved, it calls crawling module
    if __name__ == '__main__':
        link = str()
        while not link.startswith('http'):
            # Checking if user gave proper url
            link = str(input('Paste base url to crawl in: '))
            if not link.startswith('http'):
                print(
                    'Please use proper url. It should start with "http", '
                    'and end with domain name (e.g. ".com")'
                )
                continue

        print(
            '############\n'
            'Extracted data will be stored in csv file called "data", '
            'which will be created in the project directory.\n'
            'Script is now running...\n############'
        )
        crawler(link)
        print("Task completed")


main()
