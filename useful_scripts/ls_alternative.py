import sys
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

file_types = {
        'py' : '',
        'c' : '',
        'cpp': '',
        'h' : '',
        'vim': '',
        'css': '',
        'html': '',
        'js': '',
        'ts': 'ﯤ',
        'mp3': '',
        'mp4': '',
        'txt': '',
        'jsx': '',
        'tsx': '',
        'hs': '',
        'java': '',
        'exe': '',
        'dmg': '',
        'go': ''
        }

def main(path=""):
     all_files_in_current_dir = os.listdir(path)

     for file in all_files_in_current_dir:
        # print(file, end="\t")
        if(os.path.isdir("{}/{}".format(path, file))):
            print(bcolors.OKCYAN + " {}".format(file), end="\t" + bcolors.ENDC)
        else:
            if(file.split(".")[-1] in file_types): 
                print("{} {}".format(file_types[file.split(".")[-1]], file), end="\t") 
            else:
                print("{} {}".format('', file), end="\t")

     print("")


if __name__ == "__main__":
    main(os.getcwd())

