import sys
import importlib

REQUIRED = ["numpy", "pandas", "scipy", "sklearn", "matplotlib", "seaborn"]

print(f"Python {sys.version.split()[0]}")
print(f"Interpreter: {sys.executable}\n")

missing = []
for name in REQUIRED:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"  ok      {name:<12} {version}")
    except ImportError:
        print(f"  MISSING {name}")
        missing.append(name)

print()
if missing:
    print(f"Install these: python -m pip install {' '.join(missing)}")
else:
    print("Environment is ready.")