def find_profits():
    import time
    import csvfile as csv
    import trianglecheck as tc

    my_profits=[]
    my_triangles=csv.csv_to_lol("my_triangles.csv")
    print(time.ctime(),"|| Starting search...")
    
    for triangle in my_triangles:
        a = tc.check_triangle(triangle[0],triangle[1],triangle[2])
        new_item = triangle + a[0] + a[1]
        my_profits.append(new_item)

    print(time.ctime(),"|| Finished search. Found",len(my_profits),"profits.")
    csv.lol_to_csv(my_profits,"my_profits.csv")
        
    return(my_profits)


def sort_profits(list, index):
    from operator import itemgetter
    
    sorted_profits = sorted(list, key=itemgetter(index), reverse=True)
    return sorted_profits