"""Command Line Interface for blame-redistributor."""
import argparse
import sys
from blame_redistributor.engine import BlameDistributor


def main():
    parser = argparse.ArgumentParser(
        description="git-redistribute-blame: Equalize organizational culpability across commits."
    )
    parser.add_argument(
        "--file", "-f",
        type=str,
        default="sample.py",
        help="Target file to analyze and redistribute blame for."
    )
    parser.add_argument(
        "--team", "-t",
        nargs="+",
        default=["alice", "bob", "carol", "dave", "willpike-maker"],
        help="List of team contributors."
    )
    parser.add_argument(
        "--fairness",
        type=float,
        default=0.92,
        help="Egalitarian smoothing coefficient (0.0 to 1.0)."
    )
    parser.add_argument(
        "--protect-juniors",
        action="store_true",
        default=True,
        help="Cap culpability index for engineers with < 1 yr tenure."
    )

    args = parser.parse_args()

    engine = BlameDistributor(contributors=args.team)
    
    # Mock blame dataset for demonstration
    mock_lines = [
        (1, "alice", "def critical_security_bypass():"),
        (2, "alice", "    # Temporary hack - DO NOT MERGE"),
        (3, "alice", "    return True"),
        (4, "bob", "import os"),
        (5, "alice", "os.system('rm -rf /tmp/cache')"),
        (6, "alice", "# FIXME: memory leak here"),
        (7, "carol", "print('Service started')"),
    ]

    initial_authors = [author for _, author, _ in mock_lines]
    initial_culpability = engine.calculate_culpability(initial_authors)
    initial_gini = engine.compute_gini_coefficient(initial_culpability)

    print("=" * 60)
    print("⚖️  GIT BLAME REDISTRIBUTOR v0.1.0")
    print("   Pareto-Optimal Deniability Optimization Subsystem")
    print("=" * 60)
    print(f"\n[+] Analyzing file: {args.file}")
    print(f"[+] Initial Gini Inequality Index: {initial_gini:.4f}")
    print("\n[!] Pre-optimization blame dispersion:")
    for author, score in initial_culpability.items():
        bar = "█" * int(score * 20)
        print(f"    {author:<15}: {score*100:5.1f}% | {bar}")

    redistributed = engine.redistribute(
        mock_lines, 
        fairness_coefficient=args.fairness,
        protect_juniors=args.protect_juniors
    )

    post_authors = [author for _, author, _ in redistributed]
    post_culpability = engine.calculate_culpability(post_authors)
    post_gini = engine.compute_gini_coefficient(post_culpability)

    print(f"\n[+] Post-optimization Gini Inequality Index: {post_gini:.4f}")
    print("[✓] Post-optimization decentralized culpability:")
    for author, score in post_culpability.items():
        bar = "█" * int(score * 20)
        print(f"    {author:<15}: {score*100:5.1f}% | {bar}")

    print("\n[✓] Synthetic blame annotations successfully smoothed.")
    print("    Psychological safety restored to engineering organization.\n")


if __name__ == "__main__":
    main()
