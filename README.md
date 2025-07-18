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

## Plans

* [ ] Add `-h` arg. (Use an arg-parsing scheme for this and also for `-d`).
* [ ] Add `e` token
* [ ] Add `chs` unary operator
* [ ] Add `exp` unary operator
* [ ] Add `log` unary operator
* [ ] Add `chs` unary operator
* [ ] Add `recip` or `inv` unary operator
* [ ] Add `arc` (as prefix to `sin`, `cos` or `tan`)
* [ ] Add `==` arg (need to decide on number of digits unless python has a
* [ ] Add `exch` binary operator
* [ ] Add `digits`
* [ ] Add other things I use a lot on my calculator.
* [ ] Make help longer (so folks don't have to go to a webpage)
