with open("books.txt") as bofm:
    for row in bofm:
        # print(row)
        bk = row.split("\n")
        # # clean_bk = bk.strip()
        bk = bk[0].strip()
        print(bk)
    # BETTER SOLUION
    # DON'T SPLIT THE ROWS
    # for line in bofm:
    #     book = line.strip()
    #     print(book)
