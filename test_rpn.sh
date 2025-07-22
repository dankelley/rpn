./rpn e                        # 2.718282 (Euler's number ...)
./rpn e -d 10 2.7192818 approx  # 2.7182818285 (... to 10 digits.)
./rpn pi                       # 3.141593 (pi is also built-in)
./rpn 10 35                    # [10.0, 35.0] (two items on stack ...)
./rpn 10 35 + 45 APPROX        # 45.000000 (addition)
./rpn 10 2 / 5 APPROX          # divide second-last stack item by last stack item
./rpn 10 2 x 20 APPROX         # multiplication, preferred style ...
./rpn 45 sin 2 sqrt inv APPROX # sin, cos, and tan use angle in degrees
./rpn 10 35 exch               # [35.0, 10.0] (... exchange those items)
./rpn 1 asin 90 APPROX         # asin, acos, and atan return an angle in degrees
./rpn 10 ln                    # natural log
./rpn 10 log                   # base-10 log
./rpn 10 2 ^ 100 APPROX        # exponentiation
# Saving 'def' quantities to a file
./rpn -l lib.json pi 2 x _tau def
./rpn -l lib.json _tau 2 / pi APPROX #
rm -f lib.json
# Puzzles: without running rpn, guess the meaning of the following
./rpn pi 4 / deg sin
./rpn 45 sin sqr 45 cos sqr +
./rpn 1e-7 _eps def 1 _eps + sqr 1 sqr - _eps /

./rpn -l gravity.json 5.972e24 _Me def 6371e3 _Re def 6.674e-11 _G def
./rpn -l gravity.json _G _Me x _Re sqr / _g def
./rpn -l gravity.json -s
rm -f gravity.json

