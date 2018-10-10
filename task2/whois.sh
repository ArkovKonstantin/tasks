#!/bin/bash
mkdir $1
cd $1

if [ $2 = 'domain' ]
then
var=$(echo "$3.html" | sed 's/\./_/')
curl "https://www.whois.com/whois/$3" >> $var
fi

if [ $2 = 'file' ]
then
FILE=$3
while read line; do
     var=$(echo "$line.html" | sed 's/\./_/')
     curl "https://www.whois.com/whois/$line" >> $var
done < $FILE
fi

#github.com
#http://google.com
#www.yandex.ru
#stackoverflow.com


#stringZ='http://google.com'

# echo `expr match "$stringZ" '.*\(*[a-z]\)'`

#echo `expr match "$stringZ" '\(..[a-z]*[\.]\)'`