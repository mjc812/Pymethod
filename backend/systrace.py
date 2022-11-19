#!/usr/bin/env python
# encoding: utf-8

import sys

allDefs = []

def trace_callback(frame, event, arg):
    if event != 'call':
        return

    co = frame.f_code
    coName = co.co_name
    
    if (coName not in allDefs) :
        return

    caller = frame.f_back
    callerName = caller.f_code.co_name

    if (callerName not in allDefs) :
        return

    print('Call to %s from %s' % (coName, callerName))
    return

def trace_call(file_bytes, defs):
    allDefs.extend(defs['allDefs'])
    sys.settrace(trace_callback)
    exec(file_bytes, locals(), locals()) # globals(), globals()
