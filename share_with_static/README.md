### g++ -c com.cpp
### ar crv com.a com.o
### g++ -shared -fPIC -o libliba.so liba.cpp com.a
### g++ -shared -fPIC -o liblibb.so libb.cpp com.a
### g++ main.cpp -L./ -lliba -llibb -o main