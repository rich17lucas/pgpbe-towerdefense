class mythang(object):

    def sayHello(self, text):
        print("Hello {} ".format(text))

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        self._text = val


if __name__ == '__main__':
    mt = mythang()
    mt.sayHello("Richard")
    print("Setting text")
    mt.text = "Sue"
    print(mt.sayHello(mt.text))
