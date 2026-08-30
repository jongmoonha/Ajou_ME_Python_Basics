# -*- coding: utf-8 -*-
# Practice_Python_Basics.ipynb 생성 스크립트.
# 기존 한국어 노트북을 영어 강의 규약(CLAUDE.md "Language — English only")에 맞춰 영문화한다.
# 원본의 셀 구성과 코드 동작은 유지하고, docstring -> # 주석, 메타 코멘트 제거,
# 다른 강의 회차 참조 제거, 암호 같은 변수명 풀어쓰기만 함께 반영한다.

import json

NOTEBOOK = "Practice_Python_Basics.ipynb"

cells = []


def md(text):
    cells.append(("markdown", text.strip("\n")))


def code(text):
    cells.append(("code", text.strip("\n")))


# ---------------------------------------------------------------- 0. Intro
md(r"""
# Practice 01 — Python Basics

This notebook covers the **Python fundamentals** you need in order to read and write AI / machine learning
code.

### Objectives
- Understand Python's basic data types and operators
- Use the core data structures: lists, tuples, and dictionaries
- Control program flow with conditionals and loops
- Define and call functions
- Understand classes and inheritance
- Get started with NumPy arrays and Matplotlib visualization

""")

md(r"""
### Contents

| Section | Topic |
|:---:|------|
| 0 | Terminology |
| 1 | Variables and Data Types |
| 2 | Data Structures (list, tuple, dict) |
| 3 | Control Flow (conditionals, loops) |
| 4 | Functions |
| 5 | List Comprehensions and Lambda Functions |
| 6 | String Formatting |
| 7 | Classes and Object-Oriented Programming |
| 8 | NumPy Basics |
| 9 | Matplotlib Basics |
| 10 | Loading Data |
| 11 | Pandas Basics |
| 12 | Summary |
""")

md(r"""
### Using Jupyter Notebook

| Shortcut | Action |
|--------|------|
| `Shift + Enter` | Run the current cell and move to the next one |
| `Ctrl + Enter` | Run the current cell and stay on it |
| `Esc` | Leave edit mode (the shortcuts below then work) |
| `A` | Insert a new cell above |
| `B` | Insert a new cell below |
| `M` | Change the cell to markdown |
| `Y` | Change the cell to code |

""")

md(r"""
- The marker to the left of a cell: `[ ]` not run &nbsp;|&nbsp; `[*]` running &nbsp;|&nbsp; `[number]`
  finished
- **Edit the code cells and re-run them as you read — that is how this notebook is meant to be used.**
""")

md(r"""
### Using Google Colab

[Google Colab](https://colab.research.google.com/) is a **cloud-based Jupyter environment** that runs Python
code directly in the browser.
Nothing to install, and a GPU is available, which makes it convenient for deep learning practice.

""")

md(r"""
#### Main differences from a local Jupyter Notebook

| Item | Jupyter Notebook (local) | Google Colab |
|------|------------------------|--------------|
| Where code runs | Your machine | Google servers (cloud) |
| Installation | Python + Jupyter required | A browser is enough |
| GPU | Needs separate setup | **Runtime -> Change runtime type -> GPU** |
| File storage | Local disk | Google Drive |
| Kernel menu | Kernel | **Runtime** |
| Session | Alive until you shut it down | **Disconnects automatically when idle** |

""")

md(r"""
#### Frequently used shortcuts (the ones that differ from Jupyter)

| Shortcut | Action |
|--------|------|
| `Ctrl + M, B` | Insert a new cell below (Jupyter: `B` alone) |
| `Ctrl + M, A` | Insert a new cell above (Jupyter: `A` alone) |
| `Ctrl + M, M` | Change the cell to markdown |
| `Ctrl + M, Y` | Change the cell to code |
| `Ctrl + M, D` | Delete the cell (Jupyter: `D, D`) |
| `Ctrl + /` | Toggle comments on the selection |

> Colab enters command mode with `Ctrl + M` instead of `Esc`.

""")

md(r"""
#### Colab-only features

```python
# (1) check whether a GPU is available
import torch
print(torch.cuda.is_available())   # True means a GPU is available

# (2) mount Google Drive to read data files
from google.colab import drive
drive.mount('/content/drive')

# (3) install a package straight from a cell
!pip install some_package

# (4) upload / download files
from google.colab import files
files.upload()                     # your machine -> Colab
files.download('result.csv')       # Colab -> your machine
```

> **Tip:** a Colab session **disconnects automatically** after roughly 90 minutes of inactivity.
> Save important results to Google Drive or pull them down with `files.download()` before that happens.
""")

code(r"""
# Run your first Python code
print("Hello, Mechanical Engineering!")
print("Welcome to the AI course!")
""")

# ---------------------------------------------------------------- 0. Terminology
md(r"""
---
# 0. Terminology and Basics

Before reading any code, here are the terms that keep coming back.

| Term | Meaning | Example |
|------|------|------|
| **variable** | A name that stores data | `x = 10` |
| **function** | Something called as `name()` | `print()`, `len()` |
| **library** | Functions written by someone else, brought in with `import` | `import numpy as np` |
| **library function** | A function that lives inside a library: `library.function()` | `np.sqrt()`, `np.mean()` |
| **method** | A function attached to a variable: `variable.method()` — with parentheses | `arr.reshape(2, 3)` |
| **attribute** | Information stored on a variable: `variable.attribute` — no parentheses | `arr.shape`, `arr.dtype` |
""")

code(r"""
# library: bring it in with import
import numpy as np

# calling a function inside the library: np.function_name()
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.sqrt(16))              # the sqrt function inside np
print(np.mean(arr))             # the mean function inside np

# method: a function attached to the variable -> variable.method()
print(arr.reshape(2, 3))        # the reshape method attached to arr
print(arr.sum())                # the sum method attached to arr

# attribute: information stored on the variable -> variable.attribute (no parentheses)
print(arr.shape)                # size of the array
print(arr.dtype)                # data type of the array

# list the methods and attributes a variable has (in Colab, type arr. and press Tab)
print(dir(arr))
""")

code(r"""
# print and f-strings: how to display the value of a variable
lecture_number = 1
topic = "Python Basics"

print("Hello, Mechanical Engineering!")              # fixed text
print(f"This is lecture number {lecture_number}")    # f"...{variable}..." inserts the value
print(f"Topic: {topic}")                             # string variables work too
print(f"Next lecture: number {lecture_number + 1}")  # you can compute inside the braces
""")

# ---------------------------------------------------------------- 1. Variables
md(r"""
---
# 1. Variables and Data Types

In Python a **variable** is a name attached to a piece of data.
Unlike C or MATLAB, you **do not declare the type** when you create a variable.

> **Why this matters.** In machine learning the data itself is numeric (`int`, `float`),
> while the model output is read back as a string (`str`) or a truth value (`bool`).
""")

md(r"""
### 1.1 Basic Data Types
""")

code(r"""
# integers (int) - number of measurements, number of samples, ...
num_samples = 100         # number of training samples
num_features = 4          # number of features (for example, the iris data)
print(num_samples, type(num_samples))

# floats (float) - temperature, pressure, learning rate, ...
temperature = 25.3        # temperature in Celsius
lr = 0.001                # learning rate
pi = 3.14159
print(temperature, type(temperature))
print(lr, type(lr))
""")

code(r"""
# strings (str) - file paths, label names, ...
material = "Steel"
label = 'setosa'          # name of an iris species
file_path = "data/iris.csv"
print(material, type(material))

# booleans (bool) - conditions, whether to use a GPU, ...
is_training = True
use_gpu = False
print(is_training, type(is_training))

# a comparison also evaluates to a bool
print(1 > 2, type(1 > 2))        # False
print(10 >= 10, type(10 >= 10))  # True
""")

md(r"""
### 1.2 Arithmetic Operators

| Operator | Meaning | Example | Result |
|:---:|------|------|:---:|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `3 - 2` | `1` |
| `*` | Multiplication | `3 * 2` | `6` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder | `7 % 2` | `1` |
| `**` | Power | `3 ** 2` | `9` |
""")

code(r"""
# engineering example: area and second moment of area of a circular section
import math

radius = 0.05  # radius of 50 mm = 0.05 m

area = math.pi * radius ** 2                    # area A = pi * r^2
moment_of_inertia = math.pi * radius ** 4 / 4   # second moment of area I = pi * r^4 / 4

print("Cross-sectional area:", area, "m^2")
print("Second moment of area:", moment_of_inertia, "m^4")
""")

