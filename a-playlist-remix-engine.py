import math


def flatten_playlists(playlists):
    if not isinstance(playlists, list):
        return []

    result = []
    for p_idx, playlist in enumerate(playlists):
        for t_idx, track in enumerate(playlist):
            item = track.copy()
            item["source"] = [p_idx, t_idx]
            result.append(item)
    return result


def score_tracks(tracks):
    result = []
    for track in tracks:
        item = track.copy()
        item["score"] = track["votes"] * 10 - abs(track["bpm"] - 120)
        result.append(item)
    return result


def dedupe_tracks(tracks):
    seen = set()
    result = []
    for track in tracks:
        if track["trackId"] not in seen:
            seen.add(track["trackId"])
            result.append(track)
    return result


def enforce_artist_quota(tracks, max_per_artist):
    counts = {}
    result = []
    for track in tracks:
        artist = track["artist"]
        count = counts.get(artist, 0)
        if count < max_per_artist:
            counts[artist] = count + 1
            result.append(track)
    return result


def build_schedule(tracks):
    return [
        {"slot": i + 1, "trackId": track["trackId"]}
        for i, track in enumerate(tracks)
    ]


def remix_playlist(playlists, max_per_artist):
    flattened = flatten_playlists(playlists)
    scored = score_tracks(flattened)
    deduped = dedupe_tracks(flattened)
    quota_enforced = enforce_artist_quota(deduped, max_per_artist)
    return build_schedule(quota_enforced)