#!/bin/bash

# g++ -O3 solve.cpp

# ./a.out < inputs/0-demo.txt > output/0.out
# ./a.out < inputs/1-thunberg.txt > output/1.out
# ./a.out < inputs/2-attenborough.txt > output/2.out
# ./a.out < inputs/3-goodall.txt > output/3.out
# ./a.out < inputs/4-maathai.txt > output/4.out
# ./a.out < inputs/5-carson.txt > output/5.out
# ./a.out < inputs/6-earle.txt > output/6.out
# ./a.out < inputs/7-mckibben.txt > output/7.out
# ./a.out < inputs/8-shiva.txt > output/8.out

# pypy3.10 solve.py < inputs/0-demo.txt > output/0.out
# pypy3.10 solve.py < inputs/1-thunberg.txt > output/1.out
# pypy3.10 solve.py < inputs/2-attenborough.txt > output/2.out
# pypy3.10 solve.py < inputs/3-goodall.txt > output/3.out
# pypy3.10 solve.py < inputs/4-maathai.txt > output/4.out
# pypy3.10 solve.py < inputs/5-carson.txt > output/5.out
# pypy3.10 solve.py < inputs/6-earle.txt > output/6.out
# pypy3.10 solve.py < inputs/7-mckibben.txt > output/7.out
# pypy3.10 solve.py < inputs/8-shiva.txt > output/8.out

g++ -O3 2.cpp -o exe2
g++ -O3 3.cpp -o exe3
g++ -O3 4-6.cpp -o exe4-6
g++ -O3 5.cpp -o exe5
g++ -O3 7.cpp -o exe7
g++ -O3 8.cpp -o exe8

pypy3.10 0-1.py < inputs/0-demo.txt > output/0.out
pypy3.10 0-1.py < inputs/1-thunberg.txt > output/1.out
./exe2 < inputs/2-attenborough.txt > output/2.out
./exe3 < inputs/3-goodall.txt > output/3.out
./exe4-6 < inputs/4-maathai.txt > output/4.out
./exe5 < inputs/5-carson.txt > output/5.out
./exe4-6 < inputs/6-earle.txt > output/6.out
./exe7 < inputs/7-mckibben.txt > output/7.out
./exe8 < inputs/8-shiva.txt > output/8.out