md(r"""
### 1.3 Type Conversion

Machine learning code converts types constantly.
Converting image data from integers (0-255) to floats (0.0-1.0) with `float()` is a typical case.
""")

code(r"""
# type conversion
pixel_value = 128                        # pixel value of an image (integer 0-255)
normalized = float(pixel_value) / 255.0  # normalization: convert to a float in 0.0-1.0
print(f"original: {pixel_value}, type: {type(pixel_value)}")
print(f"normalized: {normalized:.4f}, type: {type(normalized)}")  # :.4f prints 4 decimals (Section 6)

# string -> number
epoch_str = "100"
epoch_num = int(epoch_str)
print(f"string '{epoch_str}' -> integer {epoch_num}")
""")

md(r"""
### 1.4 Assignment and Multiple Assignment

Python lets you assign several variables on one line.
This pattern shows up **constantly** in ML code when a dataset is loaded.

```python
# code you will see often:
(x_train, y_train), (x_test, y_test) = mnist.load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
```
""")

code(r"""
# multiple assignment
width, height, channels = 28, 28, 1   # MNIST image size
print(f"image size: {width} x {height} x {channels}")

# swapping values - shorter than in most other languages
a, b = 10, 20
print(f"before swap: a={a}, b={b}")
a, b = b, a
print(f"after swap:  a={a}, b={b}")
""")

md(r"""
### Exercise 1

1. Store 100.0 (unit: N) in a variable `force` and 0.01 (unit: m^2) in `area`, then compute and print the
   stress (`stress = force / area`).
2. Use `type()` to check the data type of the result.
3. Convert the result to an integer (`int`) and print it.
""")

code(r"""
# Exercise 1 - your answer here



""")

# ---------------------------------------------------------------- 2. Data structures
md(r"""
---
# 2. Data Structures

The core Python data structures: **list**, **tuple**, and **dictionary (dict)**.

> **Why this matters.**
> - **list**: recording training losses, collecting predictions (`losses = []`, `losses.append(...)`)
> - **tuple**: values that must not change, such as an image shape `(28, 28, 1)` or a kernel size `(3, 3)`
> - **dict**: hyperparameter settings and training histories (`history['accuracy']`)
""")

md(r"""
### 2.1 List
""")

code(r"""
# list - an ordered, mutable collection of data
# indispensable for recording the training process in ML

# creating a list
scores = [92, 87, 95, 78, 88]
print("exam scores:", scores)
print("number of students:", len(scores))
print("first:", scores[0])
print("last:", scores[-1])        # a negative index counts from the end

# create an empty list and grow it with append
losses = []
losses.append(2.35)               # loss of epoch 1
losses.append(1.82)               # loss of epoch 2
losses.append(0.95)               # loss of epoch 3
print("recorded losses:", losses)
""")

code(r"""
# indexing and slicing - the basis of NumPy array manipulation
# Python indices start at 0

feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print("first:        ", feature_names[0])    # first element
print("last:         ", feature_names[-1])   # last element
print("index 1 to 2: ", feature_names[1:3])  # indices 1 through 2 (3 is excluded)
print("start to 1:   ", feature_names[:2])   # from the start through index 1
print("2 to the end: ", feature_names[2:])   # from index 2 to the end
""")

code(r"""
# list operations and methods
layers = [784, 128, 64]
layers.append(10)               # append at the end
print("network structure:", layers)

layers.insert(1, 256)           # insert at index 1
print("after inserting a layer:", layers)

layers.remove(256)              # remove by value
print("after removing a layer:", layers)

# concatenating lists
train_acc = [0.8, 0.85, 0.9]
test_acc = [0.75, 0.80, 0.85]
all_acc = train_acc + test_acc
print("\nall accuracies:", all_acc)

# sorting
scores = [92, 87, 95, 78, 88]
print("ascending: ", sorted(scores))
print("descending:", sorted(scores, reverse=True))
""")

md(r"""
### 2.2 Tuple

A tuple is like a list, but it is **immutable**. In ML / DL code it is used for values that must not change:
data shapes, kernel sizes, and so on.

```python
# code you will see often:
input_shape = (28, 28, 1)
kernel_size = (3, 3)
pool_size = (2, 2)
```
""")

code(r"""
# tuple - an immutable collection of data
image_shape = (28, 28, 1)     # (height, width, channels)
kernel_size = (3, 3)
pool_size = (2, 2)

print(f"image shape: {image_shape}")
print(f"height: {image_shape[0]}, width: {image_shape[1]}, channels: {image_shape[2]}")

# tuple unpacking
height, width, channels = image_shape
print(f"H={height}, W={width}, C={channels}")

# a tuple cannot be modified
# image_shape[0] = 32  # uncommenting this line raises a TypeError
""")

md(r"""
### 2.3 Dictionary

A dictionary stores **key-value** pairs.
In ML it holds hyperparameter settings, training histories, and similar records.
""")

code(r"""
# dictionary - convenient for managing hyperparameters
hyperparams = {
    'lr': 0.001,
    'batch_size': 128,
    'epochs': 30,
    'optimizer': 'Adam'
}

print("learning rate:", hyperparams['lr'])
print("batch size:", hyperparams['batch_size'])

# modifying and adding values
hyperparams['epochs'] = 50           # change the value of an existing key
hyperparams['dropout_rate'] = 0.5    # add a new key-value pair
print("\nafter modification:", hyperparams)

# accessing keys and values
print("\nkeys:  ", list(hyperparams.keys()))
print("values:", list(hyperparams.values()))

# iterating over key-value pairs at once (for loops: Section 3)
print("\nall settings:")
for key, value in hyperparams.items():
    print(f"  {key}: {value}")
""")

code(r"""
# keeping a training history in a dictionary (a real ML code pattern)
history = {'accuracy': [], 'loss': []}

# epoch 1
history['accuracy'].append(0.65)
history['loss'].append(2.1)

# epoch 2
history['accuracy'].append(0.78)
history['loss'].append(1.5)

# epoch 3
history['accuracy'].append(0.85)
history['loss'].append(0.9)

print(f"history: {history}")
print(f"final accuracy: {history['accuracy'][-1]}")
print(f"number of epochs: {len(history['accuracy'])}")
""")

md(r"""
### 2.4 Comparison of the Three Data Structures

| Property | list `[ ]` | tuple `( )` | dict `{ }` |
|:---:|:---:|:---:|:---:|
| Mutable | O | **X** | O |
| Ordered | O | O | O (3.7+) |
| Indexed by | number | number | key |
| Typical ML use | recording values | shapes, sizes | settings, histories |
""")

md(r"""
### Exercise 2

1. Build a list from the five temperature readings `[22.1, 23.5, 21.8, 24.2, 22.9]` and print **only the
   first three** using slicing.
2. Describe a beam with a dictionary: `length` = 2.0 m, `material` = "Steel", `area` = 0.01 m^2.
   Then print the value of the `'material'` key.
3. Create `history = {'score': [], 'passed': []}`.
   For the three student scores `[85, 42, 73]`, append each score to `'score'` and append `True` to
   `'passed'` if the score is at least 60 and `False` otherwise.
   Print the final `history`.
4. Create an empty list, `append` the values 1, 4, 9, 16, 25 to it, and print the whole list.
""")

code(r"""
# Exercise 2 - your answer here


""")

# ---------------------------------------------------------------- 3. Control flow
md(r"""
---
# 3. Control Flow

The syntax that controls the order statements run in.

> **Why this matters.**
> - **comparison / logical operators**: deciding whether a condition holds
> - `if/elif/else`: classifying a prediction, deciding whether to use a GPU
> - `for` loops: **iterating over epochs**, processing batches, evaluating
> - `while` loops: checking a convergence criterion

> **Careful.** Python marks code blocks by **indentation**, not by braces `{}` as in C or Java.
> Use **four spaces** per level.
""")

md(r"""
### 3.1 Comparison and Logical Operators
""")

code(r"""
# comparison operators - used constantly for branching in ML code
accuracy = 0.95
threshold = 0.90

print("accuracy > threshold :", accuracy > threshold)   # True
print("accuracy == 1.0     :", accuracy == 1.0)         # False
print("accuracy >= 0.95    :", accuracy >= 0.95)        # True
print("accuracy != threshold:", accuracy != threshold)  # True

# logical operators
is_accurate = accuracy > 0.90
is_fast = True
print("\nis_accurate and is_fast:", is_accurate and is_fast)  # True only if both are True
print("is_accurate or is_fast :", is_accurate or is_fast)     # True if either one is True
print("not is_accurate        :", not is_accurate)            # negation
""")

md(r"""
### 3.2 Conditionals (if / elif / else)
""")

