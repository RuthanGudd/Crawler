import os


class Link():
    # Class that creates new object for each url

    # Class variable shared among all instances
    path = 'data.csv'

    def __init__(self, url, title='', internal_links=0, external_links=0, reference_count=0):
        self.url = url
        self.title = title
        self.internal_links = internal_links
        self.external_links = external_links
        self.reference_count = reference_count

    def set_title(self, title):
        self.title = title

    def count_internal_links(self):
        self.internal_links += 1

    def count_external_links(self):
        self.external_links += 1

    def count_reference(self):
        self.reference_count += 1

    def add_to_csv(self):
        # Function that add gathered data to csv file
        if not os.path.isfile(Link.path):
            # Check if file already exists, if not then create it
            with open(Link.path, 'w', encoding='utf-8') as file:
                # Set column names
                file.write(
                    'url,'
                    'title,'
                    'internal links count,'
                    'external links count,'
                    'reference count\n'
                )
                file.write(
                    f'{self.url}, {self.title}, {self.internal_links}, {self.external_links}, {self.reference_count}\n'
                )
        else:
            with open(Link.path, 'a', encoding='utf-8') as file:
                file.write(
                    f'{self.url}, {self.title}, {self.internal_links}, {self.external_links}, {self.reference_count}\n'
                )
