class ChandyLamportNode:
    """
    Chandy-Lamport Distributed Snapshot algorithm maintaining node local state
    and recording inflight channel messages upon marker arrival.
    """
    def __init__(self, node_id, channels):
        self.node_id = node_id
        self.channels = {c: [] for c in channels}
        self.local_state = 100
        self.has_recorded_state = False
        self.channel_recording = {c: False for c in channels}
        self.recorded_channel_msgs = {c: [] for c in channels}

    def start_snapshot(self):
        self.has_recorded_state = True
        for c in self.channels:
            self.channel_recording[c] = True
        return "MARKER"

    def receive_marker(self, channel_id):
        if not self.has_recorded_state:
            self.has_recorded_state = True
            self.channel_recording[channel_id] = False
            for c in self.channels:
                if c != channel_id:
                    self.channel_recording[c] = True
            return "FORWARD_MARKER"
        else:
            self.channel_recording[channel_id] = False
            return "SNAPSHOT_CHANNEL_CLOSED"

    def receive_message(self, channel_id, msg):
        if self.channel_recording.get(channel_id, False):
            self.recorded_channel_msgs[channel_id].append(msg)
        self.local_state += msg
