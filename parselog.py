from bitcoin import *
from bitcoin.net import *
from bitcoin.core import *
from bitcoin.messages import *
from StringIO import StringIO
SelectParams('mainnet')

def parse(entry):
	pieces = entry.split(' ')
	if pieces[2] == 'debug' and pieces[3] == 'sent' and pieces[4] == 'inv':
		timestamp = pieces[0] + ' ' + pieces[1]
		to = pieces[7][:-1]
		dump = pieces[8]
		s = StringIO(dump.decode('hex'))
		msg = MsgSerializable.stream_deserialize(s)
		return ('sent', timestamp, to, msg)
	elif pieces[2] == 'got' and pieces[3] == 'inv:':
		timestamp = pieces[0] + ' ' + pieces[1]
		fro = pieces[-1]
		c = CInv()
		if pieces[4] == 'tx':
			c.type = 1
		elif pieces[4] == 'block':
			c.type = 1
		c.hash = lx(pieces[5])
		m = msg_inv()
		m.inv.append(c)
		return ('recv', timestamp, fro, m)
	return None
		

if __name__ == '__main__':
	print parse('2017-03-23 03:59:33 debug sent inv msg to 213.46.222.31:8333: f9beb4d9696e7600000000000000000069010000cc0c1cb60a010000009ac38d6309b991b9b8925f1b956e8356480d8a4a294b4a39f8683beb4a4fead101000000240b7b1d7572ffde52bb65e3c2c24db5c4b39cff47ab568a8e6fba4544eb6492010000001c7f69e79ee66cdc6417eaea1a60f54520bc7e8cb2b97847873a84fc0fde3e7d010000003bbd4aa6a50959f20089872122ac280a11a09d57649cd4ecc83a443cc846f10d0100000068528db1d71c0944d2f1b90a096cd66bee2a662567e6654fe88ffa8b18535a5f01000000862cdce417b37cd5c8fd4bfa83736f33ec123aac0b7192053b9d74b2690d892701000000db361556db54993a404ae1c8d2408948d28d97404c884e2e3d49102035d20aa901000000c5dd8c2b72e1a211a5d58749820c43d2e58ec709df93426ebcfcb39e56bb35a6010000003462331be3d6e27fcd26ba27f7971a06e391bb1e56dd5475f5614129bf1288c9010000004df18b817a16cbb78c44c7f91fde62a8f06a02bd9f25bddcf9593460dc4f0e0b')
	print parse('2017-03-23 16:18:52 got inv: tx 61aa3c4aa7c4823b9ce3d621a025a4a5d381e1245b7296c1aaa5303c9070c8fc  have peer=1, 93.190.140.198:8333')
