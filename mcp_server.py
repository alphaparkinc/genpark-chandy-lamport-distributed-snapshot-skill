"""MCP Server for Chandy-Lamport Snapshot Skill."""
import json
import sys
from client import ChandyLamportSnapshot

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "take_distributed_snapshot",
                            "description": "Capture consistent global cut using Chandy-Lamport algorithm",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "nodes": {"type": "array", "items": {"type": "string"}},
                                    "balances": {"type": "object"},
                                    "initiator": {"type": "string"}
                                },
                                "required": ["nodes", "balances", "initiator"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                engine = ChandyLamportSnapshot(args["nodes"], args["balances"])
                out = engine.record_snapshot(args["initiator"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
