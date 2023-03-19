#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janstoitkernel
IPKernelApp.launch_instance(kernel_class=janstoitkernel)
