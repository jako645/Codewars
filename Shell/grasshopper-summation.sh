#/bin/sh
n=$1
sum=0
while [ $n -ne 0 ]
do
  $((sum+=n))
  $((n-=1))
done

echo $sum
