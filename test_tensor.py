
import tensorflow as tf

try:
    from google.colab import drive
    COLAB = True
    print("Note: using Google Colab")

except ModuleNotFoundError:
    print("Note: not using Google Colab")
    COLAB = False

print("TensorFlow version:", tf.__version__)
