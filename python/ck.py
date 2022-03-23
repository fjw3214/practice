import dns.resolver
domain=input()
A=dns.resolver(domain,'A')
"""
from IPy import  IP
#判断ip，网段是否在另一个网段中 IP("") in IP("")
#判断两个网段是否重叠  IP("").overlaps("")
#
ip_s=input()
ips=IP(ip_s)
if len(ips)>1:
    print('net:%s'% ips.net())#输出网络地址
    print('netmask: %s' % ips.netmask())#输出网络掩码
    print('broadcast: %s' % ips.broadcast())#输出网络广播地址
    print('reverse addr； %s' % ips.reverseNames()[0])#输出地址反向解析
    print('subnet: %s' % len(ips))#输出网络子网数
else:
    print('iptype:%s' % ips.iptype())#类型
    print('binary ip:%s'% ips.strBin())#转化为二进制
    print('hexadecimal ip:%s'% ips.strHex())#转化为16进制

"""
"""
#系统信息模块psutil
import psutil

#查看进程及状态
pid=psutil.pids()
# for i in pid:
#      if i>3000 & i<5000:
#         print(psutil.Process(i).name()+'\t\t\t'+psutil.Process(i).status()+'\t\t',i)
#cpu
print(psutil.cpu_times())
#内存
me=psutil.virtual_memory()
print(me.free,me.total)
#分区
swap=psutil.swap_memory()
print(swap)
#磁盘
print(psutil.disk_partitions())
#当前用户
print(psutil.users())
"""