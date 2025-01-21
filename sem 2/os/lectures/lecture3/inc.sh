N=0
echo start `cat x`

while test $N -lt 1000; do
    K=`cat x`
    K=`expr $K + 1`
    echo $K > x
    N=`expr $N + 1`
done
echo stop `cat x`
