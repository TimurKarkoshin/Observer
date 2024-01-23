import abc


class ObserverABC(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    @abc.abstractmethod
    def receive_event(self, event: str = None):
        ...


@abc.abstractmethod
class NotifierABC(abc.ABC):

    @abc.abstractmethod
    def subscribe(self, observer: ObserverABC):
        ...

    @abc.abstractmethod
    def unsubscribe(self, observer: ObserverABC):
        ...

    @abc.abstractmethod
    def notify(self, *args, **kwargs):
        ...


class SenderABC(abc.ABC):

    @abc.abstractmethod
    def receive_event(self, event: str = None):
        ...


class Observer(ObserverABC):
    def receive_event(self, event: str = None):
        print(f"{self} received an event: {event=}")


class Notifier(NotifierABC):
    def __init__(self):
        self.observers = dict()

    def subscribe(self, observer: Observer):
        self.observers[id(observer)] = observer

    def unsubscribe(self, observer: Observer):
        del self.observers[id(observer)]

    def notify(self, event: str):
        for observer in self.observers.values():
            observer.receive_event(event)


class Sender(SenderABC):
    def __init__(self, notifier: NotifierABC):
        self.event_types = []
        self.notifier = notifier

    def receive_event(self, event: str = None):
        self.notifier.notify(event)

    def set_notifier(self, notifier: NotifierABC):
        self.notifier = notifier


if __name__ == "__main__":
    notifier_ = Notifier()
    sender = Sender(notifier_)
    observer1 = Observer("observer#1")
    observer2 = Observer("observer#2")
    notifier_.subscribe(observer1)
    notifier_.subscribe(observer2)
    sender.receive_event("event 11")
