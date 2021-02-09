import proxyscrape
import os
file=open("prox.txt", 'w+')
col=proxyscrape.create_collector('pcol', ['http', 'socks5'])
numar=input('how many proxies do you want ')

for i in range(int(numar)):
    prox=col.get_proxy({'anonymous': True})
    phpp=str(prox.host) +' '+ str(prox.port)
    print(phpp)
    file.write(phpp + '\n')
