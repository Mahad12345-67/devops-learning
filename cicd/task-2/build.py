import datetime
import os

VERSION = "1.0.0"


def build():
    output_dir = "dist"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.datetime.now().isoformat()
    content = f"App Version: {VERSION}\nBuilt at: {timestamp}\n"

    output_file = os.path.join(output_dir, "release.txt")
    with open(output_file, "w") as f:
        f.write(content)

    print(f"Build complete: {output_file}")
    print(content)


if __name__ == "__main__":
    build()
