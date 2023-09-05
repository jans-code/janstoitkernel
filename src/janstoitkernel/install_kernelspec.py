#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""Kernel installer"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

json ="""{"argv":["python","-m","janstoitkernel", "-f", "{connection_file}"],
 "display_name":"Toit"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   viewBox="0 0 34.56 34.56"
   width="300"
   height="300"
   version="1.1"
   id="svg6"
   sodipodi:docname="toit.com"
   inkscape:version="1.2.2 (732a01da63, 2022-12-09)"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs10" />
  <sodipodi:namedview
     id="namedview8"
     pagecolor="#505050"
     bordercolor="#ffffff"
     borderopacity="1"
     inkscape:showpageshadow="0"
     inkscape:pageopacity="0"
     inkscape:pagecheckerboard="1"
     inkscape:deskcolor="#505050"
     showgrid="false"
     inkscape:zoom="1.8758129"
     inkscape:cx="252.4239"
     inkscape:cy="163.12928"
     inkscape:window-width="1920"
     inkscape:window-height="1009"
     inkscape:window-x="-8"
     inkscape:window-y="-8"
     inkscape:window-maximized="1"
     inkscape:current-layer="svg6" />
  <rect
     style="fill:#fac864;fill-opacity:1;stroke-width:0.156102;stroke-linecap:square;stroke-miterlimit:7"
     id="rect291"
     width="34.560001"
     height="34.560001"
     x="2.3092639e-14"
     y="1.9539925e-14"
     ry="3.7390182" />
  <path
     d="m 17.9664,14.676 c -0.312,0.492 -0.324,1.836 -0.048,2.4 0.48,0.948 3,4.788 3.204,4.908 0.276,0.144 0.96,0.156 1.2,0.024 0.108,-0.06 0.852,-0.84 1.656,-1.728 0.804,-0.888 1.572,-1.632 1.692,-1.656 0.252,-0.048 0.576,0.168 0.576,0.384 0,0.216 -3.096,3.588 -3.516,3.828 -0.528,0.3 -1.692,0.24 -2.196,-0.12 -0.192,-0.144 -0.936,-1.176 -1.668,-2.364 -0.732,-1.152 -1.392,-2.136 -1.488,-2.172 -0.252,-0.096 -0.372,0.06 -1.788,2.292 -1.476,2.328 -1.74,2.568 -2.772,2.568 -0.888,0 -1.152,-0.18 -2.556,-1.692 -1.836,-1.992 -2.028,-2.256 -1.896,-2.52 0.276,-0.504 0.612,-0.276 2.1,1.38 0.792,0.888 1.56,1.68 1.704,1.752 a 1.362,1.362 0 0 0 1.272,-0.036 c 0.144,-0.096 0.936,-1.248 1.764,-2.556 l 1.5,-2.388 0.036,-0.912 c 0.048,-1.008 -0.12,-1.524 -0.624,-1.848 -0.144,-0.096 -1.92,-0.564 -3.924,-1.02 -3.756,-0.876 -4.068,-0.996 -3.816,-1.452 a 0.4584,0.4584 0 0 1 0.396,-0.228 c 0.144,0 2.016,0.408 4.152,0.9 2.136,0.492 4.08,0.9 4.32,0.9 0.24,0 2.184,-0.408 4.332,-0.9 2.148,-0.492 4.02,-0.888 4.176,-0.876 0.408,0.048 0.6,0.396 0.372,0.636 -0.108,0.096 -1.752,0.54 -3.828,1.02 -1.992,0.468 -3.732,0.9 -3.864,0.972 a 1.6032,1.6032 0 0 0 -0.468,0.504 z"
     id="path4"
     style="stroke-width:0.12" />
</svg>"""

def install_kernelspec():
    kerneldir = "/tmp/janstoitkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janstoitkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janstoitkernel')