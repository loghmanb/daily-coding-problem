'''
Observer pattern

https://en.wikipedia.org/wiki/Observer_pattern

The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods.

'''

class Observable:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)
    
class Observer:
    def __init__(self, observerable):
        observerable.register(self)

    def notify(self, observable, *args, **kwargs):
        print('notified by', args, kwargs, ' from ', observable)

if __name__ == "__main__":
    subject = Observable()
    observer = Observer(subject)
    subject.notify_observers('test')