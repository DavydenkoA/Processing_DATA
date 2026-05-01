import os
from parsers_csv import parsing_data
from services import timing

directory = r'C:\Web\Python\DATA\sources'
sources_lst = [os.path.join(directory, file) for file in os.listdir(directory)]


@timing.timer
def main():
    for source in sources_lst:
        print(parsing_data.get_data(source))


main()