code(r"""
# conditional - grading a model by its accuracy
accuracy = 0.87

if accuracy >= 0.95:
    grade = "Excellent"
elif accuracy >= 0.90:
    grade = "Good"
elif accuracy >= 0.80:
    grade = "Acceptable"
else:
    grade = "Needs Improvement"

print(f"accuracy: {accuracy*100}% -> grade: {grade}")
""")

code(r"""
# conditional expression - a pattern that appears often in real ML code
import random

# choosing the device depending on whether a GPU is available
# (real code calls torch.cuda.is_available())
gpu_available = random.choice([True, False])  # simulated here

# written with if-else
if gpu_available:
    device = 'cuda'
else:
    device = 'cpu'
print(f"GPU available: {gpu_available} -> device: {device}")

# the same thing as a one-line conditional expression
device = 'cuda' if gpu_available else 'cpu'
print(f"conditional expression: {device}")
""")

md(r"""
### 3.3 `for` Loops

```python
# code you will see often:
for epoch in range(n_epochs):
    for i, (X_batch, y_batch) in enumerate(dataloader):
        loss = train_step(X_batch, y_batch)
```
""")

code(r"""
# range() - generate a sequence of numbers
print("range(5)       :", list(range(5)))         # [0, 1, 2, 3, 4]
print("range(1, 6)    :", list(range(1, 6)))      # [1, 2, 3, 4, 5]
print("range(0, 10, 2):", list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

print()

# iterating over epochs (the skeleton of every ML training loop)
n_epochs = 5
for epoch in range(n_epochs):
    print(f"Epoch {epoch+1}/{n_epochs}")
""")

code(r"""
# enumerate() - index and value at the same time (very common in ML code)
feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for idx, name in enumerate(feature_names):
    print(f"feature {idx}: {name}")
""")

code(r"""
# zip() - walk through two lists in parallel
models = ['KNN', 'SVM', 'Random Forest']
accuracies = [0.93, 0.87, 0.91]

for model, accuracy in zip(models, accuracies):
    print(f"{model}: {accuracy*100:.1f}%")
""")

code(r"""
# nested loops - the skeleton of a deep learning training loop
import random

n_epochs = 3
n_batches = 4  # in real code this is len(train_loader)

for epoch in range(n_epochs):
    total_loss = 0
    for batch_idx in range(n_batches):
        batch_loss = random.random()  # a simulated loss value
        total_loss += batch_loss
    avg_loss = total_loss / n_batches
    print(f"Epoch [{epoch+1}/{n_epochs}], Avg Loss: {avg_loss:.4f}")
""")

md(r"""
### 3.4 `while` Loops
""")

code(r"""
# example: keep training until the loss is small enough

loss = 10.0
threshold = 0.5
iteration = 0

while loss > threshold:    # repeat as long as loss > threshold
    loss = loss * 0.7      # a 30% decrease per iteration (simulated)
    iteration += 1

print(f"converged after {iteration} iterations, final loss = {loss:.4f}")
""")

code(r"""
# break and continue
# early stopping: stop training once the validation loss stops improving

val_losses = [2.1, 1.8, 1.5, 1.3, 1.4, 1.6, 1.8]
patience = 2              # how many epochs without improvement we tolerate
no_improve_count = 0
best_loss = float('inf')  # initialized to infinity

for epoch, val_loss in enumerate(val_losses):
    if val_loss < best_loss:
        best_loss = val_loss
        no_improve_count = 0
        print(f"Epoch {epoch+1}: val_loss={val_loss:.2f} (improved)")
    else:
        no_improve_count += 1
        print(f"Epoch {epoch+1}: val_loss={val_loss:.2f} (no improvement {no_improve_count}/{patience})")

    if no_improve_count >= patience:
        print(f"\n>> Early stopping at epoch {epoch+1}")
        break
""")

md(r"""
### Exercise 3

1. Use a `for` loop to compute the **sum of the multiples of 3** between 1 and 100.
2. From the list `temperatures = [22, 35, 18, 40, 25, 38, 15]`, print **only the values of at least 30
   degrees**.
3. (Challenge) Print the 5 times table with a `for` loop, in the format `5 x 1 = 5`.
""")

code(r"""
# Exercise 3 - your answer here


""")

# ---------------------------------------------------------------- 4. Functions
md(r"""
---
# 4. Functions

A function groups repeated code into a **reusable block**.

> **Why this matters.** ML / DL code is organized around functions:
> preprocessing functions, training functions, evaluation functions.
> In scikit-learn, `.fit()`, `.predict()`, and `.transform()` are all functions (methods).
""")

md(r"""
### 4.1 Function Basics
""")

code(r"""
# defining and calling a function
def calculate_stress(force, area):
    # force: applied force in N
    # area: cross-sectional area in m^2
    # returns the stress in Pa
    stress = force / area
    return stress

# calling the function
result = calculate_stress(1000, 0.01)
print(f"stress: {result} Pa")
print(f"stress: {result/1e6} MPa")
""")

code(r"""
# default parameters - essential when configuring ML models
# sklearn uses them everywhere: SVC(kernel='rbf', C=1.0), MLPClassifier(hidden_layer_sizes=(100,))

def create_model_config(n_layers=3, lr=0.001, optimizer='Adam'):
    # return the model configuration as a dictionary
    config = {
        'n_layers': n_layers,
        'lr': lr,
        'optimizer': optimizer
    }
    return config

# using the defaults
config1 = create_model_config()
print("default configuration:", config1)

# overriding only some of the values
config2 = create_model_config(n_layers=5, lr=0.01)
print("modified configuration:", config2)
""")

code(r"""
# returning several values - common in ML evaluation functions
def evaluate_model(y_true, y_pred):
    # evaluate a model: return the accuracy and the number of errors
    correct = 0
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == pred_label:
            correct += 1
    total = len(y_true)
    accuracy = correct / total
    errors = total - correct
    return accuracy, errors    # returned as a tuple

y_true = [0, 1, 2, 1, 0, 2, 1, 0]
y_pred = [0, 1, 2, 1, 0, 1, 1, 0]  # the sixth entry differs

accuracy, errors = evaluate_model(y_true, y_pred)
print(f"accuracy: {accuracy:.2%}, number of errors: {errors}")
""")

md(r"""
### 4.2 `*args` and `**kwargs`

A function can accept a **flexible** number of arguments instead of a fixed count.

- `*args` collects any number of positional arguments into a **tuple**.
- `**kwargs` collects any number of keyword arguments into a **dictionary**.

> **Why this matters.** Many functions in ML code take a varying number of arguments:
> ```python
> # statistics over an arbitrary number of values
> calculate_mean(1, 2, 3)          # *args -> (1, 2, 3)
> calculate_mean(10, 20, 30, 40)   # *args -> (10, 20, 30, 40)
>
> # passing assorted hyperparameters flexibly
> train_model(lr=0.001, epochs=100, batch_size=32)  # **kwargs
> ```
>
> They are also central to **class inheritance**, covered in Section 7.
""")

code(r"""
# *args - a function that accepts any number of arguments
def calculate_mean(*args):
    # mean of an arbitrary number of values
    print(f"received arguments: {args} (type: {type(args)})")
    return sum(args) / len(args)

print("mean:", calculate_mean(1, 2, 3))
print("mean:", calculate_mean(10, 20, 30, 40, 50))
""")

code(r"""
# **kwargs - keyword arguments collected into a dictionary
def print_model_info(**kwargs):
    # print the model information as key-value pairs
    print(f"received arguments: {kwargs} (type: {type(kwargs)})")
    for key, value in kwargs.items():     # dict.items() from Section 2
        print(f"  {key}: {value}")

print_model_info(name="SVM", accuracy=0.93, dataset="Iris")
print()
print_model_info(model="Random Forest", n_estimators=100, max_depth=5)
""")

code(r"""
# using *args and **kwargs together
def flexible_function(required_arg, *args, **kwargs):
    print(f"required argument:          {required_arg}")
    print(f"extra positional arguments: {args}")
    print(f"extra keyword arguments:    {kwargs}")

flexible_function("hello", 1, 2, 3, name="test", value=42)
""")

md(r"""
### Exercise 4

1. Write a function `distance(x1, y1, x2, y2)` that computes the Euclidean distance between the points `(x1,
   y1)` and `(x2, y2)`.
   (Hint: `((x2-x1)**2 + (y2-y1)**2) ** 0.5`)
2. Write a function that accepts an arbitrary number of values and **returns both the maximum and the
   minimum** (use `*args`).
""")

code(r"""
# Exercise 4 - your answer here


""")

