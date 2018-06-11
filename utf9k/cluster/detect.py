import glob

from utf9k.settings import Constants


def content_scan(base_dir=Constants.CONTENT_DIR,
                 folders=Constants.DIRECTORIES,
                 extensions=Constants.EXTENSIONS):
    files = list()
    content = glob.glob(f'{base_dir}/**/*')
    for folder in folders:
        for item in content:
            for extension in extensions:
                if folder in item and extension in item:
                    files.append(item)
    return files


def content_type(file_path):
    if 'articles' in file_path:
        return 'article'
    if 'projects' in file_path:
        return 'project'
    if 'reviews' in file_path:
        return 'review'
    if 'snippets' in file_path:
        return 'snippet'
    if 'bites' in file_path:
        return 'bite'
