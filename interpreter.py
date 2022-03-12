# Copyright 2022 kaigonzalez
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nvbasic
import platform

# if platform.system() == 'Linux':
#     import readline

nvbasic.nvb_globalfuncs()

print("Welcome to the NVBasic Interpreter (Requires the NVBasic Lib to be linked!")
print("Type HELP if you need help with using it.")

def std_HELP(args):
    print("NVBasic Interpreter is a programming language which aims to be a performant-subset of the QBasic programming language.")
    print("Functions I can see:")
    for fnc in nvbasic.builtins:
        print("- " + fnc)
        print("\tRun " + fnc + " <args>")
    print("Refer to the NVBasic README for help.")

nvbasic.nvdAddfunc("HELP", std_HELP)

while True:
    chn = input(">>>")
    nvbasic.nvbBuild(chn)