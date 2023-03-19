##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

workingdir = "/tmp/toitkernel/"

class janstoitkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'Toit'
    language_version = '2.0.0'
    language_info = {
        'name': 'Toit',
        'mimetype': 'application/toit',
        'file_extension': '.toit',
    }
    banner = "Toit kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            with open(workingdir + "toitproj.toit", "w") as f:
                    f.write(code)
            solution = pexpect.run('toit.run ' + workingdir  + 'toitproj.toit').decode('utf-8')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
    
    def do_shutdown(self, restart):
        shutil.rmtree(workingdir)
