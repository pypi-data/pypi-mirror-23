'''
BLURB GOES HERE.

Copyright (c) 2015 - 2017 Rob "N3X15" Nelson <nexisentertainment@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''
import codecs
import os
import re
import shutil
import yaml

from buildtools import log, os_utils
from buildtools.maestro.base_target import BuildTarget

class SerializableLambda(yaml.YAMLObject):
    yaml_tag = '!lambda'

    def __init__(self, text):
        self.string=text

    def __call__(self, arg):
        return self.string

class SerializableFileLambda(SerializableLambda):
    yaml_tag = '!filelambda'

    def __init__(self, filename, outformat='{FILEDATA}', encoding='utf-8-sig'):
        self.filename=filename
        self.outformat=outformat
        self.encoding=encoding

    def __call__(self, arg):
        with codecs.open(self.filename, 'r', encoding=self.encoding) as f:
            return self.outformat.format(FILEDATA=f.read())

class CopyFileTarget(BuildTarget):
    BT_TYPE = 'CopyFile'

    def __init__(self, target=None, filename=None, dependencies=[]):
        self.subject=filename
        super(CopyFileTarget, self).__init__(target, [filename], dependencies)

    def serialize(self):
        dat = super(CopyFileTarget, self).serialize()
        return dat

    def deserialize(self,data):
        super(CopyFileTarget, self).deserialize(data)
        self.subject=data['files'][0]

    def build(self):
        if self.checkMTimes(self.files + self.dependencies, self.target, {}):
            os_utils.single_copy(self.subject, self.target, verbose=True)

class ReplaceTextTarget(BuildTarget):
    BT_TYPE = 'ReplaceText'

    def __init__(self, target=None, filename=None, replacements=None, dependencies=[], read_encoding='utf-8-sig', write_encoding='utf-8-sig'):
        self.replacements = replacements
        self.subject=filename
        self.read_encoding=read_encoding
        self.write_encoding=write_encoding
        super(ReplaceTextTarget, self).__init__(target, [filename], dependencies)

    def serialize(self):
        dat = super(ReplaceTextTarget, self).serialize()
        dat['replacements'] = self.replacements
        dat['read-encoding'] = self.read_encoding
        dat['write-encoding'] = self.write_encoding
        return dat

    def deserialize(self,data):
        super(ReplaceTextTarget, self).deserialize(data)
        self.replacements=data['replacements']
        self.read_encoding=data['read-encoding']
        self.write_encoding=data['write-encoding']
        self.subject=data['files'][0]

    def build(self):
        if self.checkMTimes(self.files + self.dependencies, self.target, self.replacements):
            with log.info('Writing %s...', self.target):
                os_utils.ensureDirExists(os.path.dirname(self.target))
                with codecs.open(self.subject, 'r', encoding=self.read_encoding) as inf:
                    with codecs.open(self.target + '.out', 'w', encoding=self.write_encoding) as outf:
                        for line in inf:
                            for needle, replacement in self.replacements.items():
                                if isinstance(needle, SerializableLambda):
                                    needle = needle()
                                #if isinstance(replacement, SerializableLambda):
                                #    replacement = replacement()
                                line = re.sub(needle, replacement, line)
                            outf.write(line)
                shutil.move(self.target + '.out', self.target)
