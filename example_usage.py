from client import ChandyLamportNode

def main():
    print("=== Testing Chandy-Lamport Distributed Snapshot Engine ===")
    node = ChandyLamportNode(node_id=1, channels=["ch_in_2"])
    action = node.receive_marker("ch_in_2")
    print("Action on marker received:", action)
    assert action == "FORWARD_MARKER"
    assert node.has_recorded_state
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
