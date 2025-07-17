import dlltracer
import sys

# You can change the 'out' parameter to a file if the output is too long
# with open("dll_trace_log.txt", "w") as log_file:
#     with dlltracer.Trace(out=log_file):
#         try:
#             import mediapipe as mp
#             print(f"MediaPipe imported successfully! Version: {mp.__version__}")
#         except ImportError as e:
#             print(f"MediaPipe import failed: {e}")

# For direct console output:
with dlltracer.Trace(out=sys.stdout):
    try:
        import mediapipe as mp
        print(f"MediaPipe imported successfully! Version: {mp.__version__}")
    except ImportError as e:
        print(f"MediaPipe import failed: {e}")

print("DLL trace complete.")