# ---------------------------------------------------------------- 5. Comprehensions
md(r"""
---
# 5. List Comprehensions and Lambda Functions

Two compact pieces of Python syntax that appear constantly when transforming data in ML code.

```python
# code you will see often:
squares = [x ** 2 for x in range(10)]
normalize = lambda x: x / 255.0
```
""")

md(r"""
### 5.1 List Comprehensions
""")

code(r"""
# a plain for loop vs a list comprehension

# option 1: a plain for loop
squares_loop = []
for i in range(10):
    squares_loop.append(i ** 2)
print("for loop:      ", squares_loop)

# option 2: a list comprehension (the same result on one line)
squares_comp = [i ** 2 for i in range(10)]
print("comprehension: ", squares_comp)
""")

code(r"""
# conditional list comprehensions
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# keep only the positive values
positives = [x for x in numbers if x > 0]
print("positive values:", positives)

# transform depending on a condition (negatives become their absolute value)
absolute = [x if x > 0 else -x for x in numbers]
print("absolute values:", absolute)

# ML pattern: compare predictions with the true labels to get the accuracy
y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]
correct = [1 if true_label == pred_label else 0 for true_label, pred_label in zip(y_true, y_pred)]
accuracy = sum(correct) / len(correct)
print(f"\ncorrect flags: {correct}")
print(f"accuracy: {accuracy:.2%}")
""")

md(r"""
### 5.2 Lambda Functions

`lambda` defines a nameless, one-line function.
It is used when the operation is short enough to fit on a single line.

```python
# a regular function written on one line
square = lambda x: x ** 2
```
""")

code(r"""
# a regular function vs a lambda function
def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2   # the same behaviour

print("regular function:", square(5))
print("lambda function: ", square_lambda(5))

# a practical use: defining a small conversion on one line
to_celsius = lambda f: (f - 32) * 5 / 9
print(f"\n100 F = {to_celsius(100):.1f} C")
print(f"212 F = {to_celsius(212):.1f} C")
""")

# ---------------------------------------------------------------- 6. Strings
md(r"""
---
# 6. String Formatting

Reporting training progress relies on string formatting.

```python
# code you will see often:
print(f'Epoch [{epoch+1}/{n_epochs}], Loss: {loss.item():.4f}')
print('iter= {},\t w0: {:3f}'.format(iteration, w0.item()))
```
""")

md(r"""
### 6.1 f-strings (recommended)
""")

code(r"""
# f-strings (the recommended way, Python 3.6+)
epoch = 5
total_epochs = 100
loss = 0.123456789
accuracy = 0.9567

print(f"Epoch [{epoch}/{total_epochs}]")
print(f"Loss: {loss:.4f}")              # 4 decimal places
print(f"Accuracy: {accuracy:.2%}")      # shown as a percentage (multiplied by 100 automatically)
print(f"Accuracy: {accuracy*100:.2f}%") # the percentage written out by hand

# alignment and padding
print()
for i in range(1, 4):
    neurons = 128 * (2 ** (3 - i))
    print(f"Layer {i}: {neurons:5d} neurons")
""")

md(r"""
### 6.2 The `.format()` Style
""")

code(r"""
# .format() - you will meet it in existing code
print('iter= {},\t w0: {:.3f},\t w1: {:.3f}'.format(10, 0.115726, 0.305614))

# a training log pattern
template = "Epoch [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%"
print(template.format(5, 100, 0.3456, 95.67))
""")

md(r"""
### 6.3 String Methods
""")

code(r"""
# practical string methods - used for file paths and data handling
filename = "model_v2_final.h5"
print("split('_'):", filename.split("_"))            # ['model', 'v2', 'final.h5']
print("endswith  :", filename.endswith(".h5"))       # True
print("replace   :", filename.replace(".h5", ".pt")) # changing the extension

# joining strings with join()
layers = [784, 128, 64, 10]
architecture = " -> ".join([str(layer_size) for layer_size in layers])
print(f"\nnetwork structure: {architecture}")
""")

# ---------------------------------------------------------------- 7. Classes
md(r"""
---
# 7. Classes and Object-Oriented Programming

A class is a blueprint that bundles **data (attributes)** and **behaviour (methods)** together.

> **Why this matters.** Almost all ML / DL code is written with classes:
> - scikit-learn: `SVC()`, `RandomForestClassifier()`, `MLPClassifier()`
> - PyTorch: models are defined by subclassing `nn.Module`
> - every model exposes `.fit()` and `.predict()` methods
>
> This section can feel dense at first, but the same patterns come back in
> **every practice notebook**, so take your time with it.
""")

md(r"""
### 7.1 Class Basics
""")

code(r"""
# the simplest possible class
class Sensor:
    # a temperature sensor

    def __init__(self, name, unit="C"):
        # constructor: called automatically when an object is created
        self.name = name           # attribute
        self.unit = unit
        self.readings = []         # list that stores the measurements

    def measure(self, value):
        # record one measurement
        self.readings.append(value)

    def get_average(self):
        # return the mean of the measurements
        if len(self.readings) == 0:
            return 0
        return sum(self.readings) / len(self.readings)

# creating an object (instance) from the class
sensor1 = Sensor("ThermoSensor_A")
sensor1.measure(22.5)
sensor1.measure(23.1)
sensor1.measure(22.8)

# reading an attribute: variable.attribute (no parentheses) - the same pattern as arr.shape in Section 0
print(f"sensor name: {sensor1.name}")
print(f"unit: {sensor1.unit}")
print(f"readings: {sensor1.readings}")

# calling a method: variable.method() (with parentheses)
print(f"average temperature: {sensor1.get_average():.1f} C")
""")

md(r"""
### 7.2 An ML-style Class: the fit / predict Pattern
""")

code(r"""
# a simple sklearn-style classifier
class SimpleThresholdClassifier:
    # threshold-based classifier
    # a feature value above the threshold is class 1, otherwise class 0

    def __init__(self, threshold=0.5):
        self.threshold = threshold
        self.is_fitted = False

    def fit(self, X, y):
        # training: use the mean of the data as the threshold
        self.threshold = sum(X) / len(X)
        self.is_fitted = True
        print(f"training done, threshold: {self.threshold:.2f}")
        return self  # sklearn convention: fit returns self

    def predict(self, X):
        # prediction
        predictions = []
        for x in X:
            if x > self.threshold:
                predictions.append(1)
            else:
                predictions.append(0)
        return predictions

# usage (the same pattern as sklearn)
X_train = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
y_train = [0, 0, 0, 0, 1, 1, 1, 1]

classifier = SimpleThresholdClassifier()
classifier.fit(X_train, y_train)

X_test = [2.5, 5.5, 4.0, 7.5]
predictions = classifier.predict(X_test)
print(f"input:      {X_test}")
print(f"prediction: {predictions}")
""")

md(r"""
### 7.3 Inheritance
""")

code(r"""
# inheritance basics
class Animal:
    def __init__(self, name):
        self.name = name
        self.default_age = 10
        print(f"Animal '{self.name}' created.")

    def speak(self):
        return "Some sound"

    def intro(self):
        print(f"I'm {self.name}, age={self.default_age}.")

# Dog inherits everything from Animal
class Dog(Animal):
    def speak(self):        # method overriding
        return "Bark!"

print("=== Animal ===")
animal = Animal("Buddy")
print(f"speak: {animal.speak()}")

print("\n=== Dog (inherits from Animal) ===")
dog = Dog("Rex")                # __init__ comes from the parent
print(f"speak: {dog.speak()}")  # speak() is the overridden version
dog.intro()                     # intro() comes from the parent
""")

md(r"""
### 7.4 `super().__init__()` with `*args` and `**kwargs`

When a child class calls the parent's `__init__`, the `*args` / `**kwargs` from Section 4 are useful: they
**forward whatever arguments the parent expects**.

```python
# forward the parent's arguments safely, even if they change later
class Dog(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # pass everything through to the parent
        self.tricks = []                    # add an attribute of the child's own
```

> This pattern is **required when defining PyTorch models**:
> without `super().__init__()` the machinery of `nn.Module` is not available.
""")

