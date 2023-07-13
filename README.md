<h1>pwgen</h1>
<h4>Python password generator</h4>

This script runs in your shell "natively" so long as you have installed python3.<br>
There are no third party dependencies (other than python), so you can essentially "drag and drop" the script into `/usr/local/bin` as long as you run `chmod a+x pwgen.py` first.

<h2>Usage</h2>
Simply run it with your shell as any other executable file using `./pwgen.py`<br>
You may add any combination of the available arguments, these are:<br>

    -u,           --uppercase   Specify the usage of Uppercase letters in the password.
    -d,           --digits      Specify the usage of Digits (numbers 0 to 9) in the password.
    -s,           --symbols     Specify the usage of Special Symbols in the password.
    -w,           --word        Specify the usage of Words in the password.
    -l <int>, --length <int>    Specify the Length of the password. 
                                If -w is also passed, this specifies the amount of words.