#!/usr/bin/env python3
"""Progress tracker for autonomous-build skill. Reads feature_list.json and prints status."""

import json
import sys
from pathlib import Path


def main():
    project_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("./autonomous_build_output")
    feature_file = project_dir / "feature_list.json"

    if not feature_file.exists():
        print("No feature_list.json found")
        sys.exit(0)

    try:
        features = json.loads(feature_file.read_text())
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading feature_list.json: {e}")
        sys.exit(1)

    total = len(features)
    passing = sum(1 for f in features if f.get("passes", False))
    failing = total - passing
    pct = (passing / total * 100) if total > 0 else 0

    # Count by category
    categories = {}
    for f in features:
        cat = f.get("category", "unknown")
        if cat not in categories:
            categories[cat] = {"passing": 0, "total": 0}
        categories[cat]["total"] += 1
        if f.get("passes", False):
            categories[cat]["passing"] += 1

    print(f"Progress: {passing}/{total} passing ({pct:.1f}%)")
    print(f"Remaining: {failing} features to implement")
    for cat, counts in sorted(categories.items()):
        print(f"  {cat}: {counts['passing']}/{counts['total']}")

    # Show next features to work on
    next_features = [f for f in features if not f.get("passes", False)][:3]
    if next_features:
        print("\nNext up:")
        for i, f in enumerate(next_features, 1):
            print(f"  {i}. [{f.get('category', '?')}] {f['description'][:80]}")


if __name__ == "__main__":
    main()
