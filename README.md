# rpn

Python commandline script for simple RPN arithmetic.

## Installation

Copy the file `rpn` to somewhere on your system path, and make it executable. (I do this with a link to `~/bin/,rpn` because I like
my additions to the shell to start with a comma, and I like knowing where such things live.)

## Usage examples

### Get help

```sh
rpn
```

### Turn on debugging

```sh
rpn -d ...
```

### Add two numbers

```sh
rpn 10 35 +
```

### Multiply two numbers

Note that `*` is not used for multiplication, because that is way to
request the unix shell to complete filenames. Instead, `x` is used.

```sh
rpn 1.0 3.5 + 10 x
```

### Trigonometry

```sh
rpn 1.0 3.5 + 10 x sin # 0.707
```

### Exponentiation

```sh
rpn 1.0 3.5 + 10 x sin 2 ^ 2 45 cos 2 ^ + # 1.0
```

