#!/bin/sh

./configure --enable-libmp3lame --enable-openssl --enable-gpl --enable-nonfree --enable-libx264 --extra-cflags=-I/usr/local/include --extra-ldflags=-L/usr/local/lib

make 

ln -s /usr/local/lib/libmp3lame.so.0 /usr/lib64/libmp3lame.so.0
ln -s /usr/local/lib/libx264.so.155 /usr/lib64/libx264.so.155

make install 
