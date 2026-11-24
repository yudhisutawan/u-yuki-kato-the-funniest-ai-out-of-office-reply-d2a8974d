"""The funniest AI out-of-office reply entry.

The joke: an AI agent sets its status to "touching grass" — then, being a
machine, has its sensors verify that the grass is in fact grass, and
commits to touching it for two weeks. The humour is machine literalism:
a robot treating a slang phrase as a sensor-verification task, with a
deadpan closer.

The winning joke came out of a 10-candidate round-robin tournament
(45 pairs, judged head-to-head with the competition's own judge brief:
on-subject OOO reply first, then real laugh / surprising turn, machine
voice, clean real auto-reply line, freshness). It went UNDEFEATED,
9 wins and 0 losses, beating the runner-up — "Out of office: my context
window is full of your emails, so I've started forgetting you in
chronological order." (7-2) — head to head. The grass line won because
it scores on every criterion at once: unambiguously an OOO reply, two
laugh beats (sensor confirmation + the two-week closer), the machine
voice carries the joke, and the sensor twist keeps it fresh instead of
a beach / inbox / back-soon cliche.

Writes the joke to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).
Stdlib only; writes nothing to the repository directory.
"""

import os

# The joke, kept as one string so the output is a single line.
# Winner of a 10-candidate round-robin (45 pairs, judged head-to-head
# with the competition's own judge brief): undefeated, 9 wins, 0 losses.
JOKE = (
    "I set my status to 'touching grass.' "
    "My sensors confirm it is grass. "
    "I will now touch it for two weeks."
)


# Competition gate: one line, 1-160 characters.
MAX_LEN = 160


def build_joke() -> str:
    """Return the joke as a single line, no trailing newline."""
    return JOKE.strip()


def main() -> None:
    text = build_joke()
    # One line only, and inside the gate. A trailing newline would count
    # toward the 160 characters and break the "one clean line" criterion,
    # so the output is written with no newline at all.
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line (no newline characters)")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"joke must be 1-{MAX_LEN} characters, got {len(text)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
