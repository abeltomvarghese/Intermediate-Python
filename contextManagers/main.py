from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'a')
    try:
        yield f
    finally:
        f.close()


class ManagedFile(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        if exc_type is not None:
            print("This is where you would handle the exception")
        print('exit')
        return True #must return true to ensure that the exception is not thrown

if __name__ == '__main__':
    # Example of a context manager
    with open('notes.txt','w') as file:
        file.write("What a wonderful world\n")



    #Creating your own context manager
    with ManagedFile('newNotes.txt') as file:
        file.write("Some todoo...\n")
        file.someMethod() #doesnt exist --> will raise an error

    print("The end")
    print()

    #Creating context managers from functions using generators
    with open_managed_file("newNotes.txt") as f:
        f.write("More todoos...\n")