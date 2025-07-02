from datetime import datetime, timedelta

def count_user_sessions(events):
    # Parse timestamps and sort events by user and time
    events_sorted = sorted(events, key=lambda x: (x[0], x[1]))
    
    user_sessions = {}  # user_id -> list of (session_start, session_end) tuples
    
    session_gap = timedelta(minutes=30)
    
    for user_id, ts_str in events_sorted:
        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M")
        
        if user_id not in user_sessions:
            # First session for user
            user_sessions[user_id] = [(ts, ts)]
        else:
            sessions = user_sessions[user_id]
            last_start, last_end = sessions[-1]
            
            if ts <= last_end + session_gap:
                # Extend current session end time
                sessions[-1] = (last_start, max(last_end, ts))
            else:
                # Start new session
                sessions.append((ts, ts))
    
    # Count total sessions across all users
    total_sessions = sum(len(sessions) for sessions in user_sessions.values())
    return total_sessions


# Example usage with your corrected timestamps
events = [
    ("user1", "2025-07-01 10:00"),
    ("user1", "2025-07-01 10:10"),
    ("user1", "2025-07-01 11:00"),
    ("user2", "2025-07-01 12:00"),
    ("user2", "2025-07-01 12:30"),
    ("user2", "2025-07-01 13:00")
]

print(count_user_sessions(events))  # Output: 3