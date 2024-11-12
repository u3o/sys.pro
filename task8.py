import doctest

def format_table(benchmarks, algos, results):
    """
    >>> format_table(["best case", "worst case"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    | Benchmark  | quick sort | merge sort | bubble sort |
    |----------------------------------------------------|
    | best case  | 1.23       | 1.56       | 2.0         |
    | worst case | 3.3        | 2.9        | 3.9         |

    >>> format_table(["best", "worst"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    | Benchmark | quick sort | merge sort | bubble sort |
    |---------------------------------------------------|
    | best      | 1.23       | 1.56       | 2.0         |
    | worst     | 3.3        | 2.9        | 3.9         |

    >>> format_table(["best case", "worst case"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.566666666666, 2.0], [3.3, 2.9, 3.9]])
    | Benchmark  | quick sort | merge sort     | bubble sort |
    |--------------------------------------------------------|
    | best case  | 1.23       | 1.566666666666 | 2.0         |
    | worst case | 3.3        | 2.9            | 3.9         |

    >>> format_table(["best case", "worst case"], ["q", "m", "b"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    | Benchmark  | q    | m    | b   |
    |--------------------------------|
    | best case  | 1.23 | 1.56 | 2.0 |
    | worst case | 3.3  | 2.9  | 3.9 |
    """

    def print_row(words, s):
        for i in range(len(words)):
            print(f"|{s}{words[i]}{s}{(lens[i] - len(str(words[i]))) * s}", end = "")
        print("|")

    #getting lengths of all rows in an array called "lens"
    benchmark_len = max([len(benchmark) for benchmark in benchmarks] + [len("Benchmark")])
    alg_lens = []
    for i in range(len(results[0])): 
        alg_len = max([len(str(result[i])) for result in results] + [len(algos[i])])
        alg_lens.append(alg_len)
    lens = [benchmark_len] + alg_lens

    print_row(["Benchmark"] + algos, " ")

    print(f"|{"-" * ( sum(lens) + 2*(len(algos)+1) + len(algos))}|")

    for i in range(len(benchmarks)):
        print_row([benchmarks[i]] + results[i], " ")

doctest.testmod()
