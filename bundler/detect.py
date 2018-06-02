import glob

from bundler.settings import Constants


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
