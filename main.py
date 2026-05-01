from parsers_csv import parsing_data
from services import timing


# sources_lst = ['POLUSDT-1m.csv', 'ARBUSDT-1m.csv', 'SUIUSDT-1m.csv', 'WIFUSDT-1m.csv']
sources_lst = ['POLUSDT-1m.csv']
@timing.timer
def main():
    for source in sources_lst:
        print(parsing_data.get_data(source))


main()
