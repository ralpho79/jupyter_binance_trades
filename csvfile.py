import csv

# list of dictionaries - lod
# list of lists - lol

def csv_to_lod(f):
    lst=[*csv.DictReader(open(f))]; return(lst)


def csv_to_lol(f):
    lst=[*csv.reader(open(f))]; return(lst)


def lod_to_csv(lod,name):

    f_columns = ['symbol','baseAsset','quoteAsset','status']

    with open(name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = f_columns)
        writer.writeheader()
        for data in lod:
            writer.writerow(data)

    print('CSV file overwritten.')


def lol_to_csv(lol,name):
    
    with open(name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(lol)

    #print('CSV file overwritten.')

if __name__ == "__main__":
    print("This was run as a script. No action.")