code(r"""
# super().__init__() - call the parent constructor, then modify or add attributes

# what happens without super()?
class DogWithoutSuper(Animal):
    def __init__(self, name):
        # super().__init__(name) is missing here
        self.tricks = ['sit']

print("=== without super() ===")
dog_without_super = DogWithoutSuper("Boo")   # Animal.__init__ never runs
print(f"tricks: {dog_without_super.tricks}")
try:
    dog_without_super.intro()                # fails: name and default_age were never set
except AttributeError as error:
    print(f"AttributeError: {error}")

# with super() everything works
class DogWithSuper(Animal):
    def __init__(self, *args, **kwargs):        # *args and **kwargs from Section 4
        super().__init__(*args, **kwargs)       # call the parent __init__
        self.default_age = 5                    # change an attribute set by the parent
        self.tricks = ['sit', 'shake']          # add an attribute of its own

    def speak(self):
        return "Bark!"

print("\n=== with super() ===")
dog_with_super = DogWithSuper("Max")
dog_with_super.intro()           # default_age changed from 10 to 5
print(f"tricks: {dog_with_super.tricks}")
""")

code(r"""
# a preview of the PyTorch nn.Module style
class BaseModel:
    # parent class: the basic model framework
    def __init__(self):
        self.layers = []
        self.trained = False

    def forward(self, x):
        raise NotImplementedError("the subclass must implement this")

    def summary(self):
        print(f"model layers: {self.layers}")
        print(f"trained: {self.trained}")

class MySimpleModel(BaseModel):
    # child class: a concrete model
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()  # call the parent __init__
        self.layers = [input_size, hidden_size, output_size]

    def forward(self, x):
        print(f"input -> passes through layers {self.layers} -> output")
        return x

model = MySimpleModel(784, 128, 10)
model.summary()
model.forward([1.0, 2.0, 3.0])
""")

md(r"""
### Why the two examples call `super().__init__()` differently

`DogWithSuper` forwards `*args, **kwargs` because that is exactly what `Animal.__init__` expects.

`BaseModel` takes no parameters at all, so there is nothing to hand up — `super().__init__()` alone
is enough for `MySimpleModel`.
""")

md(r"""
### Exercise 5

1. Write a `Vehicle` class with the attributes `name` and `max_speed`, and an `info()` method that prints
   both.
2. Write an `ElectricCar` class that inherits from `Vehicle`, adds a `battery_capacity` attribute, and
   overrides `info()` so that it prints the battery capacity as well.
""")

code(r"""
# Exercise 5 - your answer here


""")

# ---------------------------------------------------------------- 8. NumPy
md(r"""
---
# 8. NumPy Basics

**NumPy** is the core library for numerical computing in Python.
Every piece of ML / DL data is handled as a NumPy array or as a tensor compatible with one.

> **Why this matters.**
> - image data: a NumPy array of shape `(60000, 28, 28)`
> - feature data: a two-dimensional array of shape `(150, 4)`
> - every ML library (sklearn, tensorflow, pytorch) is built on top of NumPy
>
> ```python
> # code you will see often:
> import numpy as np
> x_train = x_train.reshape(60000, 28, 28, 1)
> x_train = x_train.astype(np.float32) / 255.0
> ```
""")

md(r"""
### 8.1 Creating Arrays
""")

code(r"""
import numpy as np

# creating arrays
a = np.array([1, 2, 3, 4, 5])
print(f"1-D array: {a}")
print(f"  shape: {a.shape}, dtype: {a.dtype}")

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(f"\n2-D array:\n{b}")
print(f"  shape: {b.shape}")

# special arrays
print(f"\nnp.zeros((2, 3)):\n{np.zeros((2, 3))}")
print(f"\nnp.ones((2, 3)):\n{np.ones((2, 3))}")
print(f"\nnp.arange(0, 10, 2): {np.arange(0, 10, 2)}")
print(f"np.linspace(0, 1, 5): {np.linspace(0, 1, 5)}")
""")

md(r"""
### 8.2 `dtype` and `astype` — the Data Type of an Array

Every element of a NumPy array has the **same data type (dtype)**. Converting the data to `float32` is a
standard preprocessing step in ML.

```python
# code you will see often:
x_train = x_train.astype(np.float32) / 255.0
```
""")

code(r"""
# checking the dtype and converting with astype
a_int = np.array([1, 2, 3, 4, 5])
print(f"integer array: {a_int}, dtype: {a_int.dtype}")

a_float = np.array([1.0, 2.0, 3.0])
print(f"float array:   {a_float}, dtype: {a_float.dtype}")

# specifying the dtype at creation time
a_f32 = np.array([1, 2, 3], dtype=np.float32)
print(f"float32:       {a_f32}, dtype: {a_f32.dtype}")

# astype() converts the whole array at once, unlike Python's float()
pixels = np.array([128, 64, 255, 0], dtype=np.uint8)   # image pixels (integers 0-255)
print(f"\nbefore: {pixels}, dtype: {pixels.dtype}")

pixels_float = pixels.astype(np.float32)               # convert to float
print(f"after:  {pixels_float}, dtype: {pixels_float.dtype}")

normalized = pixels_float / 255.0                      # normalization to 0-1
print(f"normalized: {normalized}, dtype: {normalized.dtype}")

# what if astype is skipped and the uint8 array is divided directly?
normalized_without_astype = pixels / 255.0              # NumPy upcasts automatically
print(f"without astype: dtype: {normalized_without_astype.dtype}")   # float64, not float32
""")

md(r"""
Dividing an integer array by a plain float (`255.0`) still works without `astype` — NumPy upcasts the
result automatically, but to `float64`, not `float32`.
`astype(np.float32)` is what pins the dtype down to the smaller, GPU-friendly type used in ML.
""")

md(r"""
### 8.3 `reshape` — One of the Most Important Operations in ML / DL

```python
# code you will see often:
x_train = x_train.reshape(60000, 28, 28, 1)   # input to a CNN
x_train = x_train.reshape(-1, 784)            # input to a fully connected layer
X = X.reshape(-1, 1)                          # column vector
```
""")

code(r"""
# reshape in practice
data_1d = np.arange(12)
print(f"original: {data_1d}, shape: {data_1d.shape}")

# 1-D -> 2-D (3 rows, 4 columns)
data_2d = data_1d.reshape(3, 4)
print(f"\nreshape(3, 4):\n{data_2d}")
print(f"shape: {data_2d.shape}")

# -1 means 'work this dimension out for me' (used constantly)
data_col = data_1d.reshape(-1, 1)   # column vector
print(f"\nreshape(-1, 1): shape={data_col.shape}")

# np.newaxis - add a dimension (same effect as reshape)
vec = np.array([1, 2, 3])              # shape: (3,)
col_vec = vec[:, np.newaxis]           # shape: (3, 1) - column vector
row_vec = vec[np.newaxis, :]           # shape: (1, 3) - row vector
print(f"\nvec:           shape={vec.shape}")
print(f"column vector: shape={col_vec.shape}  (= vec.reshape(-1, 1))")
print(f"row vector:    shape={row_vec.shape}  (= vec.reshape(1, -1))")

# reshaping image data
image = np.random.randint(0, 256, (28, 28))  # a 28x28 image
print(f"\noriginal image:      shape={image.shape}")
print(f"input to a CNN:      shape={image.reshape(28, 28, 1).shape}")  # add a channel
print(f"input to a FC layer: shape={image.reshape(-1).shape}")         # flatten to 1-D
""")

md(r"""
### 8.4 Indexing and Slicing
""")

code(r"""
# array indexing and slicing
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print("whole array:\n", data)
print("\nelement (0,0):", data[0, 0])
print("first row:    ", data[0, :])        # or data[0]
print("first column: ", data[:, 0])
print("submatrix:\n", data[0:2, 1:3])
""")

code(r"""
# boolean indexing - essential for filtering data in ML
# a common pattern: X_train[(y_train == 0) | (y_train == 1)] keeps two classes

labels = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2])
scores = np.array([0.8, 0.9, 0.7, 0.85, 0.95, 0.6, 0.75, 0.88, 0.72])

# keep only the samples whose label is 1
mask = labels == 1
print(f"mask: {mask}")
print(f"scores of label 1: {scores[mask]}")

# samples whose score is at least 0.8
high_scores = scores[scores >= 0.8]
print(f"\nscores of at least 0.8: {high_scores}")
""")

md(r"""
### 8.5 Vectorized Operations and Statistics
""")

code(r"""
# vectorized operations - applied to the whole array without a loop (and much faster)
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print("a + b  =", a + b)         # element-wise addition
print("a * b  =", a * b)         # element-wise multiplication
print("a * 2  =", a * 2)         # multiplication by a scalar (broadcasting)
print("a ** 2 =", a ** 2)        # element-wise square

# normalizing an image with a vectorized operation - standard preprocessing in every DL pipeline
image = np.array([128, 64, 255, 0, 192], dtype=np.uint8)
print(f"\noriginal pixels: {image} (dtype: {image.dtype})")
normalized = image.astype(np.float32) / 255.0
print(f"normalized:      {normalized} (dtype: {normalized.dtype})")
""")

