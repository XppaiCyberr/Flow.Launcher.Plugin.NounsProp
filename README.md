# Nouns Proposal Search (Flow.Launcher.Plugin.NounsProp)

Search Nouns DAO proposals directly from [Flow Launcher](https://github.com/Flow-Launcher/Flow.Launcher)

![screenshot](assets/app.png)

## About

Quickly search and open Nouns DAO proposals on [nouncil.club](https://nouncil.club). Search by proposal ID, title, or proposer ENS name.

## Features

- 🔍 **Fast Search** - Search proposals by ID, title, or proposer ENS
- 🚀 **Quick Access** - Open proposals directly in your browser
- 📊 **Status Display** - See proposal status at a glance
- 🌐 **Live Data** - Fetches latest proposals from GitHub

## Requirements

Flow Launcher will automatically install Python if needed.

## Usage

| Keyword | Description |
|---------|-------------|
| `np` | Show recent proposals |
| `np {query}` | Search proposals by ID, title, or proposer |

### Examples

- `np 100` - Find proposal #100
- `np auction` - Search proposals containing "auction"
- `np vitalik.eth` - Find proposals by a specific ENS

Press **Enter** to open the selected proposal on nouncil.club.

## Installing

### Package Manager

Use the `pm install Nouns Proposal Search` command from within Flow Launcher.

### Manual

1. Download the latest release zip
2. Extract to `%APPDATA%\FlowLauncher\Plugins\`
3. Restart Flow Launcher

## Development

### Local Setup

```bash
pip install -r requirements.txt -t ./lib
```

### Building

Push to `main` branch to trigger automated build and release.

## License

MIT License - see [LICENSE](LICENSE) file.

## Links

- [Nouncil Club](https://nouncil.club)
- [Nouns DAO](https://nouns.wtf)
- [Flow Launcher](https://www.flowlauncher.com)
