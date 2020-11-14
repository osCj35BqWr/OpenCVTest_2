import signal

def sigterm(x, y):
    pass

signal.signal(signal.SIGTERM, sigterm)
signal.sigwait([signal.SIGTERM])

