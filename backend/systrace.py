#!/usr/bin/env python
# encoding: utf-8

import sys

def trace_callback(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    coName = co.co_name
    coFileName = co.co_filename
    # print(coFileName)
    
    if coName == 'write':
        return
    if coName != 'a' and coName != 'b' and coName != 'c':
        return

    caller = frame.f_back
    callerName = caller.f_code.co_name
    
    print('Call to %s from %s' % (coName, callerName))
    return

def trace_call(file_bytes):
    sys.settrace(trace_callback)
    exec(file_bytes, locals(), locals()) # globals(), globals()
