"""Per-assertion contributors, activities and surface templates of English ConceptNet links (no Wiktionary).

Output TSV (gz): rel, start, end, dataset, contributors ('|'), activities ('|'), template (surface text with
the two concept spans replaced by [[X]] / [[Y]]). Used to examine how answer lists were collected.
"""
import argparse, gzip, json, re

SPAN = re.compile(r"\[\[(.*?)\]\]")


def term(uri):
    return uri.split("/")[3]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("dump"); ap.add_argument("out")
    a = ap.parse_args()
    with gzip.open(a.dump, "rt") as f, gzip.open(a.out, "wt") as o:
        for line in f:
            _, rel, s, e, info = line.rstrip("\n").split("\t")
            if not (s.startswith("/c/en/") and e.startswith("/c/en/")):
                continue
            d = json.loads(info)
            if "wiktionary" in d.get("dataset", ""):
                continue
            src = d.get("sources", [])
            con = sorted({x.get("contributor", "") for x in src} - {""})
            act = sorted({x.get("activity", "") for x in src} - {""})
            t = d.get("surfaceText") or ""
            k = iter(("[[X]]", "[[Y]]"))
            t = SPAN.sub(lambda m: next(k, "[[?]]"), t)
            o.write("\t".join([rel[3:], term(s), term(e), d.get("dataset", ""), "|".join(con), "|".join(act), t]) + "\n")


if __name__ == "__main__":
    main()
