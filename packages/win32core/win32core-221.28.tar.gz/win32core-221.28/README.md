# The Core of Pywin32

[![build status][2]][3] [![Codacy Badge][8]][9] [![codecov][10]][11]

This package contains all of the core libraries that are avaiable in 
PyWin32. For most users, this library will be enough to cover all use 
cases that require calling winapi function from Python code. However, this
packakge does not include a dependency on MFC and can be compiled by a default
installaion of MS Build Tools, making it a safe and reliable dependency
for most projects. 

## Simplicity by Design

One of the main goals of this project is to enhance the mantainability and 
simplicity of the core libraries that so many windows projects depend on. 
To make this possible, this project has a easy-to-understand layout that 
makes quick fixes trivial to implement.

If you `import win32.api`, you can expect that the c++ is located in the 
`win32\api` or the `win32\_api` folder. In addition, it is not difficult 
to trace c++ module dependencies by simply looking at the `module.yml` files.
This is in contrast to the original project structure, which had multiple modules
in one folder and a confusing project layout.

[2]: https://ci.appveyor.com/api/projects/status/github/pywin32/win32core?branch=master&svg=true
[3]: https://ci.appveyor.com/project/pywin32/win32core
[8]: https://api.codacy.com/project/badge/Grade/e44e29ca88954bdd9bf0a21bacc78c01
[9]: https://www.codacy.com/app/pywin32/win32core?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pywin32/win32core&amp;utm_campaign=Badge_Grade
[10]: https://codecov.io/gh/pywin32/pypiwin32/branch/master/graph/badge.svg
[11]: https://codecov.io/gh/pywin32/pypiwin32
