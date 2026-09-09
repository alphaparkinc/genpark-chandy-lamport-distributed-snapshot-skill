"""Example usage for Chandy-Lamport Distributed Snapshot Skill."""
from client import ChandyLamportSnapshot

def main():
    print("Executing Chandy-Lamport Snapshot...")
    initial_balances = {"Agent_1": 150.0, "Agent_2": 250.0, "Agent_3": 100.0}
    snap_engine = ChandyLamportSnapshot(["Agent_1", "Agent_2", "Agent_3"], initial_balances)
    res = snap_engine.record_snapshot(initiator="Agent_1")
    print("Snapshot Result:", res)
    assert res["total_system_wealth"] == 500.0
    assert res["consistent_cut"] == True
    print("Chandy-Lamport Snapshot verified successfully!")

if __name__ == "__main__":
    main()
