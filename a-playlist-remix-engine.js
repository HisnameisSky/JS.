function flattenPlaylists(playlists) {
  if (!Array.isArray(playlists)) return [];

  const result = [];
  playlists.forEach((playlist, playlistIdx) => {
    playlist.forEach((track, trackIdx) => {
      result.push({
        ...track,
        source: [playlistIdx, trackIdx]
      });
    });
  });
  return result;
}

function scoreTracks(tracks) {
  return tracks.map(track => ({
    ...track,
    score: track.votes * 10 - Math.abs(track.bpm - 120)
  }));
}

function dedupeTracks(tracks) {
  const seen = new Set();
  return tracks.filter(track => {
    if (seen.has(track.trackId)) {
      return false;
    }
    seen.add(track.trackId);
    return true;
  });
}

function enforceArtistQuota(tracks, maxPerArtist) {
  const artistCounts = {};
  return tracks.filter(track => {
    const count = artistCounts[track.artist] || 0;
    if (count < maxPerArtist) {
      artistCounts[track.artist] = count + 1;
      return true;
    }
    return false;
  });
}

function buildSchedule(tracks) {
  return tracks.map((track, index) => ({
    slot: index + 1,
    trackId: track.trackId
  }));
}

function remixPlaylist(playlists, maxPerArtist) {
  const flattened = flattenPlaylists(playlists);
  const scored = scoreTracks(flattened);
  const deduped = dedupeTracks(scored);
  const quotaEnforced = enforceArtistQuota(deduped, maxPerArtist);
  return buildSchedule(quotaEnforced);
}