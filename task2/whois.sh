#!/bin/bash
dir=$1
input_type=$2
input=$3

function clear_domain {
domain=$(echo "$domain" | sed 's/https:\/\///')
domain=$(echo "$domain" | sed 's/http:\/\///')
domain=$(echo "$domain" | sed 's/www.//')
}

function create_html {
file_name=$(echo "$domain.html" | sed 's/\./_/')
curl "https://www.whois.com/whois/$domain" >> $file_name
}

if ! [ -d $dir ]; then
mkdir $dir
fi

cd $dir

if [ $input_type = 'domain' ]; then
domain=$input
clear_domain
create_html
elif [ $input_type = 'file' ]; then
for domain in $(cat "../$input")
do
clear_domain
create_html
done
fi