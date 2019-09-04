import threading

def start():
    print('---start---1')
    event.wait()
    print('---start---2')

if __name__ == '__main__':
    event = threading.Event()
    t = threading.Thread(target=start)
    t.start()

    result = input(">>:")
    if result == 'set':
        event.set()