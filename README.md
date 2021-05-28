<h1 align="center">
  <p align="center">Downloads Cleaner</p>
  <img src="/cleaner.png" width="200px" align="center">
</h1>

<h4 align="center">A Mac based app used to keep your download folder organized.</h4>

## Navigation
- [Motivation](#motivation)
- [Getting Started](#started)
- [Installation](#installation)
- [How To Use](#use)
- [Contributing](#contributing)
- [License](#license)

## <a name="description"></a> Motivation

Everytime I tried to find a file or a folder in downloads folder I never seem to locate it unless I search for it. My downloads folder has always been messy. Once I sat for about 2 hours to try to organise my files and finally gave up and ended up watching Netflix.

<p align="center">
<img src="screenshot.png" width="900">
</p>

This gave me an idea to make this process easier by making an automator python script. This script organizes all the files and folders into their own repective folders inorder to organize the downloads folder. It keeps a watch to your downloads folder and keeps organizing unless you close the script

## <a name='started'></a>Getting Started

### Prerequisite

It is a python script so you need to have python installed on your laptop. If you don't already have it on your computer you can download it by using brew in terminal.

> brew install python3

### <a name='installation'></a> Installation

To use this script and customize it you can flork the repository by clicking on the right corner of the repository with the fork sign.

To download the dependencies required to run the "cleaning.command" scipt file use this command in the terminal.

> pip3 install -r requirements.txt

After this you need to give permission to the "cleaning.command" to give read, write and execute files. First you need to get into \*/DownloadCleaner/app by using terminal then run this command:

> chmod 755 cleaning.command

Read more about chmod 755 by clicking [here](https://codefather.tech/blog/chmod-755-command/)

## <a name="use"></a> How To Use

You just need to double click on "cleaning.command". It will run the script on your computer. If you have any issues please send me a mail at -> milindvishnoi@gmail.com

## <a name="contribution"></a> Contributing

All developers are encouraged to not only install the script but also extend and personalize it ! . All source code is available for anyone who wishes to make any tweaks.

### Steps for contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

If you want to change the folders where the files are organized, you can change the location in "location.py" according to your choice.

## <a name="license"></a> License

The MIT License (MIT)

Copyright (c) 2020 Milind Vishnoi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Back To The Top](#DownloadCleaner)
