import os


# Each Site You Crawl is a Different Project(Folder)
def create_new_project_dir(directory):
    if not os.path.exists(directory):
        print(f'Creating {directory} ...')
        os.makedirs(directory)


# Creating Queue and Crawled Files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create Data
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Append Data
def append_data_to_files(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete Content The File
def delete_file_content(path):
    with open(path, 'w'):
        pass


# Convert file to set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


def set_to_file(links, file):
    delete_file_content(file)

    for link in links:
        append_data_to_files(file, link)
