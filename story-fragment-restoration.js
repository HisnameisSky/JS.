const shuffledFragments = [
  { id: 15, text: "and, after a time, passed the place where the Hare was sleeping." },
  { id: 12, text: "he lay down beside the course to take a nap" },
  ,
  { id: 11, text: "and to make the Tortoise feel very deeply how ridiculous it was for him to try a race with a Hare," },
  { id: 7, text: "but for the fun of the thing he agreed." },
  { id: 19, text: "The Hare now ran his swiftest," },
  ,
  { id: 1, text: "A Hare was making fun of the Tortoise one day for being so slow." },
  { id: 14, text: "The Tortoise meanwhile kept going slowly but steadily," },
  { id: 9, text: "marked the distance and started the runners off." },
  ,
  { id: 5, text: "I'll run you a race and prove it.\"" },
  { id: 17, text: "and when at last he did wake up," },
  { id: 2, text: '"Do you ever get anywhere?" he asked with a mocking laugh.' },
  { id: 12, text: "he lay down beside the course to take a nap" },
  ,
  { id: 8, text: "So the Fox, who had consented to act as judge," },
  { id: 20, text: "but he could not overtake the Tortoise in time." },
  { id: 5, text: "I'll run you a race and prove it.\"" },
  { id: 6, text: "The Hare was much amused at the idea of running a race with the Tortoise," },
  ,
  { id: 13, text: "until the Tortoise should catch up." },
  { id: 10, text: "The Hare was soon far out of sight," },
  { id: 12, text: "he lay down beside the course to take a nap" },
  { id: 18, text: "the Tortoise was near the goal." },
];

function compactFragments(fragments) {
  const result = [];
  let hasRemoved = false;

  for (let i = 0; i < fragments.length; i++) {
    if (fragments[i] !== undefined) {
      result.push(fragments[i]);
    } else {
      hasRemoved = true;
    }
  }

  if (hasRemoved) {
    console.log("[COMPACTED] Removed undefined elements.");
  }

  return result;
}

const compactedShuffledFragments = compactFragments(shuffledFragments);

function sortFragments(fragments) {
  const result = [...fragments];

  for (let i = 0; i < result.length - 1; i++) {
    for (let j = 0; j < result.length - 1 - i; j++) {
      if (result[j].id > result[j + 1].id) {
        const temp = result[j];
        result[j] = result[j + 1];
        result[j + 1] = temp;
      }
    }
  }

  return result;
}

const sortedFragments = sortFragments(compactedShuffledFragments);

function dedupeFragments(fragments) {
  const result = [];
  const seenIds = new Set();

  for (let i = 0; i < fragments.length; i++) {
    const item = fragments[i];
    if (!seenIds.has(item.id)) {
      seenIds.add(item.id);
      result.push(item);
    } else {
      console.log(`[DEDUPED] Duplicate id found: ${item.id}`);
    }
  }

  return result;
}

const dedupedFragments = dedupeFragments(sortedFragments);

function fillMissingFragments(fragments) {
  if (fragments.length === 0) return [];

  const result = [];

  for (let i = 0; i < fragments.length; i++) {
    const current = fragments[i];

    if (i > 0) {
      const prevId = result[result.length - 1].id;
      for (let missingId = prevId + 1; missingId < current.id; missingId++) {
        result.push({ id: missingId, text: "[...]" });
        console.log(`[FILLED] Added placeholder for missing id: ${missingId}`);
      }
    }

    result.push(current);
  }

  return result;
}

const filledFragments = fillMissingFragments(dedupedFragments);

function assembleStory(fragments) {
  const texts = [];
  for (let i = 0; i < fragments.length; i++) {
    texts.push(fragments[i].text);
  }
  return texts.join("\n");
}

console.log(assembleStory(filledFragments));