code(r"""
# statistics - used for data analysis and model evaluation
np.random.seed(42)  # fix the seed for reproducibility
data = np.random.randn(100)  # 100 samples from a standard normal distribution

print(f"mean:               {np.mean(data):.4f}")
print(f"standard deviation: {np.std(data):.4f}")
print(f"minimum:            {np.min(data):.4f}")
print(f"maximum:            {np.max(data):.4f}")

# operations along an axis of a 2-D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"\nmatrix:\n{matrix}")
print(f"mean of everything:     {matrix.mean():.1f}")
print(f"mean per row (axis=1):  {matrix.mean(axis=1)}")
print(f"mean per column (axis=0): {matrix.mean(axis=0)}")
""")

md(r"""
### 8.6 `sum` and `argmax` — Core Operations of a Classifier

`sum` adds the elements of an array; `argmax` returns the **index of the largest element**.

```python
# code you will see often:
loss = np.sum((y - y_pred) ** 2)          # sum of squared errors
pred_class = np.argmax(scores, axis=1)    # predicted class of each sample
```
""")

code(r"""
# sum - totals along an axis
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"matrix:\n{matrix}")
print(f"sum of everything:      {matrix.sum()}")        # 21
print(f"sum per column (axis=0): {matrix.sum(axis=0)}") # [5, 7, 9]
print(f"sum per row (axis=1):    {matrix.sum(axis=1)}") # [6, 15]

# argmax - returns the 'index' of the maximum (how a classifier picks its prediction)
scores = np.array([[0.1, 0.7, 0.2],    # sample 0: score per class
                   [0.8, 0.1, 0.1]])   # sample 1: score per class
print(f"\nscores (2 samples x 3 classes):\n{scores}")

# axis=1 walks across the 3 classes of each row -> one prediction per sample (length 2)
print(f"argmax per row (axis=1):    {np.argmax(scores, axis=1)}")  # [1, 0] - predicted class of each sample

# axis=0 walks across the 2 samples of each column -> one winner per class (length 3)
print(f"argmax per column (axis=0): {np.argmax(scores, axis=0)}")  # [1, 0, 0] - highest-scoring sample per class
""")

md(r"""
### 8.7 Stacking Arrays
""")

code(r"""
# vstack and hstack - combining data
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("vstack (stack vertically):")
print(np.vstack((a, b)))

print("\nhstack (stack horizontally):")
print(np.hstack((a, b)))

# ML pattern: putting the training and test sets back together
features_train = np.array([[1, 2], [3, 4], [5, 6]])
features_test = np.array([[7, 8], [9, 10]])
features_combined = np.vstack((features_train, features_test))
print(f"\ntrain: {features_train.shape} + test: {features_test.shape} = combined: {features_combined.shape}")
""")

md(r"""
### 8.8 Matrix Multiplication and the `@` Operator

The central operation of a neural network: $\mathbf{y} = \mathbf{Wx} + \mathbf{b}$

`@` gives the same result as `np.dot()`, but it reads much closer to the formula.

| Operator | Meaning | Example |
|:---:|------|------|
| `*` | Element-wise multiplication | `[1,2] * [3,4]` -> `[3, 8]` |
| `@` | Matrix multiplication | `(2,3) @ (3,1)` -> `(2,1)` |

> **Every later practice notebook uses `@`.**
""")

code(r"""
# matrix operations - the central operation of a neural network
# y = Wx + b (a linear transformation)

W = np.array([[0.1, 0.2],
              [0.3, 0.4],
              [0.5, 0.6]])     # weight matrix (3x2)
x = np.array([1.0, 2.0])       # input vector (2,)
b = np.array([0.1, 0.2, 0.3])  # bias vector (3,)

# matrix-vector product plus the bias
y = np.dot(W, x) + b           # (3x2) @ (2,) + (3,) = (3,)
print(f"W shape: {W.shape}")
print(f"x shape: {x.shape}")
print(f"b shape: {b.shape}")
print(f"y = Wx + b = {y}")
""")

code(r"""
# comparing the @ operator, np.dot(), and *
import numpy as np

# the example above, rewritten with the @ operator
W = np.array([[0.1, 0.2],
              [0.3, 0.4],
              [0.5, 0.6]])     # (3, 2)
x = np.array([1.0, 2.0])       # (2,)
b = np.array([0.1, 0.2, 0.3])  # (3,)

# np.dot() and @ give the same result
y_dot = np.dot(W, x) + b
y_at  = W @ x + b
print(f"np.dot(W, x) + b = {y_dot}")
print(f"W @ x + b        = {y_at}")

# the difference between * (element-wise) and @ (matrix multiplication)
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print()
print("A * B (element-wise):")
print(A * B)     # [[5, 12], [21, 32]]
print("\nA @ B (matrix product):")
print(A @ B)     # [[19, 22], [43, 50]]

# the inverse is computed with np.linalg.inv
print("\ninverse of A:")
print(np.linalg.inv(A))
""")

md(r"""
### Exercise 6

1. Create a 5x3 matrix with `np.random.randn(5, 3)` and compute **(a)** the mean of all entries, **(b)** the
   mean of each column, and **(c)** the maximum of each row.
2. Create a random array of length 10 and print **only the values greater than 0** (boolean indexing).
3. (Challenge) Compute the dot product of the two vectors `a = [1, 2, 3]` and `b = [4, 5, 6]` with
   `np.dot()`, and compare it with the value computed by hand (`1*4 + 2*5 + 3*6`).
""")

code(r"""
# Exercise 6 - your answer here
import numpy as np


""")

# ---------------------------------------------------------------- 9. Matplotlib
md(r"""
---
# 9. Matplotlib Basics

Visualization is central to the ML workflow:
- drawing **learning curves** (loss / accuracy against epoch)
- inspecting the **data distribution**
- showing the **predictions**

```python
# code you will see often:
import matplotlib.pyplot as plt
plt.plot(history['accuracy'])
fig, axes = plt.subplots(1, 2)
plt.imshow(x_test[0], cmap='gray')
```
""")

md(r"""
### 9.1 Line Plots
""")

code(r"""
import matplotlib.pyplot as plt
import numpy as np

# a simulated learning curve
epochs = list(range(1, 11))
train_loss = [2.3, 1.8, 1.4, 1.0, 0.7, 0.5, 0.35, 0.25, 0.18, 0.12]
val_loss   = [2.5, 2.0, 1.6, 1.3, 1.0, 0.8, 0.7, 0.65, 0.63, 0.62]

plt.figure(figsize=(8, 5))
plt.plot(epochs, train_loss, 'b-o', label='Train Loss')
plt.plot(epochs, val_loss, 'r--s', label='Validation Loss')
plt.title('Model Loss', fontsize=14)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
""")

md(r"""
With `fig, ax = plt.subplots()` you control the **axes object (`ax`)** directly.
The result is identical to the `plt.plot()` style, but this pattern is required as soon as a figure holds
several subplots, so **it is worth getting used to it from the start**.

| Style | Characteristics |
|------|------|
| `plt.plot()` | Simple, but awkward once there are several plots |
| `fig, ax = plt.subplots()` | The axes object is managed explicitly and extends to subplots naturally |
""")

code(r"""
# the same figure drawn with the fig, ax pattern
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(epochs, train_loss, 'b-o', label='Train Loss')
ax.plot(epochs, val_loss, 'r--s', label='Validation Loss')
ax.set_title('Model Loss', fontsize=14)
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
""")

md(r"""
### 9.2 Several Plots in One Figure (subplots)
""")

code(r"""
# option 1: plt.subplot() - simple, but which axes you are drawing on is less explicit
train_acc = [0.65, 0.78, 0.85, 0.91, 0.94, 0.96, 0.97, 0.98, 0.985, 0.99]
val_acc   = [0.60, 0.72, 0.80, 0.86, 0.88, 0.89, 0.895, 0.90, 0.90, 0.90]

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(epochs, train_loss, 'b-')
plt.plot(epochs, val_loss, 'r--')
plt.title('Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'])
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(epochs, train_acc, 'b-')
plt.plot(epochs, val_acc, 'r--')
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'])
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
""")

code(r"""
# option 2: the fig, axes pattern - each plot is addressed explicitly as axes[0], axes[1]
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# left: the loss curves
axes[0].plot(epochs, train_loss, 'b-')
axes[0].plot(epochs, val_loss, 'r--')
axes[0].set_title('Loss')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].legend(['Train', 'Validation'])
axes[0].grid(True, alpha=0.3)

# right: the accuracy curves
axes[1].plot(epochs, train_acc, 'b-')
axes[1].plot(epochs, val_acc, 'r--')
axes[1].set_title('Accuracy')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].legend(['Train', 'Validation'])
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
""")

