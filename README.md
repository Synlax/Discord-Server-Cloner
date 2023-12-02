**Documentation for "Discord Guild Cloner"** 🌐

## Installation 🚀

Choose one of the following installation methods based on your preference:

1. [**Manual Python Installation**](#manual-python-installation) 🐍
2. [**Makefile Installation**](#makefile-installation) 🛠️
3. [**Manual Docker Installation**](#manual-docker-installation) 🐳

### Manual Python Installation

1. **Requirements Installation:** 📦
   ```bash
   pip install -r requirements.txt
   ```
   - Install the required Python dependencies specified in the `requirements.txt` file.

2. **Run Script:** ▶️
   ```bash
   python main.py
   ```
   - Execute the Python script after installing the dependencies. Provide the necessary input, including the Discord bot token and guild IDs when prompted.

### Makefile Installation

1. **Build Docker Image:** 🏗️
   ```bash
   make build
   ```
   - Build the Docker image using the instructions in the Dockerfile.

2. **Run Docker Container:** ▶️
   ```bash
   make run
   ```
   - Launch the Docker container interactively.

3. **View Logs (Optional):** 📋
   ```bash
   make logs
   ```
   - Display the logs of the running Docker container.

4. **Clean Up (Optional):** 🧹
   ```bash
   make clean
   ```
   - Stop and remove the Docker container, and remove the Docker image.

### Manual Docker Installation

1. **Build Docker Image:** 🏗️
   ```bash
   docker build -t discord-guild-cloner .
   ```
   - Build the Docker image, providing the image name `discord-guild-cloner`.

2. **Run Docker Container:** ▶️
   ```bash
   docker run -it --rm --name guild_cloner_container discord-guild-cloner
   ```
   - Start the Docker container interactively.

3. **View Logs (Optional):** 📋
   ```bash
   docker logs guild_cloner_container
   ```
   - Display the logs of the running Docker container.

4. **Clean Up (Optional):** 🧹
   ```bash
   docker stop guild_cloner_container || true
   docker rm -f guild_cloner_container || true
   docker rmi -f discord-guild-cloner || true
   ```
   - Stop and remove the Docker container, and remove the Docker image.

## Recommended Python Version 🐍
The recommended Python version for running this script is **3.8**. Ensure you have Python 3.8 or a compatible version installed before executing the script.

Feel free to customize the script or Dockerfile according to your needs. If you encounter any issues or have questions, please open an [issue](https://github.com/synlax/discord-cloner/issues).

Happy cloning! 🚀🌈🔍