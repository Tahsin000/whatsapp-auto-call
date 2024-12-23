# WhatsApp Auto Call Script

This project automates calling a WhatsApp user at regular intervals using Python. It uses the `pyautogui` library for GUI automation and the `python-dotenv` package to manage environment variables.

## Features

- Open WhatsApp desktop app
- Search for a user by name
- Automatically call the user
- Interval-based calling (adjustable via environment variable)
- Print the call count and wait time in the terminal

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.6 or higher
- WhatsApp Desktop App installed and logged in

### Install Dependencies

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tahsin000/whatsapp-auto-call.git
   cd whatsapp-auto-call
   ```

2. **Create and activate a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On MacOS/Linux
   source venv/bin/activate
   ```

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the `pyautogui` library** (if not already listed in `requirements.txt`):
   ```bash
   pip install pyautogui
   ```

5. **Install the `python-dotenv` library** (for handling environment variables):
   ```bash
   pip install python-dotenv
   ```

## Setting Up Environment Variables

To set up the environment variables, create a `.env` file in the root directory of the project.

1. **Create a `.env` file** in the root folder of the project.

2. **Add the following environment variables** to your `.env` file:

   ```ini
   WHATSAPP_USER=YourUserName
   INTERVAL=165
   ```

   - `WHATSAPP_USER`: The name of the user you want to call on WhatsApp.
   - `INTERVAL`: The time interval (in seconds) between each call. You can adjust this based on your requirements.

   For example:

   ```ini
   WHATSAPP_USER=John Doe
   INTERVAL=165
   ```

## How to Run the Script

1. Open the terminal and navigate to the project folder.
2. Run the script using the following command:

   ```bash
   python whatsapp_auto_call.py
   ```

   The script will start and automatically open WhatsApp, search for the user, and make a call at the specified interval. The call count and wait time will be displayed in the terminal.

### Example Output:

```
Call 1 has been made to John Doe. Wait for 2 minutes and 45 seconds.
Call 2 has been made to John Doe. Wait for 2 minutes and 45 seconds.
Call 3 has been made to John Doe. Wait for 2 minutes and 45 seconds.
...
```
## Stopping the Script

To stop the script, press `Ctrl + C` in the terminal.


## Notes

- The script assumes the WhatsApp desktop app is installed and running. If the app is not open, the script will open it automatically.
- Make sure that the coordinates of the call button in the `click_call_button()` function (`pyautogui.click(1845, 70)`) are correct for your screen resolution. You can adjust the coordinates if needed.

## Contributing

Feel free to fork this project, open an issue, or submit a pull request if you want to contribute.


### Explanation of Sections:
- **Features**: Lists the capabilities of the script.
- **Prerequisites**: Mentions Python version and necessary installations.
- **Install Dependencies**: Provides the steps for cloning the repository and installing required packages.
- **Setting Up Environment Variables**: Explains how to create and configure the `.env` file for the script to work.
- **How to Run the Script**: Walks the user through running the script.
- **Example Output**: Shows how the script's terminal output will look.
- **Stopping the Script**: Instructions for stopping the script.
- **Notes**: Any important information or adjustments required for running the script.
- **Contributing**: Encourages others to contribute or open issues.
- **License**: Specifies the licensing information for the repository.
