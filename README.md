
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
>![Screenshot 2025-07-04 005412](https://github.com/user-attachments/assets/43edaef5-4e78-4a26-8048-2bbd47c9bdc0)
>![Screenshot 2025-07-04 005438](https://github.com/user-attachments/assets/b2bce6f6-0d11-4bae-a0cc-88c1e80aa245)
>![Screenshot 2025-07-04 005506](https://github.com/user-attachments/assets/1656d392-7ac1-4f40-8dbd-818a8a373964)
>![Screenshot 2025-07-04 005523](https://github.com/user-attachments/assets/33656f6d-d78e-4f72-bf70-f6d465cc1b4f)
>![Screenshot 2025-07-04 005556](https://github.com/user-attachments/assets/c2ef1ef4-8f18-43c5-965b-74bc32a76ef9)
>![Screenshot 2025-07-04 005647](https://github.com/user-attachments/assets/eae95536-ce4b-4a5f-906c-1ebfa6e050fc)

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


