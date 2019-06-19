#!/bin/bash

FILE=new_spam_train.csv

echo "checking md5sum HAM file"
if [ ! -f .md5ham ]; then
    touch .md5ham
fi

echo "checking md5sum SPAM file"
if [ ! -f .md5ham ]; then
    touch .md5spam
fi

old_md5ham=`cat .md5ham`
old_md5spam=`cat .md5spam`

new_md5ham=`md5sum HAM`
new_md5spam=`md5sum SPAM`

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove empty lines"
    sed -i '/^[[:space:]]*$/d' HAM
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove empty lines"
    sed -i '/^[[:space:]]*$/d' SPAM
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove ,"
    sed -i 's/,//g' HAM
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove ,"
    sed -i 's/,//g' SPAM
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove sender name, prepend class and redirect output to file"
    cut -d' ' -f 2- HAM | awk '{print "ham,"$0}' >> $FILE
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Add double quotes at beginning of ham msg"
    sed -i 's/ham, */ham,"/g' $FILE
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Remove sender name, prepend class and redirect output to file"
    cut -d' ' -f 2- SPAM | awk '{print "spam,"$0}' >> $FILE
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Add double quotes at beginning of spam msg"
    sed -i 's/spam, */spam,"/g' $FILE
fi

if [ "$old_md5ham" != "$new_md5ham" ];then
    echo "Add double quotes at end of all msgs"
    sed -i 's/$/"/g' $FILE
fi

if [ -f $FILE ];then
    echo "split in training and test sets"
    gawk '
    BEGIN {srand()}
    {f = FILENAME (rand() <= 0.8 ? ".80" : ".20"); print > f}
    ' $FILE

    echo "append to old training sets"
    cat $FILE >> spam.csv
    cat $FILE.20 >> spam_test.csv 
    cat $FILE.80 >> spam_train.csv

    echo "remove temp files"
    rm -f $FILE $FILE.20 $FILE.80
fi
echo "updating md5sum HAM file"
md5sum HAM > .md5ham

echo "updating md5sum SPAM file"
md5sum SPAM > .md5spam
