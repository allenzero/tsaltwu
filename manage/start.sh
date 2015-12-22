PDIR=/home/alen/github/tsaltwu
LDIR=/home/alen/logs

echo ">> start TCP work..."
/usr/bin/python $PDIR/manage.py --daemonize=True --log_file_prefix=$LDIR/tsaltwu.log --processes=1
echo "done! \n\n"
