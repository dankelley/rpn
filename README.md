# rpn

Python commandline script for simple RPN arithmetic.

## Installation

Copy the file `rpn` to somewhere on your system path, and make it executable. (I do this with a link to `~/bin/,rpn` because I like
my additions to the shell to start with a comma, and I like knowing where such things live.)

### Instructions

To start, type

```sh
rpn -h
```

and examine what it prints.  You'll find brief explanations of the optional
arguments, as well as some examples.

### Videos

* https://youtu.be/HSpJGPOwwrg demonstration of the creation of a library file, into which a function is saved.

### Suggestions for library entries

This is a sample of my library named `~/dek.json` ...
```
{
    "_f2c": "32 - 5 x 9 /",
    "_c2f": "9 x 5 / 32 +"
}
```

... and this is how I created that first item:
```
,rpn -l dek.json '32 - 5 x 9 /' _f2c def
```
