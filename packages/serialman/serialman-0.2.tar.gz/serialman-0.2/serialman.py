#!/usr/bin/env python

import serial
import threading
import time
from multiprocessing import Process, Queue
try:
    from queue import Empty
except ImportError:
    from Queue import Empty

class SerialManager(Process):
    """ This class has been written by
        Philipp Klaus and can be found on
        https://github.com/pklaus/serialman """

    def __init__(self, device, **kwargs):
        settings = dict()
        settings['baudrate'] = 9600
        settings['bytesize'] = serial.EIGHTBITS
        settings['parity'] = serial.PARITY_NONE
        settings['stopbits'] = serial.STOPBITS_ONE
        settings['timeout'] = 0.0005
        settings.update(kwargs)
        self._kwargs = settings
        self.ser = serial.Serial(device, **self._kwargs)
        self.in_queue = Queue()
        self.out_queue = Queue()
        self.closing = False # A flag to indicate thread shutdown
        self.read_num_bytes  = 256
        self.sleeptime = None
        self._chunker = None
        Process.__init__(self, target=self.loop)

    def set_chunker(self, chunker):
        self._chunker = chunker
        self.in_queue = chunker.in_queue

    def loop(self):
        try:
            while not self.closing:
                if self.sleeptime: time.sleep(self.sleeptime)
                in_data = self.ser.read(self.read_num_bytes)
                if in_data:
                    if self._chunker:
                        self._chunker.new_data(in_data)
                    else:
                        self.in_queue.put(in_data)
                try:
                    out_buffer = self.out_queue.get_nowait()
                    self.ser.write(out_buffer)
                except Empty:
                    pass
        except (KeyboardInterrupt, SystemExit):
            pass
        self.ser.close()

    def close(self):
        self.closing = True

class NewlineChunker(object):

    delimiter = b'\n'

    # We throw away the first n items as the buffer of a USB to Serial
    # converter (like the FT232RL) might still contain old data when
    # opening the serial port.
    discard_first_n_items = 1

    # We also throw away what seems to be the first message
    # (It could be incomplete if we start listening while it's transmission was already startd.)
    discard_first_n_messages = 1

    def __init__(self):
        self.in_queue = Queue() # Queue
        self.buf = b"" # buffer holding the incoming data

    def new_data(self, data):
        if self.discard_first_n_items:
            self.discard_first_n_items -= 1
            return
        self.buf += data
        while self.delimiter in self.buf:
            first_part, delim, second_part = self.buf.partition(self.delimiter)
            self.buf = second_part
            if self.discard_first_n_messages:
                self.discard_first_n_messages -= 1
                continue
            self.in_queue.put(first_part+self.delimiter)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='A class to manage reading and writing from and to a serial port.')
    parser.add_argument('--timeout', '-t', type=float, default=0.0005, help='Seconds until reading from serial port times out [default: 0.0005].')
    parser.add_argument('--sleeptime', '-s', type=float, default=None, help='Seconds to sleep before reading from serial port again [default: none].')
    parser.add_argument('--baudrate', '-b', type=int, default=9600, help='Baudrate of serial port [default: 9600].')
    parser.add_argument('device', help='The serial port to use (COM4, /dev/ttyUSB1 or similar).')
    args = parser.parse_args()

    s1 = SerialManager(args.device, baudrate=args.baudrate, timeout=args.timeout)
    s1.sleeptime = args.sleeptime
    s1.read_num_size = 512
    s1.start()

    try:
        while True:
            data = s1.in_queue.get()
            print(repr(data))
    except KeyboardInterrupt:
        s1.close()
    finally:
        s1.close()
    s1.join()

if __name__ == "__main__":
    main()

