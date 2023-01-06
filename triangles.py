# load the file - pairs with currencies
# https://blog.finxter.com/convert-csv-to-dictionary-in-python/

def find_triangles():
    import time
    import csvfile as csv
    
    input_list = csv.csv_to_lod('my_pairs.csv')
    lst = []

    # need to "clean up" the input from non-traded pairs, and reduce the size of lod
    for item in input_list:
        if item["status"]=="TRADING":
            lst.append(item)

    my_triangles=[]
    print(time.ctime(),"|| Starting search...")
    for a in lst:
        for b in lst:
            for c in lst:
                if a["baseAsset"]==b["baseAsset"] and a["quoteAsset"]==c["baseAsset"] and b["quoteAsset"]==c["quoteAsset"]:
                    my_triangles.append([a["quoteAsset"],b["baseAsset"],c["quoteAsset"]])
                    if len(my_triangles) % 1000 == 0: print(time.ctime(),'|| Loaded:',len(my_triangles))
    print(time.ctime(),"|| Finished search. Found",len(my_triangles),"triangles.")
    csv.lol_to_csv(my_triangles,"my_triangles.csv")
    return(my_triangles)


if __name__=="__main__":
    print("Top 10:",find_triangles()[:10])