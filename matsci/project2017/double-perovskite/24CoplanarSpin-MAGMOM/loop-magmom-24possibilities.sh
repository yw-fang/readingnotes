#!/bin/sh

for((i=1;i<=24;i=i+1))
do
 if [ "$i" == 8 ] || [ "$i" == 9 ] || [ "$i" == 10 ] || [ "$i" == 11 ];
 then
  echo "This has been comptuted!"
  continue
 fi
 sed -n "$i p" ./MAGMOM.txt 
done
