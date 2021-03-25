# TCPHoneypot

TCPHoneypotはTCPポート宛の攻撃をログに保存するハニーポットです

# Requirement

- Python3
- (iptables)

# Installation

```
~ ❯❯❯ git clone https://github.com/yagimoto/TCPHoneypot

~ ❯❯❯ cd TCPHoneypot/

~/TCPHoneypot ❯❯❯ python3 TCPHoneypot.py
```
# Configuration

- ポートを変更するには ```PORT = 5555``` を編集します
- 1023以下のポートで実行したい場合はroot権限で実行せずに下記のようにしてください

```
iptables -A PREROUTING -t nat -p tcp --dport 実行したいポート番号 -j REDIRECT --to-port 5555
```

# Developers

- Motohisa Yagi

# Disclaimer

This software is released under the MIT License, see LICENSE file.

