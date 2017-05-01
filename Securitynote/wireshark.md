# Wireshark学习笔记
[i春秋小白入门兴趣团](http://www.ichunqiu.com/newRelease/darrPath/53)
## wireshark的启动
1、启动NetGroup Packet Filter Driver服务，命令行内输入：`net start npf`

## 筛选器
1、筛选某个ip和端口号`ip.addr==10.10.1.11 and tcp.port==80`
2、`!tcp`:

3、`frame.len<=160`
4 tcp[13]==0x18 13：偏移位，ox18:标志位

## 命令行
- 进入wireshark的安装目录c:\\program files\Wireshark
- `editcap demo.pcapng output.pcapng -i 4`将demo.pcapng中的每4s内的数据存储到output.pcapng中
- `tshark -n -q -r demo.pcapng -z "conv,tcp"`过滤demo.pcapng中tcp数据包
- `tshark -n -q -r demo.pcapng -z "io,stat 0,tcp.analysis.retransmission"`过滤demo.pcapng中重传的数据包
- `tshark -r demo.pcapng -Y "ip==219.153.73.221" -w demos.pcapng` 过滤出demo.pcapng中ip=219..的数据包并保存到demos.pcapng中