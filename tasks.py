import os
import platform
from invoke import task


def is_windows():
    """
    Check if the operating system is Windows.
    """
    return platform.system().lower() == "windows"


@task
def build_docs(ctx):
    """
    Clean and build the Sphinx documentation.
    """
    docs_dir = os.path.join("docs")  # Path to the docs folder
    make_command = "make.bat" if is_windows() else "make"

    print("Cleaning previous builds...")
    if is_windows():
        ctx.run(f"cd {docs_dir} && {make_command} clean")
    else:
        ctx.run(f"make clean -C {docs_dir}")

    print("Building the documentation...")
    if is_windows():
        ctx.run(f"cd {docs_dir} && {make_command} html")
    else:
        ctx.run(f"make html -C {docs_dir}")


@task(pre=[build_docs])
def serve_docs(ctx):
    """
    Serve the Sphinx documentation locally after rebuilding it.
    """
    docs_path = os.path.join("docs", "build", "html")
    print("Starting the documentation server...")

    if not os.path.exists(docs_path):
        print(
            f"Error: Documentation directory '{docs_path}' not found. Run 'make html' first."
        )
        return

    try:
        ctx.run(
            f"python -m http.server --directory {docs_path} 8000", pty=not is_windows()
        )
    except Exception as e:
        print(f"Failed to start server: {e}")
