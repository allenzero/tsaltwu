PNAME=lolt
PLOG=lolt.log

echo ">> shutdown ..."

ps aux|grep python| grep lolt| grep tcp_server |grep lolt.log|grep -v grep |kill -9 `awk -F' ' '{print $2}'`

echo "done! \n\n"
