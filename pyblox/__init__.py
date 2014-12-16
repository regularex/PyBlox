"""
The MIT License (MIT)

The Original Code is PyBlox.

The Initial Developer of the Original Code is Noel Morgan,
http://www.pyblox.org/

Copyright (c) 2014 Noel Morgan <noel@morganix.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import pkg_resources
from paste.registry import StackedObjectProxy
from paste.config import DispatchingConfig


__all__ = ['app_globals', 'cache', 'config', 'request', 'response',
           'session', 'tmpl_context', 'url']


app_globals = StackedObjectProxy(name="app_globals")
cache = StackedObjectProxy(name="cache")
request = StackedObjectProxy(name="request")
response = StackedObjectProxy(name="response")
session = StackedObjectProxy(name="session")
tmpl_context = StackedObjectProxy(name="tmpl_context")
url = StackedObjectProxy(name="url")
template = StackedObjectProxy(name="template")
permissions = StackedObjectProxy(name="permissions")
auth_id = StackedObjectProxy(name="auth_id")
config = DispatchingConfig()





