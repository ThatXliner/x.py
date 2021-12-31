# X.py

> Simplified Python scripting.

[`zx`](https://github.com/google/zx) for python.

## Installation

I don't plan to make this on PyPi anytime soon.

What you should do instead is either **copy the `x.py` file** into the same folder where your scripts are stored, or **symlink it** after you cloned this repository.

## Documentation

Like the [`fuckit`](https://github.com/ajalt/fuckitpy) Python module, all functionality are given as the module. Remember to add `import x` at the top of your script before using.

### Call a subprocess

You can use `x.py` as a simplified API for running subprocess commands.

Let's say you want to get the output of `ls -a`. You would do

```py
>>> import x
>>> print(x(["ls", "-a"]))
SubprocessOutput(stdout='.\n..\nfoo\n', stderr='')
>>>
```

### `os.system`

`x.py` provides a simple alias for `os.system()`

```py
>>> import x
>>> x.call("git clone https://github.com/git/git.git --depth=1")
Cloning into 'git'...
remote: Enumerating objects: 4073, done.
remote: Counting objects: 100% (4073/4073), done.
remote: Compressing objects: 100% (3593/3593), done.
remote: Total 4073 (delta 378), reused 1940 (delta 310), pack-reused 0
Receiving objects: 100% (4073/4073), 9.79 MiB | 6.40 MiB/s, done.
Resolving deltas: 100% (378/378), done.
>>>
```

### Print informational messages with automatic coloring

I've found myself rewriting a lot of the same utility color-info functions. `x.py` provides cross-platform utilities to print colored (via ANSI sequences. Stripped on Windows or non-terminal) messages.

`x.i` (info) and `x.w` (warning) returns a boolean indicating whether color was used or not

#### Info

```py
>>> import x
>>> x.i("Attempting to fetch data")
Info: Attempting to fetch data
>>> print(_)
True
```
#### Warning

```py
>>> import x
>>> x.w("no credentials provided")
Warning: no credentials provided
>>> print(_)
True
```
#### Success

```py
>>> import x
>>> x.s("Done!")
Success: Done!
>>> print(_)
True
```
#### Error (and quit)

```py
>>> import x
>>> x.e("failed to fetch data", status=2)
Error: failed to fetch data

[Process exited with status code 2]
```
The `status` parameter is optional, defaults to `1`. Will exit program via `sys.exit`.