md(r"""
### 9.3 Scatter Plots
""")

code(r"""
# scatter plot - visualizing two-dimensional classification data
np.random.seed(42)

# two-dimensional data for three classes (an iris-like layout)
class0_x, class0_y = np.random.randn(30) + 1, np.random.randn(30) + 1
class1_x, class1_y = np.random.randn(30) + 4, np.random.randn(30) + 4
class2_x, class2_y = np.random.randn(30) + 7, np.random.randn(30) + 1

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(class0_x, class0_y, c='red', marker='o', label='Class 0', alpha=0.7)
ax.scatter(class1_x, class1_y, c='blue', marker='s', label='Class 1', alpha=0.7)
ax.scatter(class2_x, class2_y, c='green', marker='^', label='Class 2', alpha=0.7)
ax.set_title('2D Classification Data', fontsize=14)
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
""")

md(r"""
### 9.4 Histograms and Bar Charts
""")

code(r"""
# a histogram and a bar chart side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# histogram: the distribution of the data
data = np.random.randn(1000)
axes[0].hist(data, bins=30, edgecolor='black', alpha=0.7, color='skyblue')
axes[0].set_title('Normal Distribution')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')

# bar chart: comparing model performance
models = ['LR', 'KNN', 'SVM', 'DT', 'RF']
accuracies = [0.93, 0.93, 0.87, 0.90, 0.87]
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'plum']
axes[1].bar(models, accuracies, color=colors, edgecolor='black')
axes[1].set_title('Model Comparison')
axes[1].set_ylabel('Accuracy')
axes[1].set_ylim(0.8, 1.0)

plt.tight_layout()
plt.show()
""")

md(r"""
### 9.5 Displaying Images (imshow)
""")

code(r"""
# imshow - displaying an image (essential for inspecting the input data in DL)
np.random.seed(0)
fake_image = np.random.randint(0, 256, (28, 28))

fig, axes = plt.subplots(1, 3, figsize=(10, 3))

# how to use colorbar:
#   im = ax.imshow(...)   -> im carries the colour scale
#   fig.colorbar(im, ax=) -> ax says where the colour bar goes
im0 = axes[0].imshow(fake_image, cmap='gray')
axes[0].set_title('Grayscale')
fig.colorbar(im0, ax=axes[0], shrink=0.8)

im1 = axes[1].imshow(fake_image, cmap='hot')
axes[1].set_title('Hot')
fig.colorbar(im1, ax=axes[1], shrink=0.8)

im2 = axes[2].imshow(fake_image, cmap='viridis')
axes[2].set_title('Viridis')
fig.colorbar(im2, ax=axes[2], shrink=0.8)

plt.tight_layout()  # adjust the spacing between subplots so nothing overlaps
plt.show()
""")

md(r"""
### Exercise 7

1. Plot `y = sin(x)`.
   (Build `x` with `np.linspace(0, 2*np.pi, 100)` and `y` with `np.sin(x)`.)
2. Add `y = cos(x)` to the same figure, together with a legend and a title.
3. (Challenge) Use `subplot` to show the sine and the cosine side by side.
""")

code(r"""
# Exercise 7 - your answer here
import matplotlib.pyplot as plt
import numpy as np


""")

# ---------------------------------------------------------------- 10. Loading data
md(r"""
---
# 10. Loading Data

The first step of any machine learning task is to **load the data and inspect its structure**. Here we load
data in three different ways:

1. a **scikit-learn** built-in dataset
2. a **UCI ML Repository** dataset (via `fetch_openml`)
3. a **CSV file** downloaded and read with Pandas
""")

md(r"""
### 10.1 scikit-learn Built-in Datasets
""")

code(r"""
# scikit-learn built-in dataset: Iris (flower classification)
# the classic introductory ML dataset - three species separated by four features
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
print(type(iris))     # sklearn.utils.Bunch - accessed like a dictionary
print()

print("=== Iris Dataset ===")
print(f"Keys          : {list(iris.keys())}")
print(f"Feature names : {iris.feature_names}")
print(f"Target names  : {list(iris.target_names)}")
print(f"Data shape    : {iris.data.shape}")     # (150, 4)
print(f"Target shape  : {iris.target.shape}")   # (150,)
print(f"Target values : {np.unique(iris.target)}")  # [0 1 2]

# the first five samples
print("\nFirst 5 samples (features):")
print(iris.data[:5])
print(f"First 5 labels: {iris.target[:5]}")
""")

code(r"""
# scikit-learn built-in dataset: Digits (handwritten digits 0-9)
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
print(type(digits))
print()

print("=== Digits Dataset ===")
print(f"Data shape  : {digits.data.shape}")     # (1797, 64) - each 8x8 image flattened to 1-D
print(f"Image shape : {digits.images.shape}")   # (1797, 8, 8)
print(f"Classes     : {np.unique(digits.target)}")  # [0 1 2 ... 9]

# showing the images
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="gray")
    ax.set_title(f"Label: {digits.target[i]}")
    ax.axis("off")
plt.suptitle("Digits Dataset - First 10 Samples", fontsize=14)
plt.tight_layout()
plt.show()
""")

md(r"""
### 10.2 UCI ML Repository Datasets

The [UCI ML Repository](https://archive.ics.uci.edu/) is a public collection of datasets for machine
learning research. scikit-learn's `fetch_openml()` downloads many of those UCI datasets directly from the
**OpenML** servers.
""")

code(r"""
# UCI dataset: Wine Quality
# fetch_openml downloads UCI datasets that are registered on OpenML
from sklearn.datasets import fetch_openml
import pandas as pd

wine = fetch_openml(name="wine-quality-red", version=1, as_frame=True, parser="auto")
print(type(wine))
print()

print("=== Wine Quality (Red) Dataset ===")
print(f"Data type    : {type(wine.data)}")
print(f"Data shape   : {wine.data.shape}")    # (1599, 11)
print(f"Target shape : {wine.target.shape}")
print(f"Feature names: {list(wine.feature_names)}")

# it is a DataFrame, so the Pandas methods are available straight away
print("\n--- wine.data.head() ---")
wine.data.head()
""")

code(r"""
# basic statistics - describe() shows the mean, standard deviation, minimum and maximum at a glance
wine.data.describe()
""")

md(r"""
### 10.3 Downloading and Reading a CSV File

In a real project the data usually arrives as a `.csv` file.
`pandas.read_csv()` accepts a URL directly, so it downloads and reads the file in one step.

```python
# option 1: read straight from a URL (needs an internet connection)
df = pd.read_csv("https://...csv")

# option 2: download the file first, then read it locally
# !wget https://...csv -O data.csv     # download in Colab
# df = pd.read_csv("data.csv")
```
""")

code(r"""
# reading a CSV file: the Palmer Penguins dataset
# body measurements of three penguin species (Adelie, Chinstrap, Gentoo) in Antarctica
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df = pd.read_csv(url)

print("=== Penguins Dataset (CSV) ===")
print(f"Shape : {df.shape}")
print(f"Columns: {list(df.columns)}")

# the first five rows
df.head()
""")

md(r"""
---
# 11. Pandas Basics

Once data is loaded into a `pandas.DataFrame`, a handful of methods cover most everyday inspection and
cleaning.
This section walks through them using the `df` loaded above.
""")

md(r"""
### 11.1 Inspecting a DataFrame
""")

code(r"""
# summarizing the data
print("--- info() : the type and the non-null count of every column ---")
df.info()
print("\n--- describe() : basic statistics of the numeric columns ---")
df.describe()
""")

md(r"""
### 11.2 Missing Values — `isnull`, `dropna`, and `fillna`
""")

code(r"""
# isnull() marks every cell True (missing) or False (present)
print("--- isnull() : one True/False per cell ---")
print(df.isnull().head())

# summed over the rows, it gives the number of missing values per column
print("\n--- isnull().sum() : missing values per column ---")
print(df.isnull().sum())
""")

code(r"""
# dropna() on a single column (a Series) drops its missing entries
sex_column = df["sex"]
print(f"length before dropna: {len(sex_column)}")
print(f"length after dropna:  {len(sex_column.dropna())}")
""")

code(r"""
# dropna() on the whole DataFrame drops a row if ANY of its columns is missing
print(f"rows before dropna(): {len(df)}")
print(f"rows after dropna():  {len(df.dropna())}")
""")

