def searcher():
    import time
    # Some 4 seconds time Consuming task.
    book = "this is a book it takes time to complete the whole book Adarsh................."
    time.sleep(4)

    # Yield is used to generate value on the time.
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book.")
        else:
            print("Text is not in the book.")

search = searcher()
next(search)
search.send("Adarsh")
input("Press any key")
search.send("Adarsh......")

search.close()
# Coroutinues are useful when some initialize takes time to get executed and to minimze that time.
# we use Coroutines.