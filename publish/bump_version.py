import sys


def bump_version(version):
    with open("VERSION", "w") as f:
        f.write(version)
    print(f"Version bumped to {version}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py <version>")
        sys.exit(1)
    bump_version(sys.argv[1])
