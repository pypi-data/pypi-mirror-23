Future Thread
=============

Creates a thread with Future attributes.

Based on (and actively uses) features from concurrent.futures module to easily start a function in a
new background thread without the overhead of using a ThreadPoolExecutor, while still providing a Future style handle around said thread.

Usage::

    import time
    from future_thread import Future, DeferredFuture

    def background():
        time.sleep(10)
        return True

    fut = Future(background)
    fut.result()  # will block until thread finished


    fut = DeferredFuture(background)
    # do some other stuff
    fut.start()

For more info on the Future object see: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future

