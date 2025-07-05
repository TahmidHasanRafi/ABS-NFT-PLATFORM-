
# ABS NFT Marketplace

A decentralized NFT Marketplace built on the ZKSync Era network, allowing users to mint, list, buy, and view unique NFTs. This project uses Solidity smart contracts, a Flask backend, and a responsive HTML/CSS/JavaScript frontend, leveraging Web3.py and Filebase (S3/IPFS) for asset storage.

---

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contract Details](#contract-details)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Demo
-video https://youtu.be/XQYFUFkpM48
---

## Features

- **Mint NFTs**: Upload an image, metadata is pushed to IPFS via Filebase, and a new token is minted on ZKSync.
- **List & Unlist**: Set a sale price for owned NFTs and list/unlist them on the marketplace.
- **Buy NFTs**: Purchase listed NFTs directly from the marketplace interface.
- **Profile Dashboard**: View wallet address, balance, and owned NFTs with listing controls.
- **Marketplace View**: Explore all listed NFTs for sale.

---

## Tech Stack

- **Smart Contracts**: Solidity (ERC721URIStorage) on ZKSync Era
- **Backend**: Python, Flask, Web3.py
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: Filebase (S3-compatible API) → IPFS
- **Environment**: Hardhat for compilation/deployment, dotenv for secrets

---

## Prerequisites

- Node.js & npm
- Python 3.8+
- Hardhat (`npm install --save-dev hardhat`)
- Filebase account with S3 credentials
- ZKSync Era RPC endpoint & wallet private key

---


