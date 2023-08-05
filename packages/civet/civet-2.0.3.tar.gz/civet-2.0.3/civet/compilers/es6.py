import errno
import os

from django.conf import settings

from civet.compilers.base_compiler import Compiler


es6_extension = getattr(settings, 'CIVET_ES6_EXTENSION', '.js')
node_path = getattr(settings, 'CIVET_ES6_NODE_PATH', None)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


class ES6Compiler(Compiler):
    """Civet compiler for Ecmascript 6 using Babel.
    """
    name = "ECMAScript 6"
    executable_name = 'babel'
    executable_setting = 'CIVET_BABEL_BIN'

    def __init__(self, precompiled_assets_dir, kill_on_error):
        super(ES6Compiler, self).__init__(precompiled_assets_dir,
                                          kill_on_error)
        self.args = [('--compile', '--map')]
        if node_path:
            self.env.update(NODE_PATH=node_path)

    def matches(self, base, ext):
        return ext == es6_extension

    def get_dest_path(self, base, ext):
        return os.path.join(self.precompiled_assets_dir, base + '.js')

    def get_command_with_arguments(self, src_path, dst_path):
        return [
            self.executable,
            '--source-maps', 'true',
            '-o',
            dst_path,
            src_path,
        ]

    def compile(self, src_path, dst_path):
        dst_dir, dst_basename = os.path.split(dst_path)
        mkdir_p(dst_dir)
        super(ES6Compiler, self).compile(src_path, dst_path)
