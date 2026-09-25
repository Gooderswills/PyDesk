# Converting python to an exe

## Step 1

Open your terminal

## Step 2

Navigate to your project folder: `cd G:\path\to\project`


## Step 3

Install pyinstaller if needed: `pip install pyinstaller`

## Step 4

Use pyinstaller: `pyinstaller --onefile --name PyDesk main.py`

--onefile bundles everything into a single exe file

--name PyDesk sets the name for the exe to be PyDesk

main.py tells pyinstaller which file to aim for

## Step 5

There should now be a dist folder in your project folder, in here should be the exe, run it if you want to test the exe, then upload to your chosen site (Github, Itch.io etc)