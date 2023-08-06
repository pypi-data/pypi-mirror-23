# coding: utf-8
"""

license:MIT

Copyright (c) 2016 DKZ

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

==============================================================================
 ________  __         ______                                                  
|   _____||  |       |_    _|                   _                       _     
|  |      |  |         |  |     _____   __  __ | \_    _______  __  __ | \_   
|  |      |  |         |  |    /     \ |  | | ||   _| |   __  ||  | | ||   _| 
|  |_____ |  |_____   _|  |_  |   o   ||  |_| ||  |___|    ___||  |_| ||  |___
|________||________| |______|  \_____/ |______|\_____/|___|    |______|\_____/
==============================================================================
2016/05/01 by DKZ https://davidkingzyb.github.io
github: https://github.com/davidkingzyb/CLIoutput
"""

import clio.title
import clio.list
import clio.tabel
import clio.tree
import clio.chart
import clio.ppt


__all__=['title','list','tabel','tree','chart','ppt']

dotitle=clio.title.dotitle
dolist=clio.list.dolist
dotabel=clio.tabel.dotabel
dotree=clio.tree.dotree
dojson=clio.tree.dojson
dobar=clio.chart.dobar
doppt=clio.ppt.doppt

def dotext(text):
    return text

def dohr(length):
    return '='*length+'\n'

