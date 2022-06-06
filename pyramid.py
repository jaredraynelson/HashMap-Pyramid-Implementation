import sys
from time import perf_counter
from hashmap import HashMap

WEIGHT = 200.00
cache = HashMap()

number_of_function_calls = 0
number_of_cache_calls = 0

def weight_on(row, cols):
    global cache
    global number_of_function_calls
    global number_of_cache_calls
    number_of_function_calls +=1

    #Check in the cache first
    if cache.find((row,cols)):
        number_of_cache_calls += 1
        return cache[(row,cols)]

    else:
        if row == 0:
            result = 0.0
            return result
        elif row == 1:
            result = 100.00
        
        elif cols == 0:
            result = WEIGHT/2 + (weight_on(row -1, cols) / 2)
        #     
        elif row == cols:
            result = WEIGHT/2 + (weight_on(row-1, cols-1)/ 2)
        # middle guy    
        else:
            result =  (WEIGHT/2 + weight_on(row-1, cols-1)/2) + (WEIGHT/2 + weight_on(row-1, cols)/2)



        cache.set((row,cols),result)
        return result


def main(rows = 10):
    part2_txt = 'part2.txt'
    write_file = open(part2_txt, 'w')
    start = perf_counter()
    for i in range(rows):
        for j in range(i + 1):
            write_file.write(f'{weight_on(i,j):.2f} ')
            print(f'{weight_on(i,j):.2f}', end=' ')
        write_file.write('\n')
        print()
    stop = perf_counter()

    print(f'Elapsed Time: {stop - start}','seconds')
    print('Number of function calls:', number_of_function_calls)
    print('Number of cache calls:', number_of_cache_calls)

    write_file.write(f'Elapsed Time: {stop - start} seconds\n')
    write_file.write('Number of function calls: '+ str(number_of_function_calls) + '\n')
    write_file.write('Number of cache calls: '+ str(number_of_cache_calls) +'\n')
    write_file.close()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
