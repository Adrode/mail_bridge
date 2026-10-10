import sys
import json
import struct
import traceback
from html_parser import parse_html

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
    try:
        parse_html(message["message"])
    except Exception:
        with open("parser_error.log", "w", encoding="UTF-8") as f:
            f.write(traceback.format_exc())

    send_message({
        "reply": "Connection to Python works!",
        "received": "HTML received"
    })