import sys
import json
import struct


def read_message():
    raw_length = sys.stdin.buffer.read(4)

    if not raw_length:
        return None

    message_length = struct.unpack("=I", raw_length)[0]

    message = sys.stdin.buffer.read(message_length)

    return json.loads(message.decode("utf-8"))


def send_message(message):
    encoded = json.dumps(message).encode("utf-8")

    sys.stdout.buffer.write(
        struct.pack("=I", len(encoded))
    )

    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()


message = read_message()

if message:
    send_message({
        "reply": "Python działa!",
        "received": message
    })