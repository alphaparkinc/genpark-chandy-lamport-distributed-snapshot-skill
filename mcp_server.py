import sys
import json
from client import ChandyLamportNode

def main():
    node = ChandyLamportNode(node_id=1, channels=["ch1"])
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "receive_marker":
            res = {"action": node.receive_marker(params.get("channel_id"))}
        elif method == "get_state":
            res = {"local_state": node.local_state, "recorded": node.has_recorded_state}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
