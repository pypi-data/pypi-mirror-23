from untwisted.event import LOAD, READ, WRITE, get_event
import sys

class Fixed(object):
    """
    A handle for application layers that demand fixed chunk transmission of data.

    def on_found(spin, data):
        print data

    Fixed(spin, size=4)
    xmap(spin, FOUND, on_found)

    If it arises a chunk of size equal or greater than 4 then FOUND is processed.
    """

    FOUND = get_event()
    def __init__(self, spin, size=4):
        spin.add_map(LOAD, self.update)
        self.arr  = bytearray()
        self.size = size

    def update(self, spin, data):
        self.arr.extend(data)

        for ind in xrange(self.size, len(self.arr) + 1, self.size):
            chunk = buffer(self.arr, ind - self.size, self.size)
            spin.drive(Fixed.FOUND, chunk)
        else:
            try:
               del self.arr[:ind]
            except NameError:
                pass

class Breaker(object):
    """
    A handle for application layer protocols follows a command scheme pattern.

    def on_add(spin, *args):
        print args

    Breaker(spin)
    xmap(spin, 'add', on_add)

    If it arises the sequence of data defined below then on_add is processed and its
    arguments will be ('1', '2', '3').

        'add 1 2 3'

    
    """

    def __init__(self, device, delim=' '):
        self.delim = delim
        device.add_map(Terminator.FOUND, self.handle_found)

    def handle_found(self, device, data):
        lst = data.split(self.delim)
        device.drive(lst.pop(0), *lst)

class Terminator:
    """
    A handle for application layer protocols that use '\r\n' as token.

    def on_found(spin, data):
        print data

    Terminator(spin, delim='\r\n')
    xmap(spin, FOUND, on_found)

    If it arises the sequence below then on_found is processed.

        'some-data\r\n'
    """

    FOUND = get_event()
    def __init__(self, spin, delim='\r\n'):
        self.delim  = delim
        self.arr    = bytearray()

        spin.add_map(LOAD, self.update)

    def update(self, spin, data):
        self.arr.extend(data)

        if not self.delim in data:
            return

        data = str(self.arr)
        lst  = data.split(self.delim)
        del self.arr[:]
        self.arr.extend(lst.pop(-1))

        for ind in lst:
            spin.drive(Terminator.FOUND, ind)
            
class Accumulator(object):
    """
    Just an accumulator on LOAD.
    """
    def __init__(self, spin):
        spin.add_map(LOAD, self.update)
        spin.accumulator  = self
        self.data = ''

    def update(self, spin, data):
        self.data = self.data + data

class AccUntil(object):
    DONE = get_event()
    def __init__(self, spin, data='', delim='\r\n\r\n'):
        self.delim = delim
        self.arr   = bytearray()
        self.spin  = spin
        spin.add_map(LOAD, self.update)
        self.update(spin, data)

    def update(self, spin, data):
        self.arr.extend(data)
        if self.delim in self.arr:
            self.process(spin)

    def process(self, spin):
        spin.del_map(LOAD, self.update)
        a, b = self.arr.split(self.delim, 1)
        spin.drive(AccUntil.DONE, str(a), str(b))

class TmpFile(object):
    DONE = get_event()
    def __init__(self, spin, data, max_size, fd):
        self.fd       = fd
        self.max_size = max_size
        spin.add_map(LOAD, self.update)

        self.update(spin, data)

    def update(self, spin, data):
        pos   = self.fd.tell()
        count = self.max_size - pos
        self.fd.write(data[:count])

        if len(data) < count: 
            return

        spin.del_map(LOAD, self.update)
        spin.drive(TmpFile.DONE, self.fd, data[count:])

# class AccAck(object):
    # DONE = get_event()
# 
    # def __init__(self, spin, fd, max_size, ack):
        # self.fd       = fd
        # self.max_size = size
        # xmap(spin, LOAD, self.update)
# 
    # def update(self, spin, data):
        # self.fd.write(data)
        # spin.dump(self.ack(fd, self.max_size))
# 
        # if self.fd.tell() >= self.max_size:
            # pass

def logcon(spin, fd=sys.stdout):
    def log(spin, data):
        fd.write('%s\n' % data)
    spin.add_map(Terminator.FOUND, log)





