# Motogen

Motogen is a Discord music bot built with Python, utilizing the Lavalink audio system for high-quality music playback. It offers a range of features to enhance your Discord server's music experience.

## Features

* Play music from various sources
* Pause, resume, skip, and stop tracks
* Loop and shuffle playlists
* View the current queue
* Adjust volume
* High-performance audio streaming via Lavalink

## Installation

### Prerequisites

* Python 3.8 or higher
* Java 11 or higher (required for Lavalink)
* Lavalink server running locally or remotely
* Discord bot token

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Hashed0719/motogen.git
cd motogen
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

Create a `.env` file in the root directory and add the following:

```env
DISCORD_TOKEN=your_discord_bot_token
LAVALINK_HOST=localhost
LAVALINK_PORT=2333
LAVALINK_PASSWORD=your_lavalink_password
```

4. Run the bot:

```bash
python main.py
```

## Usage

Once the bot is running, invite it to your Discord server and use the following commands:

* `!play <url or search term>`: Play a song or add it to the queue
* `!pause`: Pause the current track
* `!resume`: Resume playback
* `!skip`: Skip the current track
* `!stop`: Stop playback and clear the queue
* `!queue`: Display the current queue
* `!volume <1-100>`: Set the playback volume
* `!loop`: Toggle loop mode
* `!shuffle`: Shuffle the queue

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

* Lavalink for the audio streaming server
* discord.py for the Discord API wrapper