code(r"""
# fillna() keeps every row and fills the missing values instead of dropping them
bill_length_filled = df["bill_length_mm"].fillna(df["bill_length_mm"].mean())    # numeric -> mean
sex_filled = df["sex"].fillna(df["sex"].mode()[0])                              # categorical -> mode

print(f"bill_length_mm missing, before: {df['bill_length_mm'].isnull().sum()}, "
      f"after fillna(mean): {bill_length_filled.isnull().sum()}")
print(f"sex missing, before: {df['sex'].isnull().sum()}, "
      f"after fillna(mode): {sex_filled.isnull().sum()}")
""")

md(r"""
### 11.3 Selecting and Filtering
""")

code(r"""
# a single column name returns a Series; a list of column names returns a DataFrame
print("--- df['species'] -> a Series ---")
print(df["species"].head())
print("\n--- df[['species', 'island']] -> a DataFrame ---")
print(df[["species", "island"]].head())
""")

code(r"""
# boolean indexing: df[condition] keeps only the rows where the condition is True
gentoo = df[df["species"] == "Gentoo"]
print(f"all rows: {len(df)}, Gentoo rows: {len(gentoo)}")

# value_counts() counts how many rows fall into each category
print("\n--- counts per species ---")
print(df["species"].value_counts())
""")

md(r"""
### 11.4 Putting It Together — Visualizing the Data
""")

code(r"""
# a quick look at the data: bill length by species
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# (1) histogram of the bill length per species
for species in df["species"].unique():
    subset = df[df["species"] == species]
    # bill_length_mm has a few missing values - drop them before plotting
    axes[0].hist(subset["bill_length_mm"].dropna(), bins=15, alpha=0.6, label=species)
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Count")
axes[0].set_title("Bill Length Distribution by Species")
axes[0].legend()

# (2) scatter plot of bill length against bill depth
colors = {"Adelie": "tab:blue", "Chinstrap": "tab:orange", "Gentoo": "tab:green"}
for species, color in colors.items():
    subset = df[df["species"] == species]
    axes[1].scatter(subset["bill_length_mm"], subset["bill_depth_mm"],
                    c=color, label=species, alpha=0.6, edgecolors="w", s=40)
axes[1].set_xlabel("Bill Length (mm)")
axes[1].set_ylabel("Bill Depth (mm)")
axes[1].set_title("Bill Length vs Depth")
axes[1].legend()

plt.tight_layout()
plt.show()
""")

md(r"""
### Exercise 8

1. Load the data with `load_iris()` and compute the **mean petal length of each species**. (Hint: split the
   samples using `iris.target`.)
2. From `penguins.csv`, keep only the **Gentoo** penguins and print the mean and the standard deviation of
   `body_mass_g`.
3. (Challenge) Draw a scatter plot of the first two iris features (sepal length, sepal width), using a
   different colour for each species.
""")

code(r"""
# Exercise 8 - your answer here



""")

# ---------------------------------------------------------------- 12. Summary
md(r"""
---
# 12. Summary

### 12.1 Import Patterns

The import patterns you will type in every practice notebook.
""")

code(r"""
# (1) importing a whole module (as: giving it an alias)
import numpy as np
import matplotlib.pyplot as plt

# (2) importing only a specific function or class from a module
from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split   # used later
# from sklearn.metrics import accuracy_score             # used later

# check
print(f"NumPy version: {np.__version__}")
print("imports succeeded")
""")

md(r"""
### 12.2 The Main Libraries Used in This Course

| Library | Import pattern | Purpose |
|-----------|-------------|------|
| NumPy | `import numpy as np` | Numerical computing, array operations |
| Matplotlib | `import matplotlib.pyplot as plt` | Data visualization |
| Pandas | `import pandas as pd` | Working with tabular data |
| scikit-learn | `from sklearn.xxx import YYY` | Classical ML models |
| PyTorch | `import torch; import torch.nn as nn` | Deep learning models |
""")

md(r"""
---
# Review Exercises
""")

md(r"""
### Review Exercise 1: A Temperature Analyzer Class

Write a `TemperatureAnalyzer` class that meets the following requirements.

**Requirements:**
- `__init__(self, location)`: store the name of the measurement location and initialize an empty data list
- `add_data(self, *temperatures)`: add several temperature readings at once (use `*args`)
- `get_stats(self)`: return the mean, maximum and minimum temperature as a dictionary
- `get_above(self, threshold)`: return the readings of at least `threshold` as a list (use a list
  comprehension)
- `plot(self)`: plot the temperature history with matplotlib

**Test code:**
```python
analyzer = TemperatureAnalyzer("Lab A")
analyzer.add_data(22.1, 23.5, 24.0, 22.8, 25.1, 23.2, 24.5)
print(analyzer.get_stats())
print(f"at least 24 degrees: {analyzer.get_above(24.0)}")
analyzer.plot()
```
""")

code(r"""
# Review Exercise 1 - your answer here
import matplotlib.pyplot as plt

class TemperatureAnalyzer:
    pass  # write your implementation here


# test
# analyzer = TemperatureAnalyzer("Lab A")
# analyzer.add_data(22.1, 23.5, 24.0, 22.8, 25.1, 23.2, 24.5)
# print(analyzer.get_stats())
# print(f"at least 24 degrees: {analyzer.get_above(24.0)}")
# analyzer.plot()
""")

md(r"""
### Review Exercise 2: A Single Neuron with NumPy

Implement the behaviour of a single neuron (a perceptron).

**What the neuron does:**
1. input: `x = [x1, x2, x3]` (a NumPy array)
2. weights: `w = [w1, w2, w3]` (a NumPy array)
3. bias: `b` (a scalar)
4. output: `y = 1 if (w . x + b) > 0 else 0`

**Requirements:**
- compute the inner product with `np.dot()`
- run the prediction over several input samples with a `for` loop
- print the results with an f-string
""")

code(r"""
# Review Exercise 2 - your answer here
import numpy as np

# weights and bias
w = np.array([0.5, -0.3, 0.8])
b = -0.1

# test input (3 samples)
X = np.array([
    [1.0, 0.5, 0.8],
    [0.2, 0.9, 0.1],
    [0.7, 0.3, 0.9]
])

# write your implementation here
# for each sample, compute z = w . x + b
# and print 1 if z > 0 and 0 otherwise

""")

md(r"""
### Review Exercise 3: A Gradient Descent Simulator

Recover the slope and intercept of `y = 3x + 2` with a gradient descent loop, using the hint's formulas.

**Steps:**
1. data: `x = np.linspace(0, 10, 50)`, `y = 3*x + 2 + noise`
2. start from `w = 0.0`, `b = 0.0`
3. update `w` and `b` over 100 iterations
4. `subplot`: the data with the fitted line, and the loss history

**Hint:**
```python
y_pred = w * x + b
loss = np.mean((y - y_pred) ** 2)
dw = -2 * np.mean(x * (y - y_pred))
db = -2 * np.mean(y - y_pred)
w = w - lr * dw
b = b - lr * db
```
""")

code(r"""
# Review Exercise 3 - your answer here
import numpy as np
import matplotlib.pyplot as plt

# write your implementation here

""")

md(r"""
---
## Wrap-up

**Key points:**

| Topic | Key words |
|------|----------|
| Variables / data types | `int`, `float`, `str`, `bool`, `type()` |
| Data structures | `list[ ]`, `tuple( )`, `dict{ }`, `.items()` |
| Control flow | `if/elif/else`, `for`, `while`, `enumerate`, `zip` |
| Functions | `def`, `return`, `*args`, `**kwargs` |
| Compact syntax | list comprehensions, `lambda` |
| Strings | f-strings, `.format()`, `.split()`, `.join()` |
| Classes | `class`, `__init__`, `self`, inheritance, `super()` |
| NumPy | `np.array`, `dtype`, `astype`, `reshape`, indexing, `@` |
| Matplotlib | `plt.plot`, `fig, axes`, `plt.scatter`, `plt.imshow` |
""")


# ---------------------------------------------------------------- build
def build():
    nb_cells = []
    for cell_type, source in cells:
        lines = source.split("\n")
        source_lines = [line + "\n" for line in lines[:-1]] + [lines[-1]]
        if cell_type == "markdown":
            nb_cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": source_lines,
            })
        else:
            nb_cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": source_lines,
            })

    notebook = {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "base",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.13.5",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    with open(NOTEBOOK, "w", encoding="utf-8") as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
        f.write("\n")

    print(f"{NOTEBOOK} written ({len(nb_cells)} cells)")


if __name__ == "__main__":
    build()
